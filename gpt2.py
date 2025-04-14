# lets start
# need to setup environment again for this foler 
# need to reinstall stuff for this, put all the projects in this itself for avoiding repetition

from dataclasses import dataclass
import torch
import torch.nn as nn
from torch.nn import functional as f

###############

@dataclass # wth
class GPTConfig:
    block_size: int = 256
    vocab_size: int = 65
    n_layer: int = 6
    n_head: int = 6
    n_embd: int = 384

class GPT(nn.Module):

    def __init__(self,config):
        super.__init__()
        self.config = config
        self.transformer = nn.ModuleDict(
            dict(
                wte = nn.E
            )
        )