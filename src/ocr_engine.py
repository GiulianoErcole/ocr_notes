import pytesseract
from PIL import Image

def extract_text_from_images(image_paths):
    full_text = ""
    for i, img_path in enumerate(image_paths):
        print(f"🧠 OCR extracting text from page {i+1}...")
        try:
            text = pytesseract.image_to_string(Image.open(img_path))
            full_text += f"\n\n--- Page {i+1} ---\n\n{text}"
        except Exception as e:
            print(f"⚠️ OCR failed for {img_path}: {e}")
    return full_text
