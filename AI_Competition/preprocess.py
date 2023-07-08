import os
import glob
import json

def load_json(directory):
    files = glob.glob(os.path.join(directory, '*.json'))
    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data.append(json.load(f))
    return data

def prepare_dataset(docs_data, labels_data):
    dataset = []
    for doc, label in zip(docs_data, labels_data):
        text = ' '.join([doc['invention_title'], doc['abstract'], doc['claims']])
        target = label['SSno']
        dataset.append((text, target))
    return dataset

def main():
    docs_dir = 'train/docs'
    labels_dir = 'train/labels'

    docs_data = load_json(docs_dir)
    labels_data = load_json(labels_dir)

    dataset = prepare_dataset(docs_data, labels_data)
    return dataset

if __name__ == "__main__":
    main()
