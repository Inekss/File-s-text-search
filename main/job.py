import os
import codecs
import chardet
from docx import Document  # New import for handling .docx files


def detect_encoding(encoding_path):
    """Detect the encoding of the file using chardet for better accuracy."""
    with open(encoding_path, "rb") as file:
        raw_data = file.read(10000)  # Read a small chunk of the file
    result = chardet.detect(raw_data)
    encoding = result["encoding"]
    return encoding


def search_in_docx(search_term, path):
    try:
        doc = Document(path)
        matches = []

        for i, para in enumerate(doc.paragraphs):
            if search_term.lower() in para.text.lower():
                matches.append(f"{i + 1}: {para.text.strip()}")

        if matches:
            return "\n".join(matches)
        else:
            return f"No matches found for '{search_term}' in the file."

    except Exception as e:
        return f"Exception occurred: {str(e)}"


def search_in_file(search_term, path):
    if not os.path.isfile(path):
        return f"Error: The file '{path}' does not exist."

    if path.lower().endswith(".docx"):
        return search_in_docx(search_term, path)

    encoding = detect_encoding(path)
    if not encoding:
        return f"Error: Unable to detect file encoding for '{path}'."

    try:
        with codecs.open(path, "r", encoding=encoding, errors="ignore") as file:
            content = file.read()

        lines = content.split("\n")
        matches = [
            f"{i + 1}: {line.strip()}"
            for i, line in enumerate(lines)
            if search_term.lower() in line.lower()
        ]

        if matches:
            return "\n".join(matches)
        else:
            return f"No matches found for '{search_term}' in the file."

    except Exception as e:
        return f"Exception occurred: {str(e)}"


if __name__ == "__main__":
    file_path = r""
    request = ""
    output = search_in_file(request, file_path)
    print(output)


    # Debug information
    # print("\nDebug Info:")
    # print(f"File exists: {os.path.exists(file_path)}")
    # print(f"File size: {os.path.getsize(file_path) if os.path.exists(file_path) else 'N/A'} bytes")

    # encoding = detect_encoding(file_path)
    # print(f"Detected encoding: {encoding}")

    # try:
    #     with codecs.open(file_path, 'r', encoding=encoding) as f:
    #         content = f.read()
    #         print(f"\nFile content ({encoding}):\n{content}")
    # except Exception as e:
    #     print(f"Error reading file: {str(e)}")
