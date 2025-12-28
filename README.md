# Microsoft Email Availability Checker

⚠️ **Educational / research purposes only**

A Python tool that checks whether Microsoft email addresses  
(`@hotmail.com`, `@outlook.com`) are **AVAILABLE** or **TAKEN**  
using real browser automation.

The script uses **Playwright (Chromium)** and behaves like a real user,
with optional proxy support.

---

## ✨ Features

- ✅ Checks Hotmail / Outlook email availability
- ✅ Real browser automation (Chromium, non-headless)
- ✅ Manual input **or** CSV file input
- ✅ Proxy support (HTTP / authenticated)
- ✅ IP check page opens in a secondary tab
- ✅ Timestamped CSV results
- ✅ Multiple runs without restarting the script
- ✅ Works on multiple PCs via `git clone`

---

## 🖥️ Supported Systems

- Linux (Ubuntu / Debian / Linux Mint)
- Python **3.10+**

> ⚠️ Windows and macOS are not officially tested.

---

## 📦 Project Structure

```

ms-email-checker/
├── ms_check.py      # Main script
├── install.sh      # One-command installer
├── README.md       # Documentation

```
---

## 🚀 Installation (New PC / Fresh System)
1️⃣ **Clone the repository**

```
git clone https://github.com/amyspace01/ms-email-checker.git
cd ms-email-checker
```
---

2️⃣ **Run the installer**
```
chmod +x install.sh
./install.sh
```
The installer will:

- Install system dependencies

- Create a Python virtual environment

- Install Python packages

- Install Playwright Chromium browser

---
▶️ **Running the Script**

Activate the virtual environment:
```
source mscheck/bin/activate
```

Run the script:
```
python ms_check.py
```
---

🔧 **What Happens When You Run It**

You will be prompted to:

1. Choose proxy or no proxy

2. Enter proxy details (if selected)

3. Choose input method:

    - Manual input

    - CSV file

4. The script opens:

    - An IP check page in a secondary browser tab

    - Microsoft signup page in the main tab

5. Email availability is checked

6. Results are saved automatically

7. You can choose to run again without restarting

---

✍️ **Manual Input Method**

When prompted, paste emails one per line:
```
email
testuser1@outlook.com
testuser2@hotmail.com
```

Press ENTER twice to start checking.

---

📄 **CSV Input Method**

If using a CSV file, it must contain a column named email:
```
email
testuser1@outlook.com
testuser2@hotmail.com
```

When prompted, enter the full path to the CSV file.

---

📊 **Output (Results)**

Results are saved automatically as timestamped CSV files:
```
results-YYYY-MM-DD_HH-MM-SS.csv
```

Example output:
```
email,status
testuser1@outlook.com,TAKEN
newname123@hotmail.com,AVAILABLE
```
---
