from PIL import Image
import math as Math

def padding_zero(imagem, size):
    mask = Math.floor(size / 2)
    img_alterada = Image.new("RGB", (imagem.width + mask * 2, imagem.height + mask * 2))
    for x in range(mask, imagem.width + mask):
        for y in range(mask, imagem.height + mask):
            img_alterada.putpixel((x, y), value= imagem.getpixel((x - mask, y - mask)))
    return img_alterada 

def border_replication(imagem, size):
    mask = Math.floor(size / 2)
    img_alterada = Image.new("RGB", (imagem.width + (mask * 2), imagem.height + (mask * 2)))
    for x in range(img_alterada.width):
        for y in range(img_alterada.height):
            if (x >= imagem.width + mask or y >= imagem.height + mask):
                xp = imagem.width if x >= imagem.width + mask else x
                yp = imagem.height if y >= imagem.height + mask else y
                img_alterada.putpixel((x, y), value= imagem.getpixel((xp - mask, yp - mask)))
            elif (x < mask or y < mask):
                xp = 0 if x <= mask else x - mask
                yp = 0 if y <= mask else y - mask
                img_alterada.putpixel((x, y), value= imagem.getpixel((xp, yp)))
            else:
                img_alterada.putpixel((x, y), value= imagem.getpixel((x - mask, y - mask)))
    return img_alterada 



def average_smoothing(img_alterada, size):
    mask = Math.floor(size/2)
    #Prepara a criação de uma imagem de saída.
    for x in range(mask, img_alterada.width - mask):
        for y in range(mask, img_alterada.height - mask):
            rsum = 0
            gsum = 0
            bsum = 0
            for i in range(-mask, mask + 1):
                for j in range(-mask, mask + 1):
                    rsum += img_alterada.getpixel((x + i, y + j))[0]
                    gsum += img_alterada.getpixel((x + i, y + j))[1]
                    bsum += img_alterada.getpixel((x + i, y + j))[2]
            rmed = int(rsum / size**2)
            gmed = int(gsum / size**2)
            bmed = int(bsum / size**2)
            img_alterada.putpixel(
                (x, y), value=(rmed, gmed, bmed)
            )
    return img_alterada


exemplos = []
img_alteradas = []

#Abre a imagem.
# exemplos.append(padding_zero(Image.open("exemplo1.jpg"), size=5)) 
# img_alteradas.append(average_smoothing(exemplos[0], size= 5))

exemplos.append(border_replication(Image.open("exemplo2.jpg"), size=120)) 
img_alteradas.append(exemplos[0])

#Monta uma imagem de resultado
for x in range(0, len(exemplos)):
    resultado = img_alteradas[x]
    resultado.save("result{}.jpg".format(x))
    resultado.show()