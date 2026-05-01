# text_tools_np

## Unicode to Preeti converter

### My Plan

- Open and read word file
- Get the text
- Send the text via an online text converter
- Parse the response
- Write to a new file

### Tech Stack

- python-docx
- requests
- beautifulsoup4
- lxml

### Getting Started

#### Create a virtual environment

```bash
python3 -m venv .venv
source venv/bin/activate
```

#### Install the dependencies

```bash
pip install -r requirements.txt
```

### Usage

- In `main.py`, replace the `input_file_path` and `output_file_path` with the paths to your input and output files.
- Ideally, create a `files` directory in the same directory as `main.py`.
    - `mkdir files`
- Then put the input file inside the `files` directory.
- Set `output_file_path` to something inside `files` directory. (Eg. `output.docx`)
- Run the script

```bash
python -m main
```

### To do

- [x] Convert all content to preeti
- [ ] Convert only devanagari to preeti, leave english text as it is
