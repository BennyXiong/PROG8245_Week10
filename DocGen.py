import os
from sklearn.datasets import fetch_20newsgroups
 
# Set the number of documents to save
num_docs = 20  # You can change this number
 
# Load the dataset (text only, no headers/footers/quotes)
newsgroups_data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
 
# Create output directory (optional)
output_dir = "sample_docs"
os.makedirs(output_dir, exist_ok=True)
 
# Write the first `num_docs` documents into separate .txt files
for i in range(min(num_docs, len(newsgroups_data.data))):
    doc_text = newsgroups_data.data[i]
    file_path = os.path.join(output_dir, f"doc{i+1}.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(doc_text)
    print(f"Saved {file_path}")