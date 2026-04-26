import os
import fitz

def load(file_path: str) -> str:
    if not file_path.endswith(".pdf"):
        raise ValueError("PDF files are not supported.")
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def load_from_folder(folder_path: str) -> str:
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            all_text += load(file_path) + "\n"
    return all_text