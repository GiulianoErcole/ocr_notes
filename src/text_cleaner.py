import re

def clean_text(text):
    print("🧹 Cleaning extracted text...")
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII
    text = re.sub(r'\s+\n', '\n', text)         # clean extra spaces before newlines
    text = re.sub(r'\n{3,}', '\n\n', text)      # collapse multiple blank lines
    text = re.sub(r'([a-z])\n([a-z])', r'\1 \2', text, flags=re.I)  # fix word splits
    return text.strip()
