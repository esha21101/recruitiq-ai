from docx import Document


def extract_job_description(doc_path):
    doc = Document(doc_path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


if __name__ == "__main__":
    jd = extract_job_description(
        "data/raw/job_description.docx"
    )

    print(jd[:3000])