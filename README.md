# 🧠 AI Resume Screening Web App

An AI-powered web tool to intelligently screen and rank PDF resumes based on a given job description. Ideal for recruiters, hiring managers, and HR tech projects.

---

## 🚀 Features

- 📄 Upload multiple PDF resumes
- 📌 Input custom job descriptions
- 🧠 Extracts resume keywords using **spaCy**
- 📊 Ranks resumes using **cosine similarity** via **scikit-learn**
- 💾 Download match results as a report
- ⚡ Responsive web interface (Flask + HTML + CSS)

---

## 🛠️ Tech Stack

- **Flask** – Lightweight Python web framework  
- **pdfplumber** – PDF text extraction  
- **spaCy** – Natural Language Processing  
- **scikit-learn** – TF-IDF vectorization & cosine similarity  
- **HTML/CSS** – Frontend UI  
- *(No JavaScript framework required)*

---

## 📁 Project Structure

``` 
resume_screening_app/
├── app.py
├── static/
│   ├── style.css
│   └── images/
│       └── undraw_online-resume_z4sp.png
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── privacy.html
│   ├── terms.html
│   ├── upload.html
│   └── results.html
├── resumes/
│   ├── alice_resume.pdf
│   ├── bob_resume.pdf
│   └── charlie_resume.pdf
├── utils.py
├── job_description.txt
└── requirements.txt
```

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/resume_screening_app.git
cd resume_screening_app

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**

```bash
pip install -r requirements.txt

4. **Run the app**

```bash
python app.py

5. **Access the app**

Open your browser and navigate to `http://localhost:5000` to see the app in action.

---

## 📝 License

MIT License

##✨ Credits
Developed by Natasha Ponnachanda
Built for academic/portfolio use.

## 💡 Future Features (Ideas)
User authentication for stored results

Dashboard analytics

Skill-based resume filtering

Integration with LinkedIn API

Email shortlist to recruiter
