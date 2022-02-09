c = float(input('Digite  a temperatura da carne:'))
if c < 48:
 print('cozinhar mais')
elif c in range(48, 53):
 print('Selada')
elif c in range(54, 59):
 print('ao ponto para o mal')
elif c in range(60, 64):
  print('ao ponto')
elif c in range(65, 70):
  print('Ao ponto para o bem')
elif c >=71:
  print('Bem passada')