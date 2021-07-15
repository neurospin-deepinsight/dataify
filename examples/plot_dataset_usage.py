# -*- coding: utf-8 -*-
"""
Dataset usage
=============

Credit: A Grigis

A simple example on how to use a dataset (more information can be found in the
PyTorch documentation).
"""

from pprint import pprint
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from dataify import get_datasets

#############################################################################
# Available datasets
# ------------------
#
# First list all available datasets.

datasets = get_datasets()
pprint(datasets)

#############################################################################
# Use a dataset
# -------------
#
# Select one dataset of inerest and use it with PyTorch.

dataset = datasets["SinOscillatorDataset"]()
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
batch_data = next(iter(dataloader))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(dataset.time, batch_data.squeeze().T)
ax.set_xlabel("time")
ax.grid(True)
plt.show()
