from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, temp_dir="temp_pages"):
    os.makedirs(temp_dir, exist_ok=True)
    print(f"🔄 Converting {pdf_path} to images...")
    pages = convert_from_path(pdf_path, dpi=300)
    image_paths = []

    for i, page in enumerate(pages):
        img_name = os.path.join(temp_dir, f"page_{i+1}.png")
        page.save(img_name, "PNG")
        image_paths.append(img_name)
        print(f"🖼️  Saved: {img_name}")

    return image_paths
