from PIL import Image
from math import sqrt
from random import random

START_ADDRESS = 0x4000
STEPS = 5
# THRESHOLD = 127.5 # HALF: 127.5

def stepped_threshold(num, mini, maxi, steps, x, y):
    diff = maxi - mini
    step = diff / steps

    if num < mini + step:
        return False
    for i in range(2, steps-1):
        if num < (mini + step * i):
            return not ((x+y) % (steps-i))
    return True

def weighted_random_activation(pixels, x, y, height=None, width=None):
    rand = random()
    # return (sum(pixels[x,y]) / (765)) > rand
    return (pixels[x,y] / 255) > rand

def threshold_activation(pixels, x, y, height=None, width=None):
    return stepped_threshold(sum(pixels[x,y]) / 3, 0.0, 255.0, STEPS, x, y)
    
def surrounding_pixels_3x3(pixels, x, y):
    return [
        [pixels[x-1, y-1], pixels[x, y-1], pixels[x+1, y-1]],
        [pixels[x-1, y], pixels[x, y], pixels[x+1, y]],
        [pixels[x-1, y+1], pixels[x, y+1], pixels[x+1, y+1]]
    ]

def surrounding_pixels_2x2(pixels, x, y):
    return [
        [pixels[x, y], pixels[x+1, y]],
        [pixels[x, y+1], pixels[x+1, y+1]]
    ]

def prewitt_activation_3x3(pixels, x, y, height, width):
    if (not x) or (not y) or x == width-1 or y == height-1:
        return False

    pix = surrounding_pixels_3x3(pixels, x, y)
    gy = sum(pix[0][0]) + sum(pix[0][1]) + sum(pix[0][2])
    gy -= sum(pix[2][0]) + sum(pix[2][1]) + sum(pix[2][2])
    gx = sum(pix[0][0]) + sum(pix[1][0]) + sum(pix[2][0])
    gx -= sum(pix[0][2]) + sum(pix[1][2]) + sum(pix[2][2])

    g = sqrt(gy**2 + gx**2) # / 1081.8733
    return stepped_threshold(g, 0, 1082, STEPS, x, y)

def prewitt_activation_2x2(pixels, x, y, height, width):
    if x == width-1 or y == height-1:
        return False
    
    pix = surrounding_pixels_2x2(pixels, x, y)
    gy = sum(pix[0][0]) + sum(pix[0][1])
    gy -= sum(pix[1][0]) + sum(pix[1][1])
    gx = sum(pix[0][0]) + sum(pix[1][0])
    gx -= sum(pix[0][1]) + sum(pix[1][1])

    g = sqrt(gy**2 + gx**2) # / 1081.8733
    maxi = sqrt(((255.0 * 2)**2)*2)
    return stepped_threshold(g, 0, maxi, STEPS, x, y)

ACTIVATION_FUNCTION = prewitt_activation_2x2

image = Image.open('aperture5.jpg')
image = image.resize((512, 256))

pixels = image.load()
width, height = image.size

pointer = START_ADDRESS
data = {}
for y in range(height):
    for x in range(0, width, 16):
        start_bit = True if ACTIVATION_FUNCTION(pixels, x, y, height, width) else False
        register = '0b'
        willWrite = start_bit

        for z in range(1, 16):
            active = ACTIVATION_FUNCTION(pixels, x+z, y, height, width)
            if active ^ start_bit:
                willWrite = True
                register = register + '1'
            else:
                register = register + '0'
        
        if willWrite:
            if register not in data:
                data[register] = {True: [], False: []}
            data[register][start_bit].append(pointer)
            
        pointer += 1

text = ''
for register, points in data.items():
    text += 'A = ' + register + '\nD = A\n'
    for x in points[False]:
        text += f'A = {x}\n*A = D\n'
    if len(points[True]):
        text += 'D = ~D\n'
        for x in points[True]:
            text += f'A = {x}\n*A = D\n'

with open('out.txt', 'w') as f:
    f.write(text)
