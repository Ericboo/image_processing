from PIL import Image
import math as Math

def padding_zero(imagem, maskSize):
    neighbors = Math.floor(maskSize / 2)
    img_alterada = Image.new("RGB", (imagem.width + neighbors * 2, imagem.height + neighbors * 2))
    for x in range(neighbors, imagem.width + neighbors):
        for y in range(neighbors, imagem.height + neighbors):
            img_alterada.putpixel((x, y), value= imagem.getpixel((x - neighbors, y - neighbors)))
    return img_alterada 


def border_replication(imagem, maskSize):
    neighbors = Math.floor(maskSize / 2)
    img_alterada = Image.new("RGB", (imagem.width + (neighbors * 2), imagem.height + (neighbors * 2)))
    for x in range(img_alterada.width):
        for y in range(img_alterada.height):
            if (x >= imagem.width + neighbors or y >= imagem.height + neighbors):
                xp = imagem.width if x >= imagem.width + neighbors else x
                yp = imagem.height if y >= imagem.height + neighbors else y
                img_alterada.putpixel((x, y), value= imagem.getpixel((xp - neighbors, yp - neighbors)))
            elif (x < neighbors or y < neighbors):
                xp = 0 if x <= neighbors else x - neighbors
                yp = 0 if y <= neighbors else y - neighbors
                img_alterada.putpixel((x, y), value= imagem.getpixel((xp, yp)))
            else:
                img_alterada.putpixel((x, y), value= imagem.getpixel((x - neighbors, y - neighbors)))
    return img_alterada 



def average_smoothing(img_alterada, maskSize):
    neighbors = Math.floor(maskSize/2)
    #Prepara a criação de uma imagem de saída.
    for x in range(neighbors, img_alterada.width - neighbors):
        for y in range(neighbors, img_alterada.height - neighbors):
            rsum = 0
            gsum = 0
            bsum = 0
            for i in range(-neighbors, neighbors + 1):
                for j in range(-neighbors, neighbors + 1):
                    rsum += img_alterada.getpixel((x + i, y + j))[0]
                    gsum += img_alterada.getpixel((x + i, y + j))[1]
                    bsum += img_alterada.getpixel((x + i, y + j))[2]
            rmed = int(rsum / maskSize**2)
            gmed = int(gsum / maskSize**2)
            bmed = int(bsum / maskSize**2)
            img_alterada.putpixel(
                (x, y), value=(rmed, gmed, bmed)
            )
    return img_alterada


exemplos = []
img_alteradas = []

#Abre a imagem.
exemplos.append(padding_zero(Image.open("exemplo1.jpg"), maskSize=3)) 
img_alteradas.append(average_smoothing(exemplos[0], maskSize= 3))

exemplos.append(border_replication(Image.open("exemplo2.jpg"), maskSize=5)) 
img_alteradas.append(average_smoothing(exemplos[1], maskSize= 5))

#Monta uma imagem de resultado
for x in range(0, len(exemplos)):
    resultado = img_alteradas[x]
    resultado.save("result{}.jpg".format(x + 1))
    resultado.show()