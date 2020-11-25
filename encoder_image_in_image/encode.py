import cv2
import random

seed = input('Key: ')
random.seed(seed)


image_input = cv2.imread('input.jpg')
rows_input, cols_input, other_input = image_input.shape
image_secret = cv2.imread('secret.jpg')
rows_secret, cols_secret, other_secret = image_secret.shape


if (rows_input * cols_input) / 3 > rows_secret * cols_secret:
  image_secret_colors_bin = []
  image_secret_rows_bin = format(rows_secret, '016b')
  image_secret_cols_bin = format(cols_secret, '016b')
  image_secret_colors_bin.append(image_secret_rows_bin[:8])
  image_secret_colors_bin.append(image_secret_rows_bin[-8:])
  image_secret_colors_bin.append(image_secret_cols_bin[:8])
  image_secret_colors_bin.append(image_secret_cols_bin[-8:])

  for row in range(rows_secret):
    for col in range(cols_secret):
      b, g, r = image_secret[row, col]
      image_secret_colors_bin.append(format(r, '08b'))
      image_secret_colors_bin.append(format(g, '08b'))
      image_secret_colors_bin.append(format(b, '08b'))

      
  for row in range(rows_input):
    for col in range(cols_input):
      index = col + cols_input * row
      
      if len(image_secret_colors_bin) > index:
        current_secret_bin = image_secret_colors_bin[index]
      else:
        current_secret_bin = '00000000'
  
      rand = random.randint(0, 2)
      b, g, r = image_input[row, col]
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

      image_input[row, col] = [b, g, r]


  cv2.imwrite('encoded.bmp', image_input)
else:
  print('Secret image is too large for that input image')