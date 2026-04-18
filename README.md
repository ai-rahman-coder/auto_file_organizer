# Auto File Organizer

A simple Python tool to automatically organize files into folders based on file type.

---

## 🚀 What it does

- Scans a folder (like Downloads)
- Moves files into categories such as:
  - Documents
  - Images
  - Excel
  - Videos
- Automatically creates folders if they don’t exist
- Handles duplicate filenames safely
- Supports **dry-run mode** (preview before actual move)

---

## ⚙️ Setup

1. Clone the repository:

git clone <your-repo-link>
cd auto-file-organizer


2. Ensure Python is installed:
python --version


---

## ⚠️ Important Configuration (READ CAREFULLY)

Open `config.json`:
{
"base_path": "Downloads",
"categories": {
"Excel": [".xlsx", ".xls"],
"Presentations": [".pptx", ".ppt"],
"Documents": [".pdf", ".docx", ".txt"],
"Images": [".jpg", ".png"],
"Videos": [".mp4", ".mkv"]
}
}


### ⚠️ Be careful with `base_path`

- This is the folder that will be organized
- It is relative to your system’s home directory

#### Examples:
- `"Downloads"` → organizes your Downloads folder  
- `"Desktop/TestFolder"` → organizes a test folder  

👉 **Always test with a sample folder before using real data**

---

## ▶️ How to Run

### 1. Dry Run (Safe Mode - Recommended)
python organizer.py

- Shows what will happen  
- Does NOT move files  

---

### 2. Actual Run (Moves Files)
python organizer.py --run

- Files will be moved permanently  

---

## 📁 Example Output
[DRY RUN] report.pdf → Documents/report.pdf
[DRY RUN] image.png → Images/image.png


---

## 📌 Features

- Config-driven (no code changes needed)
- Cross-platform (Windows, Mac, Linux)
- Duplicate file handling
- "Others" folder for unmatched files
- CLI-based execution

---

## ⚠️ Disclaimer

- This tool **moves files (not copies)**
- Always run dry-run first
- Double-check your `base_path` before running

---

## 🧠 Future Improvements

- Organize by date (year/month folders)
- Add GUI (Tkinter / Streamlit)
- Auto-run using scheduler
- Content-based classification (AI/NLP)

---

## ✅ Author

Built for learning and personal productivity automation.