import argparse
from pathlib import Path
from collections import defaultdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_name", type=str, default="7Dec2025")
    parser.add_argument("--downloaded_archive", type=str, default="data/archives_dl_from_website/2025-12-06")
    parser.add_argument("--processed_batches", nargs='*', default=["data/batch_28Nov2025", "data/batch_1Dec2025_OCR_required"])

    args = parser.parse_args()

    downloaded_archive = Path(args.downloaded_archive)

    processed_batches = [Path(x) for x in args.processed_batches]

    downloaded_archive_formats = (".docx", ".doc", ".pdf",)
    # in order of preferred format, e.g. use .docx even when there's a duplicate .pdf
    processed_batches_formats = downloaded_archive_formats + (".txt",)

    # sometimes the same concert might have a programme in both .docx and .pdf formats
    # - in that case we only need to process one of these
    all_downloaded = defaultdict(list)
    for fpath in downloaded_archive.glob("*"):
        for file_format in downloaded_archive_formats:
            if fpath.name.endswith(file_format):
                all_downloaded[str(fpath).replace(file_format, "")].append(file_format)

    print(f"Total downloaded programmes in {args.downloaded_archive} (deduplicated): {len(all_downloaded)}")

    # tally up what have already been processed
    all_processed_progs = []
    for processed_batch in processed_batches:
        for fpath in processed_batch.glob("*"):
            for processed_format in processed_batches_formats:
                if fpath.name.endswith(processed_format):
                    all_processed_progs.append(fpath.name.replace(processed_format, "").lower())
                    break

    print(f"n existing programmes already processed: {len(all_processed_progs)}")

    new_files_to_be_processed = []
    for full_fpath, file_ext_list in all_downloaded.items():
        if full_fpath.split("/")[-1].lower() not in all_processed_progs:
            new_files_to_be_processed.append(full_fpath+file_ext_list[0])

    print(f"{len(new_files_to_be_processed)} new programmes recognised.")

    with open(Path(f"data/batch_{args.batch_name}_filelist.txt"), "w") as f:
        for fpath in new_files_to_be_processed:
            f.write(fpath+"\n")

