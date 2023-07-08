import torch.nn as nn

def get_loss_fn():
    loss_fn = nn.BCEWithLogitsLoss()
    return loss_fn
