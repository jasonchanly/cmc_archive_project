import argparse
import os
import json
from pathlib import Path
from datetime import datetime
from time import time

from openai import OpenAI
from jinja2 import Template
from dotenv import dotenv_values

from demo_programmes import DEMONSTRATION_EXAMPLE_INPUTS_FPATHS, DEMONSTRATION_EXAMPLE_OUTPUTS
import programme_structure


def get_ic_examples(input_fpaths, example_structured_outputs):
    examples = []
    for input_fpath, example_structured_output in zip(input_fpaths, example_structured_outputs):
        with open(input_fpath) as f:
            programme_string = f.read()

        examples.append({
            "programme_string": programme_string,
            # this workaround (instead of using model.model_dump_json()) ensures utf-8 is preserved
            "programme_structured_outputs": json.dumps(example_structured_output.model_dump(mode='json'),
                                                       ensure_ascii=False, indent=2)
        })

    return examples

def get_system_prompt(fpath="prompts/Nov2025_cmc_system_prompt.jinja2", ic_examples=None):
    with open(fpath) as f:
        system_prompt_template = Template(f.read())

    return system_prompt_template.render(ic_examples=ic_examples)

def get_user_prompt_template(fpath="prompts/Nov2025_cmc_user_prompt.jinja2"):
    with open(fpath) as f:
        user_prompt_template = Template(f.read())
    return user_prompt_template

def send_requests_in_bulk(requests_dir, model="gpt-5-mini"):
    print("Preparing requests")
    start_time = time()

    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    requests_dir = Path(requests_dir) if isinstance(requests_dir, str) else requests_dir
    outputs_dir = requests_dir / f"outputs_{current_time}"
    if not outputs_dir.exists():
        outputs_dir.mkdir()

    system_prompt = get_system_prompt(ic_examples=get_ic_examples(DEMONSTRATION_EXAMPLE_INPUTS_FPATHS,
                                                                  DEMONSTRATION_EXAMPLE_OUTPUTS))
    user_prompt_tmp = get_user_prompt_template()
    for fpath_i, fpath in enumerate(requests_dir.rglob("*.txt")):
        # NB: does not catch .html or other anomaly formats
        # if encoding error - try encoding="latin-1" when opening
        with open(fpath) as f:
            programme_string = f.read()
        user_prompt = user_prompt_tmp.render(programme_string=programme_string)

        completion = client.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            prompt_cache_key="cmc_programme_archive_batch",
            response_format=programme_structure.Concert,
            service_tier="flex",

            max_completion_tokens=12500,
            reasoning_effort="low",
            timeout=900.0,
        )

        msg = completion.choices[0].message

        if msg.refusal:
            print(f"File {fpath_i} {fpath.name} failed - refusal message: {msg.refusal}")
        else:
            programme_parsed = msg.parsed
            outputs_fpath = outputs_dir / f"{fpath.name.replace('.txt', '_parsed.json')}"
            with open(outputs_fpath, "w", encoding="utf-8") as f:
                json.dump(programme_parsed.model_dump(mode='json'), f)
            print(f"File {fpath_i}: {fpath.name} processed. Time lapsed: {(time() - start_time)/60:.2f} minutes")

    print(f"All files processed. Total time lapsed: {(time() - start_time)/60:.2f} minutes")

def send_requests_in_bulk_with_ocr(requests_dir, model="gpt-5-mini"):
    print("Preparing requests")
    start_time = time()

    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    requests_dir = Path(requests_dir) if isinstance(requests_dir, str) else requests_dir
    outputs_dir = requests_dir / f"outputs_{current_time}"
    if not outputs_dir.exists():
        outputs_dir.mkdir()

    system_prompt = get_system_prompt(ic_examples=get_ic_examples(DEMONSTRATION_EXAMPLE_INPUTS_FPATHS,
                                                                  DEMONSTRATION_EXAMPLE_OUTPUTS))
    user_prompt_tmp = get_user_prompt_template(fpath="prompts/Nov2025_cmc_user_prompt_OCR_required.jinja2")
    for fpath_i, fpath in enumerate(requests_dir.rglob("*.pdf")):
        user_prompt = user_prompt_tmp.render()
        file = client.files.create(
            file=open(fpath, "rb"),
            purpose="user_data"
        )

        completion = client.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",
                 "content": [{"type": "file", "file": {"file_id": file.id, }}, {"type": "text", "text": user_prompt}]}
            ],
            prompt_cache_key="cmc_programme_archive_batch",
            response_format=programme_structure.Concert,
            service_tier="flex",
            max_completion_tokens=12500,
            reasoning_effort="low",
            timeout=900.0,
        )

        msg = completion.choices[0].message

        if msg.refusal:
            print(f"File {fpath_i} {fpath.name} failed - refusal message: {msg.refusal}")
        else:
            programme_parsed = msg.parsed
            outputs_fpath = outputs_dir / f"{fpath.name.replace('.pdf', '_parsed.json')}"
            with open(outputs_fpath, "w", encoding="utf-8") as f:
                json.dump(programme_parsed.model_dump(mode='json'), f)
            print(f"File {fpath_i}: {fpath.name} processed. Time lapsed: {(time() - start_time)/60:.2f} minutes")

    print(f"All files processed. Total time lapsed: {(time() - start_time)/60:.2f} minutes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests_dir", required=True, type=str)
    parser.add_argument("--model", required=False, default="gpt-5.4-mini", type=str)
    parser.add_argument("--ocr_required", action="store_true")

    args = parser.parse_args()

    client = OpenAI(api_key=dotenv_values(".env")["OPENAI_API_KEY"], timeout=900.0)
    if args.ocr_required:
        send_requests_in_bulk_with_ocr(args.requests_dir, args.model)
    else:
        send_requests_in_bulk(args.requests_dir, args.model)

