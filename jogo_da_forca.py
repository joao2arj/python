import os #módulo utilizado (também) para limpar o terminal.

print('Bem vindo ao jogo da forca!')
opc = input('Digite a opção desejada: [J]ogar ou [S]air. ').upper()

if opc == 'J':
  palavra_secreta = input('Digite a palavra secreta: ').upper()
  palavra_formada = ''
  letra_certa = ''
  i = 0

while opc == 'J':
  i += 1
  os.system('cls')
  print(f'Palavra formada:', palavra_formada)
  print(f'Tentativas: ', i)
  letra = input("Digite uma letra: ").upper()

  if len(letra) > 1: #validação do número de caracteres
    print("Digite apenas uma letra de cada vez.")
    continue

  

  if letra in palavra_secreta:
    letra_certa += letra

    palavra_formada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letra_certa:
      palavra_formada += letra_secreta
    else:
      palavra_formada += '_'

  if palavra_formada == palavra_secreta:
    os.system('cls')
    print(f'Parabéns, você descobriu a palavra secreta: {palavra_secreta}!')
    opc = input('Digite [S]air ou [J]ogar novamente.').upper()
    if opc == 'S':
      print('Finalizando jogo...')
      break
    elif opc == 'J':
      palavra_secreta = input('Digite a nova palavra secreta: ').upper()
      palavra_formada = ''
      letra_certa = ''
      i = 0
    else:
      print('Digite uma opção válida')
      continue

else:
  print('Finalizando jogo...')


