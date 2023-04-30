import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnet18, ResNet18_Weights
import numpy as np
import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import cv2
import albumentations as A
from albumentations.pytorch import ToTensorV2
import streamlit as st
import random
import os


IMG_OPTIONS = ('Great White',
               'Hammerhead',
               'Tiger Shark',
               'Loggerhead Turtle',
               'Leatherback Turtle')

IMG_NAME_MAP = {
    'Great White': ['shark0'],
    'Hammerhead': ['shark1'],
    'Tiger Shark': ['shark2', 'shark3'],
    'Loggerhead Turtle': ['turtle0', 'turtle2'],
    'Leatherback Turtle': ['turtle1', 'turtle3'],
}

IMG_SIZE = (224, 224)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class Augmentation(object):

    def __init__(self, img):
        self.img = img
        self.transform = None

    def _apply_transform(self):
        aug = self.transform(image=self.img)['image']
        return aug

    def rotate(self, degrees):
        # expected value is [-360, 360]
        # rotation happens around the center of an image
        self.transform = A.Affine(rotate=degrees, p=1)
        return self._apply_transform()

    def crop(self):
        self.transform = A.RandomCrop(height=224, width=224)
        return self._apply_transform()

    def shear(self):
        raise NotImplementedError

    def pixel_drop_out(self):
        raise NotImplementedError


# @st.cache_data  # for performance purposes
def load_model(which='baseline'):

    model = resnet18(weights=None)
    model.fc = nn.Linear(512, 2)

    checkpoint_path = os.path.join('models', which, 'best.pt')
    state = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(state)
    model = model.to(device)
    return model


def get_prediction(model, img):
    model.eval()

    # softmax = nn.Softmax(dim=0)

    img = preprocess(img)
    img = img.to(device)

    output = model(img)
    _, predicted = torch.max(output.data, 1)
    # print('output: ', output)
    # print('pred: ', predicted)

    # top 2 predictions
    top_2 = torch.topk(output, 2)
    # print('top_2\,', top_2)
    vals = top_2.values.squeeze()
    indices = top_2.indices.squeeze().cpu().detach().numpy()

    # print('indices\n', indices)

    # return values as probabilities & name of class pred
    # probs = softmax(vals)
    probs = F.softmax(output, dim=1)
    probs = probs.cpu().detach().numpy()
    return probs



def load_image(img_path):
    raise NotImplementedError


def preprocess(img, size=224):
    transform = A.Compose([
        A.PadIfNeeded(min_height=size, min_width=size),
        A.RandomCrop(height=size, width=size),
        A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ToTensorV2(),
    ])
    transformed = transform(image=img)
    img = transformed['image']
    img = torch.unsqueeze(img, dim=0)
    return img


def apply_augmentation(img, aug='hflip'):
    res=224
    if aug == 'baseline':
        transform = A.Compose([
            A.PadIfNeeded(min_height=res, min_width=res),
            A.RandomCrop(height=res, width=res),
        ])
    elif aug == 'blur':
        transform = A.Compose([
            A.Blur(blur_limit=[5, 13], p=1.0),
        ])
    elif aug == 'drop':
        transform = A.Compose([
            A.CoarseDropout(max_holes=3, min_holes=1, min_width=10, min_height=10, max_height=50,max_width=50, p=1),
        ])
    elif aug == 'emboss':
        transform = A.Compose([
            A.Emboss(p=1.0),
        ])
    elif aug == 'gray':
        transform = A.Compose([
            A.ToGray(p=1.0),
        ])

    augmented = transform(image=img)['image']
    return augmented


def get_random_cifar_image():
    raise NotImplementedError


# note: idk if need
def get_formatted_imagenet_class_idx(pth):
    # this is from lime tutorial and seems weird
    idx2label = []
    cls2label = {}
    cls2idx = {}

    with open(pth, 'r') as f:
        class_idx = json.load(f)
        idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
        cls2label = {class_idx[str(k)][0]: class_idx[str(k)][1] for k in range(len(class_idx))}
        cls2idx = {class_idx[str(k)][0]: k for k in range(len(class_idx))}
    return idx2label, cls2label, cls2idx

#
#
# if __name__ == '__main__':
#
#     img = get_random_mnist_image()
#     img = cv2.resize(img, (256, 256))
#     cv2.imshow('input', img)
#
#     aug = apply_augmentation(img)
#     print(aug.shape)
#
#     cv2.imshow('aug', aug)
#     cv2.waitKey(0)