###importando as bibliotecas
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from datetime import datetime
now = datetime.now()
datahj = now.strftime("%d/%m/%Y")

def main():
    print("Inicializando o Script!")
    names = pd.read_csv('SeresInstrutores.csv')
    for i, row in names.iterrows():

        print('Imagem ' + str(i))
##As colunas do arquivo *.csv
        name = str(row['nome'])
        nome_evento = str(row['evento'])
        #trabalho = str(row['trabalho'])
        horas_palestra = str(row['horas'])
        data = str(row['data'])


        name = name.title()

        frases = [
            'Certificamos que: {} '.format(name),
            'participou do evento de extensão: {},'.format(nome_evento),
            'no IFCE campus Maracanaú.' 
            'Como membro da comissão organizadora',
            #'{}'.format(trabalho),
            #'Em parceria com a Secretaria de Assistência Social e Cidadania de Maracanaú.'#.format(nome_evento),
            'com carga horária de {} hora(s), no(s) dia(s) {}'.format(horas_palestra, data),
            'Maracanaú,'+format(datahj)+'.'

        ]
#setando os parâmetros para trabalharmos com a imagem
        empty_img = Image.open("template.jpg")
        font_size = 40
        font = ImageFont.truetype(r"calibri.ttf", 80)
        W, H = empty_img.size

        posicoes = []
        tamanhos = []
        counterline = 0
#laço para posicionar o texto
        for i in frases:
            tamanhos.append(font.getsize(i))

        for i in range(len(frases)):
            posicoes.append([(W / 2) - (tamanhos[i][0] / 4), ((H - tamanhos[i][1]) / 2) + counterline])
            #posicoes.append([((((W - tamanhos[i][0]) / 2)/5) + 200), ((H - tamanhos[i][1]) / 2)+ counterline])
            counterline += 60


        font = ImageFont.truetype(r"calibri.ttf", font_size)
        image_editable = ImageDraw.Draw(empty_img)


        for i in range(len(frases)):
            image_editable.multiline_text((posicoes[i][0], posicoes[i][1]), frases[i], (35, 57, 75), align='center',font=font)

#por fim o arquivo editado com o texto
        empty_img.save("gerados\{}.jpg".format(name.replace(" ", "_")))
        if i % 50 == 0:
            print('quantidade de linhas processadas {} Rows'.format(i))

    print("gerando certificados....")


main()