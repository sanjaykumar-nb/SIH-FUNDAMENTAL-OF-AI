import PyPDF2
import docx2txt
from collections import Counter

def extract_text(file_path: str) -> str:
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as f:
            return f.read()
    return ""

def summarize_text(text: str) -> str:
    sentences = text.split('.')
    if len(sentences) > 5:
        summary = '.'.join(sentences[:3]) + '.'
    else:
        summary = text[:200] + '...'
    return summary

def extract_keywords(text: str) -> list:
    words = text.lower().split()
    word_counts = Counter(words)
    common = word_counts.most_common(10)
    return [word for word, count in common if len(word) > 3]

def process_document(file_path: str) -> dict:
    text = extract_text(file_path)
    summary = summarize_text(text)
    keywords = extract_keywords(text)
    return {
        "summary": summary,
        "keywords": keywords
    }
