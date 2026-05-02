from app.reader import read_docx
from app.sender_in_one_go import send_page_in_one_go
from app.writer_in_one_go import create_doc, add_page, save_doc

import logging

logging.basicConfig(level=logging.INFO)


def main(input_file_path, output_file_path):
    pages = read_docx(input_file_path)
    doc = create_doc()

    for i, page_text in enumerate(pages):
        logging.info(f"Processing page {i+1}...")

        converted_lines = send_page_in_one_go(page_text)

        add_page(doc, converted_lines)

    save_doc(doc, output_file_path)
    logging.info(f"Saved doc to {output_file_path}")


if __name__ == "__main__":
    input_file_path = "files/input-1.docx"
    output_file_path = "files/output-1.docx"
    # input_file_path = "files/OCR-unicode.docx"
    # output_file_path = "files/OCR-preeti.docx"
    main(input_file_path, output_file_path)
