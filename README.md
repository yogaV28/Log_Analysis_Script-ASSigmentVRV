# Log Analysis Script

## Overview

The Log Analysis Script is a Python tool designed to analyze web server log files. It extracts and analyzes key information such as request counts per IP address, the most frequently accessed endpoints, and potential suspicious activity based on failed login attempts. This script is particularly useful for cybersecurity professionals and web administrators.

## Features

- **Count Requests per IP Address**: Parses the log file to count the number of requests made by each IP address and displays the results in descending order.
- **Identify the Most Frequently Accessed Endpoint**: Extracts endpoints from the log file and identifies the one accessed the most.
- **Detect Suspicious Activity**: Flags IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).
- **Output Results**: Displays results in a clear format in the terminal and saves them to a CSV file named `log_analysis_results.csv`.

## Requirements

- Python 3.x
- No external libraries are required.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/log-analysis-script.git
   cd log-analysis-script
   ```
2. **Prepare the Log File**: Save your log entries in a file named sample.log in the same directory as the script.

## Usage

Run the script using Python:
```bash
python main.py
```
## Sample Log File

You can use the following sample log entries for testing. Save it as sample.log:
```bash
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:45 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /profile HTTP/1.1" 200 768
192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:49 +0000] "POST /feedback HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.1 - - [03/Dec/2024:10:12:51 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:52 +0000] "GET /about HTTP/1.1" 200 256
203.0.113.5 - - [03/Dec/2024:10:12:53 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:55 +0000] "GET /contact HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:56 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.100 - - [03/Dec/2024:10:12:57 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:58 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:59 +0000] "GET /dashboard HTTP/1.1" 200 1024
192.168.1.1 - - [03/Dec/2024:10:13:00 +0000] "GET /about HTTP/1.1" 200 256
198.51.100.23 - - [03/Dec/2024:10:13:01 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:13:02 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:13:03 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:13:04 +0000] "GET /profile HTTP/1.1" 200 768
198.51.100.23 - - [03/Dec/2024:10:13:05 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:13:06 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:13:07 +0000] "POST /feedback HTTP/1.1" 200 128
```
## Output
### Terminal Output
The script will print the following information to the terminal:
```bash
IP Address, Request Count
192.168.1.1, 7
203.0.113.5, 8
10.0.0.2, 6
198.51.100.23, 8
192.168.1.100, 5

Most Accessed Endpoint, Access Count
/login, 13

IP Address, Failed Login Count
203.0.113.5, 8
192.168.1.100, 5
```
CSV Output
The results will be saved in log_analysis_results.csv with the following structure:

**Requests per IP**: Columns: IP Address, Request Count
**Most Accessed Endpoint**: Columns: Endpoint, Access Count
**Suspicious Activity**: Columns: IP Address, Failed Login Count

## UI
### Thinker UI
To enhance user experience, the project includes a user-friendly Thinker UI. This interface allows users to interact with the log analysis features seamlessly. Key functionalities of the Thinker UI include:

**Upload Log Files**: Easily upload your web server log files for analysis.
**View Results**: Display analysis results in a visually appealing format, making it easier to interpret data.
**Filter Options**: Apply filters to focus on specific IP addresses or endpoints.
**Export Data**: Download the analysis results in CSV format directly from the UI.

## Getting Started with Thinker UI
Installation: Ensure you have the required dependencies installed. You can do this by running:
```bash
pip install -r requirements.txt
```
Run the Application: Start the Thinker UI by executing:
```bash
python app.py
```
**Upload Your Log File**: Use the upload button in the UI to select your log file.

**Analyze**: Click on the "Analyze" button to process the log file and view the results.

**Export**: If you wish to save the results, use the "Export" button to download the data in CSV format.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
