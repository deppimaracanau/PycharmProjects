from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import pandas as pd

now = datetime.now()
data = str(format(now))
print(data)
def main():
    print("Inicializando o Script!")
    names = pd.read_csv('lista.csv')
    for i,row in names.iterrows():
        name = str(row['FName']) + ' ' + str(row['LName'])
        name = name.title()
        name2 = 'certifico que ' + name
        empty_img = Image.open("template.jpg")
        font_size = 18
        font = ImageFont.truetype(r"calibri.ttf", 18)
        W,H = empty_img.size
        w, h = font.getsize(name)
        width = ((W-w)/2)
        height = ((H-h)/2)-50
        if W%w >= 2:
            font_size = 50
            width = ((W-w)/2) +75
            height = ((H-h)/2)-10

        font = ImageFont.truetype(r"calibri.ttf", font_size)
        image_editable = ImageDraw.Draw(empty_img)
        image_editable.multiline_text((width -200,height -50 ), name, (35, 57, 75), font=font)
        image_editable.multiline_text((width -500, height + 20), 'participou do(a) atividade do evento de', (35, 57, 75), font=font)
        image_editable.multiline_text((width -500, height + 60), 'Extensão: do Instituto Federal de Educação, Ciência e Tecnologia do Ceará,', (35, 57, 75), font=font)
        image_editable.multiline_text((width -500, height + 100), 'com carga horária de 80 horas, no(s) dia(s) ().', (35, 57, 75), font=font)
        image_editable.multiline_text((width +350, height + 300), 'Maracanaú,'+data, (35, 57, 75), font=font)

        empty_img.save("{}.jpg".format(name.replace(" ", "_")))
        if i % 50 == 0:
            print('quantidade de linhas processadas {} Rows'.format(i))

    print("gerando certificados....")


if __name__ == "__main__":
    main()