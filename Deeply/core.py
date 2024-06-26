# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['CustomImageDataset']

# %% ../00_core.ipynb 3
import torch
import torchvision
from torchvision.datasets import DatasetFolder
from torchvision.io import read_image, ImageReadMode

# %% ../00_core.ipynb 4
class CustomImageDataset(DatasetFolder):
    """Subclasses DatasetFolder for custom dataset organised by labels as subfolder names.
        https://pytorch.org/vision/stable/generated/torchvision.datasets.DatasetFolder.html
    """
    def __init__(self, image_dir,
                 loader=torchvision.io.read_image, extensions=('png','jpg','jpeg'),
                 transform=None, target_transform=None):
        self.root = image_dir
        self.loader = loader
        self.extensions = extensions
        self.transform = transform
        self.target_transform = target_transform
        self.labels, self.mapping = super().find_classes(self.root)
        print(f'{len(self.labels)} classes found.')
        self.dataset = super().make_dataset(self.root, self.mapping, extensions=self.extensions)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image, label = self.dataset[idx]
        print(image, label)
        image = self.loader(image)
        if self.transform:            
            image = self.transform(image)
            print('transformed')
        if self.target_transform:
            label = self.target_transform(label)
            print('target transformed')
        return image, label
