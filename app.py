from flask import Flask, request, render_template, redirect, url_for, session, send_file
import os
import csv, io
from utils import load_and_process_resumes, rank_resumes
from datetime import datetime

app = Flask(__name__)
@app.context_processor

def inject_now():
    return {'now': datetime.now}
app.secret_key = "your-secret-key"
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist('resumes')
        for file in files:
            if file.filename.endswith('.pdf'):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        job_description = request.form['job_description']
        session['job_description'] = job_description  # Save for next page

        # ✅ Store in session for download access
        session['results'] = sorted_results

        return redirect(url_for('results'))

    return render_template('upload.html')

@app.route('/results')
def results():
    job_description = session.get('job_description', '')
    resumes = load_and_process_resumes(app.config['UPLOAD_FOLDER'])
    results = rank_resumes(resumes, job_description)
    return render_template('results.html', results=results)

@app.route('/download')
def download_results():
    if not session.get("results"):
        return redirect(url_for('results'))

    # Prepare CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Filename", "Score"])

    for filename, score in session["results"]:
        writer.writerow([filename, f"{score:.4f}"])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='ranked_resumes.csv'
    )
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == "__main__":
    app.run(debug=True)

