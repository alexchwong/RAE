from setuptools import setup, find_packages

setup(
  name = 'RAE',
  packages = find_packages(exclude=[]),
  version = '0.1',
  license='MIT',
  description = 'An installable version of RAE',
  author = 'Alex Wong',
  install_requires=[
    'torch-fidelity', 'torchdiffeq', 'torchmetrics', 'torch>=2.0',
    'timm>=0.9.16', 'transformers>=4.56.2', 'einops',
    'omegaconf>=2.3.0'
  ],
)
