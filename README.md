📝 OCR for Lecture Notes

A powerful Python tool that extracts text from scanned lecture notes, PDFs, and images — turning them into **searchable, editable text files**.  
Ideal for students who want to digitize and organize handwritten or printed notes from **Anatomy, Nursing, or Science courses**.


## 📂 Project Structure

ocr_notes/
│
├── ocr_notes.py           # Main OCR script
├── requirements.txt       # Python dependencies
├── /input/                # Folder for scanned PDFs or images
│   ├── lecture1.jpg
│   ├── lecture2.png
│   └── notes.pdf
├── /output/               # Extracted text files saved here
│   ├── lecture1.txt
│   ├── lecture2.txt
│   └── notes.txt
└── README.md              # Project documentation

## 🚀 Features

✅ Extract text from **images (JPG, PNG)** and **PDFs**  
✅ Uses **Tesseract OCR** via `pytesseract`  
✅ Automatically outputs readable `.txt` files  
✅ Batch processes multiple files in `/input`  
✅ Simple and beginner-friendly codebase  
✅ Cross-platform (Windows, macOS, Linux)


## 🧰 Requirements

### Python 3.8 or newer

Install the required packages:

pip install -r requirements.txt


Contents of `requirements.txt`:

pytesseract
pdf2image
Pillow


## ⚙️ Setup Instructions

### 1. Install Tesseract OCR Engine

#### 🔹 Windows
Download the installer from:
👉 https://github.com/UB-Mannheim/tesseract/wiki

After installing, note the installation path (e.g. `C:\Program Files\Tesseract-OCR\tesseract.exe`).

#### 🔹 macOS

brew install tesseract

#### 🔹 Linux (Debian/Ubuntu)
sudo apt update
sudo apt install tesseract-ocr


### 2. Verify Installation
Run this command:

tesseract --version

If you see version info, it’s installed correctly ✅



## ▶️ How to Use

1. Place all your **lecture images or PDFs** inside the `/input` folder.  
   Example:
   
   /input/
   ├── anatomy_notes.pdf
   ├── lecture1.jpg
   └── lecture2.png
   

2. Run the program:
   python ocr_notes.py
   

3. The program will:
   - Scan all files in `/input`
   - Convert PDFs to images (if needed)
   - Extract text using OCR
   - Save the output as `.txt` files in `/output`

   Example result:
   
   /output/
   ├── anatomy_notes.txt
   ├── lecture1.txt
   └── lecture2.txt
   


## 🧠 How It Works

1. **PDF Handling:**  
   `pdf2image` converts PDFs into a series of images.

2. **Image OCR:**  
   `pytesseract` reads text from each image.

3. **Output:**  
   The recognized text is written into `.txt` files, one per source document.



## 🧩 Example

### Input
File: `lecture1.jpg` (handwritten or printed notes)

### Output
File: `lecture1.txt`

Introduction to Anatomy:
The human body consists of various organ systems...




## 🛠️ Customization

You can modify `ocr_notes.py` to:
- Change OCR language (`lang='eng'`, `'spa'`, `'deu'`, etc.)
- Add PDF merging
- Add progress indicators
- Output as `.docx` or `.pdf` instead of `.txt`



## ❗ Troubleshooting

| Issue | Solution |
|-------|-----------|
| `TesseractNotFoundError` | Make sure Tesseract is installed and added to PATH |
| Text output is gibberish | Try higher-quality scans or adjust image contrast |
| Blank output file | Check if the PDF or image actually contains text (some are just scanned backgrounds) |
| Slow processing | Reduce image resolution or process fewer pages at once |



## 🤝 Contributing

Feel free to improve the OCR pipeline or add support for:
- Multi-language OCR  
- Automatic note categorization  
- Integration with Notion or Obsidian  

Pull requests welcome!



## 📜 License

This project is open-source under the **MIT License**.  
You may use, modify, and distribute it freely for personal or educational use.



### ⭐ If this project helps you digitize your notes...
Consider giving it a ⭐ and sharing it with classmates who take lots of handwritten notes!
