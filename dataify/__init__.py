# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Helper module providing common Datasets for PyTorch.
"""

# Imports
from .info import __version__
from .brats import BraTSDataset
from .dsprites import DSpritesDataset
from .echocardiography import EchocardiographyDataset
from .hcp import HCPAnatDataset
from .impac import IMPACDataset
from .kang import SingleCellRNASeqDataset
from .moving_mnist import MovingMNISTDataset
