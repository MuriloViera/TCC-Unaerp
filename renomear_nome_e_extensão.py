# -*- coding: utf-8 -*-
"""Renomear Nome e Extensão.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qVtHvRjjbyUDiTdYcuQm7EdI8JYXeIgt

Bibliotecas
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sympy import *
import csv
import re
import math
!pip install Pillow
import PIL
from PIL import Image

"""Mudar a imagem para 120x120"""

#Adicionar a imagem a uma 120 branca
diretorio = "/content/drive/Othercomputers/Meu computador/Data_set_Frutas_2/dados/plum"

i = 1

# Modifica nome
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
      imgteste = Image.open('/content/drive/Othercomputers/Meu computador/Data_set_Frutas_2/dados/plum/Plum_' + str(i) + '.jpg')
      imgteste2 = Image.open('/content/branco.jpg')
      imgteste2.paste(imgteste, (10,10))
      imgteste2.save('/content/drive/Othercomputers/Meu computador/Data_set_Frutas_2/dados/plum2/Plum_' + str(i) + '.jpg')
      i = i + 1

"""Mudar nome e extensão"""

import string
import os

diretorio = "/content/drive/Othercomputers/Meu computador/Data_set_Frutas_2/dados/plum"
i = 1

# Modifica nome
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        parteQueSai = arquivo
        parteQueSubstitui = "Plum_" + str(i) + ".jpg"
        novoNome = str.replace(arquivo, parteQueSai, parteQueSubstitui)
        fullpathOld = os.path.join(diretorio,arquivo)
        fullpathNew = os.path.join(diretorio,novoNome)
        os.rename(fullpathOld, fullpathNew)
        i = i + 1
        print(i)