from PIL import Image, ImageFont
import math as Math

def showImage(img, contadorExemplos):
    #Monta uma imagem de resultado
    print("Iniciando demonstração")
    resultado = img
    resultado.save("result{}.jpg".format(contadorExemplos))
    resultado.show()

def laplacian(imagem):
    #define o kernel 3x3 da imagem
    kernel = [[], [], []]
    kernel[0] = [-1, -1, -1]
    kernel[1] = [-1, 8, -1] 
    kernel[2] = [-1, -1, -1]
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
    neighbour = Math.floor(size/2)
    kernel = [[]]
    for x in range(size):
        kernel.append([])
    for x in range(-neighbour, neighbour + 1):
        for y in range(-neighbour, neighbour + 1):
            val = ( (1/(2 * Math.pi * sigma**2) )* Math.e ** - ((x**2 + y**2) / (2 * sigma ** 2)))
            kernel[x + neighbour].append(round(val, 8))
    return kernel

def gaussian_smooth(imagem, size, sigma):
    neighbour = Math.floor(size/2)
    #define o kernel da imagem
    kernel = generate_gauss_kernel(size, sigma)
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    for x in range(neighbour, imagem.width - neighbour):
        for y in range(neighbour, imagem.height - neighbour):
            sum = [0, 0, 0]
            weight = 0
            for i in range(-neighbour, neighbour + 1):
                for j in range(-neighbour, neighbour + 1):
                    weight += kernel[i + neighbour][j + neighbour]
                    xp = x + i
                    yp = y + j
                    sum[0] += (imagem.getpixel((xp, yp))[0] * kernel[i + neighbour][j + neighbour])
                    sum[1] += (imagem.getpixel((xp, yp))[1] * kernel[i + neighbour][j + neighbour])
                    sum[2] += (imagem.getpixel((xp, yp))[2] * kernel[i + neighbour][j + neighbour])
            img_alterada.putpixel(
                (x, y), value=(int(sum[0] / weight), int(sum[1] / weight), int(sum[2] / weight))
            )
    return img_alterada


def unsharp(imagem, k):
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    img_alterada_smooth = gaussian_smooth(imagem, 5, 2)
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            unsharp = [0, 0, 0]
            unsharp[0] = imagem.getpixel((x, y))[0] - k * (img_alterada_smooth.getpixel((x, y))[0])
            unsharp[1] = imagem.getpixel((x, y))[1] - k * (img_alterada_smooth.getpixel((x, y))[1])
            unsharp[2] = imagem.getpixel((x, y))[2] - k * (img_alterada_smooth.getpixel((x, y))[2])
            img_alterada.putpixel(
                (x, y), value=(int(unsharp[0] / k), int(unsharp[1] / k), int(unsharp[2] / k))
            )
    return img_alterada


def high_boost(imagem, a):
    #define o kernel 3x3 da imagem
    kernel = [[], [], []]
    kernel[0] = [  0, -1, 0   ]
    kernel[1] = [-1, a + 4, -1] 
    kernel[2] = [  0, -1, 0   ]
    #Prepara a criação de uma imagem de saída.
    img_alterada = Image.new('RGB', imagem.size)
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = [0, 0, 0]
            weight = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    weight += kernel[i + 1][j + 1]
                    xp = x + i
                    yp = y + j
                    sum[0] += (imagem.getpixel((xp, yp))[0] * kernel[i + 1][j + 1])
                    sum[1] += (imagem.getpixel((xp, yp))[1] * kernel[i + 1][j + 1])
                    sum[2] += (imagem.getpixel((xp, yp))[2] * kernel[i + 1][j + 1])
            img_alterada.putpixel(
                (x, y), value=(int(sum[0] / weight), int(sum[1] / weight), int(sum[2] / weight))
            )
    return img_alterada

    

exemplos = []

#Abre a imagem.
print("Laplacian...", end="")
exemplos.append(Image.open("exemplo1.jpg")) 
image = laplacian(exemplos[0])
print("OK.")
showImage(image, contadorExemplos= 1)

print("Sharpening...", end="")
exemplos.append(Image.open("exemplo2.jpg")) 
image = sharpening(exemplos[1])
print("OK.")
showImage(image, contadorExemplos= 2)

print("LoG...", end="")
sigma = 1
size = 5
exemplos.append(Image.open("exemplo3.jpg")) 
image = laplacian(gaussian_smooth(exemplos[2], size, sigma))
print("OK.")
showImage(image, contadorExemplos= 3)

print("Unsharp...", end="")
exemplos.append(Image.open("exemplo4.jpg")) 
image = unsharp(exemplos[3], k= 0.5)
print("OK.")
showImage(image, contadorExemplos= 4)

print("High boost...", end="")
exemplos.append(Image.open("exemplo5.jpg")) 
image = high_boost(exemplos[4], a=2)
print("OK.")
showImage(image, contadorExemplos= 5)

