# 🔐 Smart Log Analyzer \& Threat Detection System



![Python](https://img.shields.io/badge/Python-3.x-blue)

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)

![Status](https://img.shields.io/badge/Project-Active-brightgreen)



---



## 📌 Overview

A Python-based cybersecurity tool that analyzes system logs to detect suspicious activities such as brute force attacks and blacklisted IP access.



---



## 🚀 Features

- Detects brute force login attempts  

- Identifies blacklisted IP addresses  

- Generates automated security reports  



---



## 🛠️ Tech Stack

- Python  

- Regex  

- File Handling  



---



## 📂 Project Structure



smart-log-analyzer/

│── analyzer.py

│── logs.txt

│── blacklist.txt

│── report.txt

│── screenshots/

│── README.md

│── requirements.txt





---



## ▶️ How to Run

```bash

git clone https://github.com/ankitvishwakarmavishwas/smart-log-analyzer.git

cd smart-log-analyzer

pip install -r requirements.txt

python analyzer.py

```


## 📊 Output

Analysis Complete. Check report.txt


⚠️ Brute Force Detected from IP: 192.168.1.10

🚫 Blacklisted IP Access: 10.0.0.5


---



## 🏗️ Architecture
The system follows a simple detection pipeline:

1. Log Ingestion → Reads raw logs from file  
2. Parsing Engine → Extracts IP and status using regex  
3. Detection Engine → Applies rules:
   - Brute force detection (≥3 failed attempts)
   - Blacklist matching  
4. Alert Generation → Writes alerts to report.txt



---


## 🧠 Detection Logic

- ## Brute Force Detection:
  Tracks failed login attempts per IP using a dictionary counter.
  Flags IPs exceeding threshold (≥3 attempts)

- ## Blacklist Detection:
  Matches incoming IPs against predefined malicious IP list



---


## 📄 Sample Log Format

2026-05-01 LOGIN FAILED user=admin ip=192.168.1.10

## Fields:
- Timestamp
- Status (FAILED/SUCCESS)
- Username
- IP Address


---



## 🌍 Real-World Use Case



Simulates SOC (Security Operations Center) log monitoring to detect brute force attacks and suspicious IP behavior.



---



## 📌 Author



Ankit Vishwakarma

https://github.com/ankitvishwakarmavishwas

https://www.linkedin.com/in/ankitvishwakarmavishwas/



