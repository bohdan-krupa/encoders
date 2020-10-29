import binascii

encoded_text_file = open('encoded_text.txt', 'r')
encoded_text = encoded_text_file.read()
encoded_text_file.close()

full_binary_secret = ''

for index, char in enumerate(encoded_text):
  if char == ' ' and encoded_text[index - 1] != ' ':
    full_binary_secret += '1' if encoded_text[index + 1] == ' ' else '0'


binary_secret = ''

for i in range(0, len(full_binary_secret), 8):
  binary_secret_part = full_binary_secret[i:i+8]

  if binary_secret_part != '00000000' and len(binary_secret_part) == 8:
    binary_secret += binary_secret_part


n = int(f'0b{binary_secret}', 2)
print(binascii.unhexlify('%x' % n).decode())