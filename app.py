import re
import csv
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk

def analyze_log_entries(log_entries):
    req_count_ip = defaultdict(int)  
    access_count = defaultdict(int)   
    failed_logins = defaultdict(int)   

    for entry in log_entries:
        log_pattern = r'(\S+) - - \[.*\] "(.*?) (.*?) HTTP.*" (\d{3}) .*'
        match = re.match(log_pattern, entry)
        if match:
            ip, method, endpoint, status = match.groups()
            req_count_ip[ip] += 1
            access_count[endpoint] += 1
            
            if method == "POST" and status == "401":
                failed_logins[ip] += 1

    return req_count_ip, access_count, failed_logins

def save_to_csv(ip_counts, endpoint_counts, failed_logins):
    csv_output = []
    csv_output.append(["IP Address", "Request Count"])
    for ip, count in ip_counts.items():
        csv_output.append([ip, count])
    csv_output.append([])  
    csv_output.append(["Endpoint", "Access Count"])
    for endpoint, count in endpoint_counts.items():
        csv_output.append([endpoint, count])
    csv_output.append([])  
    csv_output.append(["IP Address", "Failed Login Count"])
    for ip, count in failed_logins.items():
        csv_output.append([ip, count])
    with open('log_analysis_output.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_output)

def analyze_log_file():
    file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("Log Files", "*.log")])
    if not file_path:
        return 
    try:
        with open(file_path, 'r') as log_file:
            log_entries = log_file.readlines()
        ip_counts, endpoint_counts, failed_logins = analyze_log_entries(log_entries)
        for text_area in result_text_areas:
            text_area.delete(1.0, tk.END)
        result_text_areas[0].insert(tk.END, "IP Address, Request Count\n")
        for ip, count in ip_counts.items():
            result_text_areas[0].insert(tk.END, f"{ip}, {count}\n")
        result_text_areas[1].insert(tk.END, "Endpoint, Access Count\n")
        for endpoint, count in endpoint_counts.items():
            result_text_areas[1].insert(tk.END, f"{endpoint}, {count}\n")
        most_accessed = max(endpoint_counts.items(), key=lambda x: x[1])
        result_text_areas[2].insert(tk.END, f"Most Accessed Endpoint: {most_accessed[0]}, Access Count: {most_accessed[1]}\n")
        result_text_areas[3].insert(tk.END, "IP Address, Failed Login Count\n")
        for ip, count in failed_logins.items():
            result_text_areas[3].insert(tk.END, f"{ip}, {count}\n")
        save_to_csv(ip_counts, endpoint_counts, failed_logins)
        messagebox.showinfo("Success", "Analysis complete and saved to log_analysis_output.csv")
        notebook.select(results_tab)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Log Analyzer")
app.geometry("400x600")
app.configure(bg="#f0f0f0")
notebook = ttk.Notebook(app)
notebook.pack(fill='both', expand=True)
upload_tab = ttk.Frame(notebook)
results_tab = ttk.Frame(notebook)
notebook.add(upload_tab, text="Upload Log File")
notebook.add(results_tab, text="Analysis Results")
title_label = tk.Label(upload_tab, text="Log Analyzer", font=("Arial", 24, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)
analyze_button = tk.Button(upload_tab, text="Analyze Log File", command=analyze_log_file, bg="#4CAF50", fg="white", font=("Arial", 14))
analyze_button.pack(pady=10)
canvas = tk.Canvas(results_tab, bg="#f0f0f0")
scrollbar = ttk.Scrollbar(results_tab, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")  # Use tk.Frame instead of ttk.Frame
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text_areas = []
for title in ["IP Address, Request Count", "Endpoint, Access Count", "Most Accessed Endpoint", "IP Address, Failed Login Count"]:
    frame = ttk.Frame(scrollable_frame)
    frame.pack(pady=10, padx=10, fill='both', expand=True)

    label = tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="#f0f0f0")
    label.pack(anchor='w')
    text_frame = ttk.Frame(frame)
    text_frame.pack(fill='both', expand=True)
    text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=70, height=10, bg="#ffffff", font=("Arial", 10))
    text_area.pack(side=tk.LEFT, fill='both', expand=True)
    scrollbar = ttk.Scrollbar(text_frame, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    text_area['yscrollcommand'] = scrollbar.set
    result_text_areas.append(text_area)

app.mainloop()