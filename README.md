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

#### In one go

- This only sends 1 request per page, so this is preferable.
- In `main_in_one_go.py`, replace the `input_file_path` and `output_file_path` with the paths to your input and output files.
- Ideally, create a `files` directory in the same directory as `main_in_one_go.py`.
    - `mkdir files`
- Then put the input file inside the `files` directory.
- Set `output_file_path` to something inside `files` directory. (Eg. `output.docx`)
- Run the script

```bash
python -m main_in_one_go
```

#### Deprecated

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
- [x] Convert only devanagari to preeti, leave english text as it is
- [x] Convert pages in one go instead of chunks to reduce requests
- [ ] Fix the bug of khutta kaatiyeko letters being interpreted as aadhi letters. Eg: `गर्छन्` becomes `गर्छ` + aadhi `न` like the aadhi `न` of `धन्य`. It is probably because of how I'm building payload via `_build_payload` function in `sender_in_one_go.py`. `गर्छन्` becomes `गर्छन्###N###` which the online converter interprets as the khutta kateko `न` to be aadhi `न` which is a rule of nepali grammar.
- [ ] All the spaces, commas, punctuations (like hyphens except purnabiram) are currently in Times New Roman which isn't desirable. `segment_text` function in `segmenter.py` needs to be fixed to handle this.
