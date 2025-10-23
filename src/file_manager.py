import os

def save_text(output_dir, filename, text):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{filename}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
