from hotel import Hotel
from guest import Guest

menu = 1
hoteis = []

while menu != 0:
  print('1 - Adicionar hotel\n2 - Ver hoteis\n3 - Remover hotel\n4 - Remover hóspede\n8 - Sair ')
  res = int(input())

  if res == 1:
    print('Adicionar hotel - Digite as informações abaixo: ')
    nomeHotel = input('Nome: ')
    capacidade = int(input('Capacidade: '))
    piscina = input('Tem piscina? (s/n): ')
    if piscina == 's':
      piscina = True
    else:
      piscina = False
    hoteis.append(Hotel(nomeHotel, capacidade, piscina))
    print('Hotel adicionado com sucesso!\n#################')

  elif res == 2:
    print('Ver hoteis - Exibindos todos os hotéis: ')
    for i in range(len(hoteis)):
      print(f'{i+1} - {hoteis[i].name}')
      hotelSelecionado = int(input('Selecione o hotel: '))
      print(f'Hotel Selecionado: {hoteis[hotelSelecionado-1].name}\n Capacidade do hotel: ')

  elif res == 8:
    print('Saindo...')
    menu = 0