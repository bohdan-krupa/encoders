import cv2
import random
import numpy as np

seed = input('Key: ')
random.seed(seed)

image = cv2.imread('encoded.bmp')
rows, cols, other = image.shape

image_secret_colors_bin = []

for row in range(rows):
  for col in range(cols):
    rand = random.randint(0, 2)
    b, g, r = image[row, col]

    bin_rest_1 = format(r, '08b')[-2:] if rand == 0 else format(r, '08b')[-3:]
    bin_rest_2 = format(g, '08b')[-2:] if rand == 1 else format(g, '08b')[-3:]
    bin_rest_3 = format(b, '08b')[-2:] if rand == 2 else format(b, '08b')[-3:]

    image_secret_colors_bin.append(bin_rest_1 + bin_rest_2 + bin_rest_3)

height = int(f'0b{image_secret_colors_bin[0] + image_secret_colors_bin[1]}', 2)
width = int(f'0b{image_secret_colors_bin[2] + image_secret_colors_bin[3]}', 2)
image_output = np.zeros((height, width, 3), np.uint8)

for row in range(height):
  for col in range(width):
    index = (col + width * row) * 3 + 4

    if len(image_secret_colors_bin) > index + 2:
      image_output[row, col] = [
        int(f'0b{image_secret_colors_bin[index + 2]}', 2),
        int(f'0b{image_secret_colors_bin[index + 1]}', 2),
        int(f'0b{image_secret_colors_bin[index]}', 2)
      ]

cv2.imwrite('output.jpg', image_output)