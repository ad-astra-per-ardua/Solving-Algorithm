import torch
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from transformers import BertTokenizer
from preprocess import main as prepare_dataset
from data_loader import PatentDataset, create_data_loader
from model import create_model, create_optimizer
from loss import get_loss_fn
from train import train, eval_model

if __name__ == "__main__":
    dataset = prepare_dataset()
    texts = [x[0] for x in dataset]
    labels = [x[1].split() for x in dataset]

    mlb = MultiLabelBinarizer()
    labels = mlb.fit_transform(labels)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    patent_dataset = PatentDataset(texts, labels, tokenizer, max_len=128)
    data_loader = create_data_loader(patent_dataset, batch_size=32)
    model = create_model('bert-base-uncased')
    optimizer = create_optimizer(model, learning_rate=1e-5)

    # device
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # loss
    loss_fn = get_loss_fn()
    train_acc, train_loss = train(model, data_loader, loss_fn, optimizer, device)

    # preprocessing
    test_df = pd.read_csv('test_input.csv')
    test_texts = test_df['claims']

    test_patent_dataset = PatentDataset(test_texts, None, tokenizer, max_len=128)
    test_data_loader = create_data_loader(test_patent_dataset, batch_size=32)

    test_predictions = eval_model(model, test_data_loader, loss_fn, device, mlb)

    test_df['SSnos'] = test_predictions
    test_df.to_csv('submission.csv', index=False)

