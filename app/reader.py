from docx import Document
from docx.oxml.ns import qn


def read_docx(file_path):
    doc = Document(file_path)
    pages = []
    current_page = []

    for para in doc.paragraphs:

        # Explicit page break: <w:br w:type="page"/>
        has_page_break = any(
            br.get(qn("w:type")) == "page"
            for br in para._element.findall(".//" + qn("w:br"))
        )

        # Section break (next-page type): <w:sectPr> with <w:type w:val="nextPage"/>
        sect_pr = para._element.find(".//" + qn("w:sectPr"))
        has_section_break = False
        if sect_pr is not None:
            type_el = sect_pr.find(qn("w:type"))
            if type_el is not None:
                val = type_el.get(qn("w:val"), "")
                has_section_break = val in ("nextPage", "evenPage", "oddPage")

        text = para.text.strip()
        if text:
            current_page.append(text)

        if has_page_break or has_section_break:
            pages.append("\n".join(current_page))
            current_page = []

    if current_page:
        pages.append("\n".join(current_page))

    # print("Pages length:", len(pages))
    return pages


if __name__ == "__main__":
    # filepath = "files/input.docx"
    # read_docx(file_path=filepath)
    pass
