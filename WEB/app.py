import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from main1 import analyze_log_entries, print_and_save_analysis  # Import your existing functions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'log'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure the upload directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            file.save(filepath)
            # Analyze the log file
            with open(filepath, 'r') as log_file:
                log_entries = log_file.readlines()
            ip_counts, endpoint_counts, failed_logins = analyze_log_entries(log_entries)
            most_accessed_endpoint = max(endpoint_counts.items(), key=lambda x: x[1])
            csv_path = 'log_analysis_results.csv'
            print_and_save_analysis(ip_counts, endpoint_counts, failed_logins, csv_path)
            return render_template('result.html', ip_counts=ip_counts, most_accessed_endpoint=most_accessed_endpoint, failed_logins=failed_logins, csv_path=csv_path)
    return render_template('index.html')

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
