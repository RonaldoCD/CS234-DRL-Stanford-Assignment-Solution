import torch
import gym
from network_utils import build_mlp
import torch as nn
import numpy as np

x = torch.rand(10, 10)
fcn = build_mlp(10, 4, 2, 32)
out = fcn(x)
print(out.shape)
out = torch.squeeze(out)
print(out.shape)
print(out.ndim)

