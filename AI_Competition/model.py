from transformers import BertModel, AdamW

def create_model(pretrained_model_name):
    return BertModel.from_pretrained(pretrained_model_name)

def create_optimizer(model, learning_rate):
    return AdamW(model.parameters(), lr=learning_rate)
