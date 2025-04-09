import fitz  # PyMuPDF
import docx

def load_text_from_file(uploaded_file):
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        try:
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                return "\n".join([page.get_text() for page in doc])
        except Exception:
            return "Error reading PDF."

    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        try:
            doc = docx.Document(uploaded_file)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception:
            return "Error reading DOCX."

    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    return "Unsupported file format."
