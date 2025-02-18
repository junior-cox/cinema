import opcao
# a lista fica do lodo de fora
cadeiras=['','','','','','','','','','']
donos=['','','','','','','','','']
while(True):
  opcao.op()
  prom=input('prom //')
  if(prom=='1'):
    #  adicina a rersseva e o dono
    opcao.linha()
    ca=int(input('qual cadeira //'))
    cb=str(input('o nome do dono //'))
    if ca>=10:
      print('   erro e de 0 a 9    ')
    if ca<=9:
      cadeiras.pop(ca)
      cadeiras.insert(ca,ca)
      donos.pop(ca)
      donos.insert(ca,cb)
  if(prom=='2'):
    opcao.linha()
    print('ai esta {}'.format(len(cadeiras)))
    print(cadeiras)
  if(prom=='3'):
    opcao.linha()
    opcao.preco()
  # e aqui que se ver
  if prom=='4':
    opcao.linha()
    don=int(input('qual o numero //'))
    opcao.linha()
    print('>>>>> o dono da cadeira {} e {} <<<<<'.format(cadeiras[don],donos[don]))
  if(prom=='sair'):
    exit()

# criador junior honrato 
# critinacox@gmail.com