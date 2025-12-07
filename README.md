# QR Code Generator 📱

A modern, cross-platform desktop application built with **Python** and **CustomTkinter**. This tool allows users to generate, customize, and save QR codes effortlessly with a sleek, dark-mode-ready interface.

## ✨ Features
- **Modern UI:** Clean interface built with CustomTkinter.
- **Customizable:** Adjust QR code data and window dimensions.
- **Theme Support:** Fully compatible with Light and Dark modes.
- **Cross-Platform:** Runs smoothly on both **macOS** and **Windows**.

---

## 🛠️ Installation

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/KostasSot/qrcodegenerator.git](https://github.com/KostasSot/qrcodegenerator.git)
cd qrcodegenerator
```

### 3. Install Dependencies
Install the required libraries (CustomTkinter, Pillow, etc.) using the requirements file:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 🖥️ Windows
1. Open Command Prompt or PowerShell in the project folder.
2. Run the application:
   ```powershell
   python main.py
   ```

### 🍎 macOS / Linux
1. Open Terminal in the project folder.
2. Run the application:
   ```bash
   python3 main.py
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
