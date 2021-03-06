from __future__ import absolute_import


from . import distances
from . import metrics
from . import utils

from .GANs.GAN import GAN #main class
from .GANs.AAE import AAE
from .GANs.CGAN import CGAN
from .GANs.DiscoGAN import DiscoGAN
from .GANs.Pix2Pix import Pix2Pix

__version__ = '0.0.6'
