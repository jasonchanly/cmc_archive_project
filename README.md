### CMC Archive Project

Personal project to digitise 70+ years of concert programmes for my university's chamber music club into a searchable database (work in progress)

1. `website_sweep.py` - access the chamber music club's website, sweep through URLs and download the concert programmes to be processed
2. `identify_new_programmes.py` - create a list of files to be processed by filtering the downloaded programmes, removing any that have already been processed in the past. 
3. `convert_to_api_input_formats.py` - convert each .doc, .docx and .pdf to string (saved as .txt file) where possible; record problematic files for remedial action.
4. `api_inference.py` - make OpenAI API calls to parse each text string (or pdf, if OCR required) into structured outputs
   1. `programme_structure.py` - defines the schema with which each concert programme is parsed (concert date, time, pieces (name, composer...), etc.)
   2. `demo_programmes.py` - in-context examples
5. `postprocess.py` - postprocess API outputs into DataFrame for manual inspection and cleaning using OpenRefine

Create a `archive_urls.txt` containing a list of URLs where concert programmes should be extracted

In `.env`, set OPENAI_API_KEY=[your_api_key]