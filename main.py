from app.reader import read_docx
from app.sender import send_page
from app.parser import parse_html
from app.writer import create_doc, add_page, save_doc

import logging

logging.basicConfig(level=logging.INFO)


def main(input_file_path, output_file_path):
    pages = read_docx(input_file_path)
    doc = create_doc()

    for i, page in enumerate(pages):
        logging.info(f"Processing page {i+1}...")

        logging.debug(f"Sending content to online conversion URL")
        html = send_page(page)

        logging.debug(f"Received html from response")
        logging.debug(f"Parsing html")
        parsed = parse_html(html)
        logging.debug(f"Parsed html")
        logging.debug(f"Adding parsed content to doc")
        add_page(doc, parsed)
        logging.debug(f"Added parsed content to doc")

    logging.debug(f"Saving all content to doc")
    save_doc(doc, output_file_path)
    logging.debug(f"Saved all content to doc")
    logging.info(f"Saved doc to {output_file_path}")


if __name__ == "__main__":
    input_file_path = "files/input-1.docx"
    output_file_path = "files/output-1.docx"
    main(input_file_path, output_file_path)
