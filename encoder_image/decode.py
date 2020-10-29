import cv2

image = cv2.imread('encoded.bmp')
rows, cols, other = image.shape

bin_parts_array = []

for row in range(rows):
  for col in range(cols):
    b, g, r = image[row, col]
    r_bin_rest = format(r, '08b')[-3:]
    g_bin_rest = format(g, '08b')[-2:]
    b_bin_rest = format(b, '08b')[-3:]

    bin_parts_array.append(r_bin_rest + g_bin_rest + b_bin_rest)


decoded_text = ''

for i in range(1, len(bin_parts_array), 2):
  char_bin = bin_parts_array[i - 1] + bin_parts_array[i]
  char_num = int(char_bin, 2)
  
  decoded_text += chr(char_num) if char_num != 0 else ''


with open('decoded_text.txt', 'w') as file:
  file.write(decoded_text)