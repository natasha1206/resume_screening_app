import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return ' '.join([page.extract_text() or '' for page in pdf.pages])

def extract_keywords(text):
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])

def load_and_process_resumes(folder_path):
    resumes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            path = os.path.join(folder_path, filename)
            raw_text = extract_text_from_pdf(path)
            processed_text = extract_keywords(raw_text)
            resumes[filename] = processed_text
    return resumes

def rank_resumes(resumes, job_description_text):
    jd_keywords = extract_keywords(job_description_text)
    corpus = [jd_keywords] + list(resumes.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked_resumes = sorted(
        zip(resumes.keys(), cosine_similarities),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked_resumes
