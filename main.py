import os
from src.pdf_converter import pdf_to_images
from src.ocr_engine import extract_text_from_images
from src.text_cleaner import clean_text
from src.file_manager import save_text


def process_file(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"\n📘 Processing: {base_name}")

    # If it's a PDF
    if file_path.lower().endswith(".pdf"):
        image_paths = pdf_to_images(file_path)
    else:
        image_paths = [file_path]  # single image input

    # OCR Extraction
    raw_text = extract_text_from_images(image_paths)

    # Clean Text
    cleaned_output = clean_text(raw_text)

    # Save Output
    output_file = save_text("output", base_name, cleaned_output)
    print(f"✅ Saved OCR text to: {output_file}")


def main():
    input_dir = "input"
    os.makedirs("output", exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)

    files = [os.path.join(input_dir, f)
             for f in os.listdir(input_dir)
             if f.lower().endswith((".pdf", ".png", ".jpg", ".jpeg"))]

    if not files:
        print("⚠️ No input files found in /input/. Add your lecture PDFs or images.")
    else:
        for file in files:
            process_file(file)

    print("\n🎉 All files processed successfully!")


if __name__ == "__main__":
    main()
