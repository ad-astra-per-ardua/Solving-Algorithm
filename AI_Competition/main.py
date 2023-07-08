import torch
from sklearn.preprocessing import MultiLabelBinarizer
from transformers import BertTokenizer
from preprocess import main as prepare_dataset
from data_loader import PatentDataset, create_data_loader
from model import create_model, create_optimizer
from loss import get_loss_fn
from train import train, eval_model

if __name__ == "__main__":
    # 데이터셋 로딩
    dataset = prepare_dataset()
    texts = [x[0] for x in dataset]
    labels = [x[1].split() for x in dataset]

    # 토크나이저, 모델, 데이터셋, 데이터 로더 초기화
    mlb = MultiLabelBinarizer()
    labels = mlb.fit_transform(labels)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    patent_dataset = PatentDataset(texts, labels, tokenizer, max_len=128)
    data_loader = create_data_loader(patent_dataset, batch_size=32)
    model = create_model('bert-base-uncased')
    optimizer = create_optimizer(model, learning_rate=1e-5)

    # device 설정
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # 손실함수 초기화 및 학습
    loss_fn = get_loss_fn()
    train_acc, train_loss = train(model, data_loader, loss_fn, optimizer, device)
