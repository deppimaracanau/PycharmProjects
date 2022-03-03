import os
from os import listdir
from os.path import isfile, join
from fpdf import FPDF
from PIL import Image

caminho = "/home/c1c3ru/PycharmProjects/pdf/" # caminho para o diretório

for each_file in listdir(caminho):
    if isfile(join(caminho,each_file)):
        if each_file.endswith(".jpg"):
            print(each_file)
            imagem = os.path.join(caminho,each_file)
            pdf_path =  os.path.join(caminho,each_file.rsplit('.', 1)[0]+'.pdf')
            img = Image.open(imagem)
            img.save(pdf_path)
