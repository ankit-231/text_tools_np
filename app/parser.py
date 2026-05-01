from bs4 import BeautifulSoup


def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    textarea = soup.find("textarea", class_="out preeti")
    preeti_result = textarea.text

    return preeti_result


# if __name__ == "__main__":
#     html_file_path = "files/output.html"
#     html = load_html(html_file_path)
#     parsed_text = parse_html(html)
#     print(parsed_text)
