# -*- coding: UTF-8 -*-

import argparse
import numpy as np
import torch
import gym
from policy_gradient import PolicyGradient
from config import get_config
import random

import pdb

parser = argparse.ArgumentParser()
parser.add_argument(
    "--env-name", required=True, type=str, choices=["cartpole", "pendulum", "cheetah"]
)
parser.add_argument("--baseline", dest="use_baseline", action="store_true")
parser.add_argument("--no-baseline", dest="use_baseline", action="store_false")
parser.add_argument("--seed", type=int, default=1)

parser.set_defaults(use_baseline=True)

if __name__ == "__main__":
    # args = parser.parse_args()
    # torch.random.manual_seed(args.seed)
    # np.random.seed(args.seed)
    # random.seed(args.seed)

    seed = 5
    torch.random.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    env = "cartpole"  # cartpole, pendulum, cheetah
    use_baseline = False

    # config = get_config(args.env_name, args.use_baseline, args.seed)
    config = get_config(env, use_baseline, seed)
    env = gym.make(config.env_name)
    # train model
    model = PolicyGradient(env, config, seed)
    model.run()
