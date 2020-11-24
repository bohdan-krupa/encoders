import cv2
import random

seed = input('Key: ')
random.seed(seed)

with open('secret.txt', 'r') as file:
  secret_bin_array = list(format(ord(char), '016b') for char in file.read())

splited_secret_bin_array = []

for secret_bin in secret_bin_array:
  splited_secret_bin_array.append(secret_bin[:8])
  splited_secret_bin_array.append(secret_bin[-8:])


image = cv2.imread('input.jpg')
rows, cols, other = image.shape


if not len(splited_secret_bin_array) > rows * cols:
  for row in range(rows):
    for col in range(cols):
      index = col + cols * row
      
      if len(splited_secret_bin_array) > index:
        current_secret_bin = splited_secret_bin_array[index]
      else:
        current_secret_bin = '00000000'

      rand = random.randint(0, 2)
      b, g, r = image[row, col]
      r_bin = ''; g_bin = ''; b_bin = ''

      if rand == 0:
        r_bin = format(r, '08b')[:-2] + current_secret_bin[:2]
        g_bin = format(g, '08b')[:-3] + current_secret_bin[2:5]
        b_bin = format(b, '08b')[:-3] + current_secret_bin[-3:]
      elif rand == 1:
        r_bin = format(r, '08b')[:-3] + current_secret_bin[:3]
        g_bin = format(g, '08b')[:-2] + current_secret_bin[3:5]
        b_bin = format(b, '08b')[:-3] + current_secret_bin[-3:]
      elif rand == 2:
        r_bin = format(r, '08b')[:-3] + current_secret_bin[:3]
        g_bin = format(g, '08b')[:-3] + current_secret_bin[3:6]
        b_bin = format(b, '08b')[:-2] + current_secret_bin[-2:]

      r = int(f'0b{r_bin}', 2)
      g = int(f'0b{g_bin}', 2)
      b = int(f'0b{b_bin}', 2)

      image[row, col] = [b, g, r]

  cv2.imwrite('encoded.bmp', image)
else:
  print('Secret message is too long for that image')