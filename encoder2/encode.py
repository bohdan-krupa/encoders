LINE_LENGTH = 60

with open('secret.txt', 'r') as file:
  input_binary = ''.join(format(ord(char), '08b') for char in file.read())


input_spaces = []

for i in range(0, len(input_binary), 4):
  n = int(f'0b{input_binary[i:i+4]}', 2)
  
  input_spaces.append(n)


with open('common_text.txt', 'r') as file:
  common_text = file.read()


char_amount = 0
current_input_space = 0
encoded_text = ''

for char in common_text:
  char_amount += 1
  encoded_text += char

  if char_amount >= LINE_LENGTH and char == ' ' and len(input_spaces) > current_input_space:
    encoded_text += ' ' * (input_spaces[current_input_space] - 1) + '\n'

    current_input_space += 1
    char_amount = 0
  elif char_amount >= LINE_LENGTH and char == ' ' and len(input_spaces) <= current_input_space:
    encoded_text = encoded_text[:-1]
    encoded_text += '\n'

    char_amount = 0


with open('encoded_text2.txt', 'w') as file:
  file.write(encoded_text)