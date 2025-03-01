#!/usr/bin/env python3
from PIL import ImageGrab, ImageOps, ImageFilter, Image
import imagemethodcalc
from random import random
from pathlib import Path


def FEdge(image):
    imageProcessed = image.filter(ImageFilter.FIND_EDGES)
    return imageProcessed


def Inverted(image):
    imageProcessed = ImageOps.invert(image)
    return imageProcessed


def Posterized(image):
    imageProcessed = ImageOps.posterize(image, 2)
    return imageProcessed


def poolMap(image, imageName, currMethod, primePartsnames):
    currMethodName = "".join(i.__name__ for i in currMethod)
    currMethoditer = imageName + "-"
    for f in currMethod:
        nextMethoditer = currMethoditer + f.__name__
        image = f(image)
        currMethoditer = nextMethoditer
    itemInfo = imagemethodcalc.mappedCalc(image, currMethodName, primePartsnames)
    return itemInfo


def processFoo(k, where, primePartsnames):
    image = ImageGrab.grab(bbox=where)
    imageName = str(random())[2:]
    image.save(Path("/home/brandon/Pictures"))
    processes = imageName + "-"
    for f in (FEdge, Inverted, Posterized):
        image = f(image)
        processes = processes + f.__name__
    image.save(Path("/home/brandon/Pictures"))
    itemInfo = imagemethodcalc.mappedCalc(image, primePartsnames)
    return (k, itemInfo)
