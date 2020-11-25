seed = int(input('Number: '))

for i in range(10):
  seed = int(str(seed * seed)[:6])

  print(f'Rand {i}: {seed}')