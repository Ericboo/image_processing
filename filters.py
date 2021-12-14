from PIL import Image
import math as Math

def laplacian(imagem):
    #define o kernel 3x3 da imagem
    kernel = [[], [], []]
    kernel[0] = [0, -1, 0]
    kernel[1] = [-1, 4, -1] 
    kernel[2] = [0, -1, 0]
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = [0, 0, 0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    xp = x + i
                    yp = y + j
                    sum[0] += (imagem.getpixel((xp, yp))[0] * kernel[i + 1][j + 1])
                    sum[1] += (imagem.getpixel((xp, yp))[1] * kernel[i + 1][j + 1])
                    sum[2] += (imagem.getpixel((xp, yp))[2] * kernel[i + 1][j + 1])
            img_alterada.putpixel(
                (x, y), value=(int(sum[0]), int(sum[1]), int(sum[2]))
            )
    return img_alterada


def sharpening(imagem):
    #define o kernel 3x3 da imagem
    kernel = [[], [], []]
    kernel[0] = [0, -1, 0]
    kernel[1] = [-1, 5, -1] 
    kernel[2] = [0, -1, 0]
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = [0, 0, 0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    xp = x + i
                    yp = y + j
                    sum[0] += (imagem.getpixel((xp, yp))[0] * kernel[i + 1][j + 1])
                    sum[1] += (imagem.getpixel((xp, yp))[1] * kernel[i + 1][j + 1])
                    sum[2] += (imagem.getpixel((xp, yp))[2] * kernel[i + 1][j + 1])
            img_alterada.putpixel(
                (x, y), value=(int(sum[0]), int(sum[1]), int(sum[2]))
            )
    return img_alterada


def generate_gauss_kernel(size, sigma):
    kernel = [[], [], []]
    for x in range(size):
        for y in range(size):
            kernel[x].append(( (1/(2 * Math.pi * sigma**2) )* Math.e ** - ((x**2 + y**2) / (2 * sigma ** 2))))
            print(kernel[x][y] * 16)
        print()
    return kernel

def gaussian_smooth(imagem, size, sigma):
    #define o kernel da imagem
    kernel = generate_gauss_kernel(size, sigma)
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    return img_alterada
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = [0, 0, 0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    xp = x + i
                    yp = y + j
                    sum[0] += (imagem.getpixel((xp, yp))[0] * kernel[i + 1][j + 1])
                    sum[1] += (imagem.getpixel((xp, yp))[1] * kernel[i + 1][j + 1])
                    sum[2] += (imagem.getpixel((xp, yp))[2] * kernel[i + 1][j + 1])
            img_alterada.putpixel(
                (x, y), value=(int(sum[0] / 16), int(sum[1] / 16), int(sum[2] / 16))
            )
    return img_alterada
    

exemplos = []
img_alteradas = []

#Abre a imagem.
exemplos.append(Image.open("exemplo1.jpg")) 
img_alteradas.append(laplacian(exemplos[0]))

exemplos.append(Image.open("exemplo2.jpg")) 
img_alteradas.append(sharpening(exemplos[1]))

exemplos.append(Image.open("exemplo3.jpg")) 
img_alteradas.append(gaussian_smooth(exemplos[2], sigma= 1, size= 3))

#Monta uma imagem de resultado
for x in range(0, len(exemplos)):
    resultado = img_alteradas[x]
    resultado.save("result{}.jpg".format(x + 1))
    resultado.show()