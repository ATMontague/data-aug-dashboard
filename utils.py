import torch
from torchvision.datasets import MNIST, CIFAR10
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


@st.cache_data  # for performance purposes
def load_model():
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model = model.to(device)
    model = model.eval()
    return model


def get_prediction():
    raise NotImplementedError


def load_image(img_path):
    raise NotImplementedError


def preprocess():
    raise NotImplementedError


def apply_augmentation(img, method='hflip'):
    # need to specify aug method
    # todo: figure out how to also include other params for given method. crap

    transform = A.Compose([
        A.HorizontalFlip(p=1.0)
    ])
    transformed = transform(image=img)
    img = transformed['image']
    return img


# @st.cache_data
def get_random_mnist_image(idx=10):
    mnist = MNIST(root='../data', download=True, train=True)
    img, cl = mnist[idx]
    img = np.array(img)

    return img


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



if __name__ == '__main__':

    img = get_random_mnist_image()
    img = cv2.resize(img, (256, 256))
    cv2.imshow('input', img)

    aug = apply_augmentation(img)
    print(aug.shape)

    cv2.imshow('aug', aug)
    cv2.waitKey(0)