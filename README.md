# QR Code Generator 📱

A modern, cross-platform desktop application built with **Python** and **CustomTkinter**. This tool allows users to generate, customize, and save QR codes effortlessly with a sleek, dark-mode-ready interface.

## ✨ Features
- **Modern UI:** Clean interface built with CustomTkinter.
- **Customizable:** Adjust QR code data and window dimensions.
- **Theme Support:** Fully compatible with Light and Dark modes.
- **Cross-Platform:** Runs smoothly on both **macOS** and **Windows**.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/KostasSot/qrcodegenerator.git](https://github.com/KostasSot/qrcodegenerator.git)
cd qrcodegenerator
```

### 3. Virtual Environment (Recommended)
It is best practice to run this app inside a virtual environment to keep dependencies clean.

**Create the environment:**
```bash
python3 -m venv venv
```

**Enter (Activate) the environment:**
* **Windows:**
    ```powershell
    venv\Scripts\activate
    ```
* **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
*(You should see `(venv)` appear at the start of your terminal line).*

### 4. Install Dependencies
Once the environment is active, install the required libraries:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 🖥️ Windows
```powershell
python main.py
```

### 🍎 macOS / Linux
```bash
python3 main.py
```

---

## 🚪 Exiting the Environment
When you are finished using the application, you can exit the virtual environment by running:
```bash
deactivate
```

---

## ⚠️ Troubleshooting: Window Not Updating?

If you are a developer making changes to the code (e.g., changing window size or colors) and the app keeps launching with old settings, you likely have a **Zombie Process** or **Cache** issue.

### 1. Force Close Stuck Processes
The application might still be running in the background even if the window is closed.
* **Windows:** Open Task Manager (`Ctrl+Shift+Esc`), find `python.exe`, and select **End Task**.
* **macOS:** Open Activity Monitor, search for `Python`, and select **Force Quit**.

### 2. Clean Cache & Run (The "Hard" Restart)
Use these commands to delete temporary compiled files and force a fresh launch.

**For Windows:**
```powershell
del /S *.pyc && python main.py
```

**For macOS:**
```bash
find . -name "*.pyc" -delete && python3 main.py
```
