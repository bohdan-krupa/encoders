input_file = open('secret.txt', 'r')
input_binary = ''.join(format(ord(char), '08b') for char in input_file.read())
input_file.close()


common_text_file = open('common_text.txt', 'r')
common_text_array = common_text_file.read().split(' ')
common_text_file.close()


if len(common_text_array) > len(input_binary):
  for index, bit in enumerate(input_binary):
    common_text_array[index] += ' ' if bit == '1' else ''

  output_file = open('encoded_text.txt', 'w')
  output_file.write(' '.join(common_text_array))
  output_file.close()
else:
  print('Secret is too long for that text')