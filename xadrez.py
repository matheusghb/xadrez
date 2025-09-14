def jgdcor(c):
      if c==1:
            return "branco"
      else:
            return 'preto'

def mtab(ch):
    print('    1     2      3     4     5     6     7     8 \n'
          '  -   -   -   -   -   -   -   -   -   -   -   -   -\n'
          '1 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '2 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '3 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '4 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '5 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '6 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '7 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '8 | %s | %s | %s | %s | %s | %s | %s | %s | \n'
          '  -   -   -   -   -   -   -   -   -   -   -   -   -\n' %(ch[0:3], ch[3:6], ch[6:9], ch[9:12], ch[12:15], ch[15:18], ch[18:21], ch[21:24], 
                                                                  ch[24:27], ch[27:30], ch[30:33], ch[33:36],
                                                                  ch[36:39], ch[39:42], ch[42:45], ch[45:48],
                                                                  ch[48:51], ch[51:54], ch[54:57], ch[57:60], ch[60:63], ch[63:66], ch[66:69], ch[69:72],
                                                                  ch[72:75], ch[75:78], ch[78:81], ch[81:84], ch[84:87], ch[87:90], ch[90:93], ch[93:96],
                                                                  ch[96:99], ch[99:102], ch[102:105], ch[105:108], ch[108:111], ch[111:114], ch[114:117], ch[117:120],
                                                                  ch[120:123], ch[123:126], ch[126:129], ch[129:132], ch[132:135], ch[135:138], ch[138:141], ch[141:144],
                                                                  ch[144:147], ch[147:150], ch[150:153], ch[153:156], ch[156:159], ch[159:162], ch[162:165], ch[165:168],
                                                                  ch[168:171], ch[171:174], ch[174:177], ch[177:180], ch[180:183], ch[183:186], ch[186:189], ch[189:192]
                                                                  ))

def checkp(a, b, chk):
      if len(a)<3:
            while len(a)<3:
                  a = a+' '
      c = a[2]

      if (b == 'preto' and c == 'b') or (b == 'branco' and c == 'p'):
            return False
      else:
            return (((chk.find(a))//3)+1)

def movp (a, b, pos,pep):

      #a = peça
      #b = posição desejada
      #pos = posição atual
      #c = cor da peça

      pc = a[0]
      flg = 0 
      if a[2]==ch[(b*3)-1:(b*3)]:
            print('É uma peça de mesma cor.')
            flg=1
      else:
            print (a, pep.find(a), pep)
            if pc == 'p': #peão
                  p = 8
                  if a[2] == 'b':
                        p = p*(-1)

                  if pep.find(a)==(-1) and (b==pos+(p*2)):
                        return True
                  else:
                        if b != pos+p:
                              if (b==(pos+(p+1)) and ch[((pos+(p+1))*3)-3:((pos+(p+1))*3)]=='   ') and (b==(pos+(p-1)) and ch[((pos+(p-1))*3)-3:((pos+(p-1))*3)]=='   '):
                                    flg = 1
                              else:
                                    if b!=pos+p and b!=pos+(p-1) and b!=pos+(p+1):
                                          flg = 1
                        else:
                              if (b==pos+p and (ch[((pos+p)*3)-3:((pos+p)*3)]!='   ')):
                                    print('A peça %s está no caminho.'%(ch[((pos+p)*3)-3:((pos+p)*3)]))
                                    flg = 1
            
            elif pc == 'b': #bispo
                  i = 1
                  while i<8:
                        if b == (pos+(7*i)) or b == (pos+(9*i)) or b == (pos+(-(9*i))) or b == (pos+(-(7*i))):
                              flg = 0

                              if b == pos+(7*i): #inferior esquerda
                                    dire = 1
                              elif b == pos+(-(7*i)): #superior direita
                                    dire = 2
                              elif b == pos+(-(9*i)): #superior esquerda
                                    dire = 3
                              elif b == pos+(9*i): #inferior direita
                                    dire = 4
                              j = i-1
                              i = i+8
                              while j>0:
                                    if dire == 1: #diagonal inferior esquerda
                                          if ch[((pos+(+(7*j)))*3)-3:(((pos+(7*j)))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(+(7*j)))*3)-3:(((pos+(7*j)))*3)]))
                                                flg = 1
                                                break

                                    elif dire == 4: #diagonal inferior direita.
                                          if ch[((pos+(9*j))*3)-3:((pos+(9*j))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(9*j))*3)-3:((pos+(9*j))*3)]))
                                                flg = 1
                                                break

                                    elif dire == 3: #diagonal superior esquerda.
                                          if ch[((pos+(-(9*j)))*3)-3:((pos+(-(9*j)))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(-(9*j)))*3)-3:((pos+(-(9*j)))*3)]))
                                                flg = 1
                                                break 

                                    elif dire == 2: #diagonal superior direita
                                          if ch[((pos+(-(7*j)))*3)-3:((pos+(-(7*j)))*3)] != '   ' :
                                                print('A peça %s está no caminho.'%(ch[((pos+(-(7*j)))*3)-3:((pos+(-(7*j)))*3)]))
                                                flg = 1
                                                break
                                    j = j-1
                        else:
                              flg = 1
                        i = i+1

            elif pc == 't': #torre
                  direcao = None
                  passo = 0

                  if b % 8 == pos % 8:  # mesma coluna (vertical)
                        if b > pos:
                              passo = 8
                        else:
                              passo = -8
                  elif (b - 1) // 8 == (pos - 1) // 8:  # mesma linha (horizontal)
                        if b > pos:
                              passo = 1
                        else:
                              passo = -1
                  else:
                        flg = 1  # movimento inválido
                        passo = 0

                  if passo != 0:
                        i = pos + passo
                        while i != b:
                              if ch[(i * 3) - 3:(i * 3)] != '   ':
                                    print('A peça %s está no caminho.' % ch[(i * 3) - 3:(i * 3)])
                                    flg = 1
                                    break
                              i += passo

            elif pc == 'c': #cavalo
                  if b !=pos-17 and b!=pos-15 and b!=pos-6 and b!=pos+10 and b!=pos+17 and b!=pos+15 and b!=pos+6 and b!=pos-10:
                        flg = 1
            
            elif pc == 'r': #rei
                  if b!=(pos+8) and b!=pos-8 and b!=pos-1 and b!=pos+1 and b!=pos+9 and b!=pos+7 and b!=pos-7 and b!=pos-9:
                        flg = 1
            
            else: #rainha
                  i = 1
                  while i<8:
                        if b == (pos+(7*i)) or b == (pos+(9*i)) or b == (pos+(-(9*i))) or b == (pos+(-(7*i))):
                              flg = 0

                              if b == pos+(7*i): #inferior esquerda
                                    dire = 1
                              elif b == pos+(-(7*i)): #superior direita
                                    dire = 2
                              elif b == pos+(-(9*i)): #superior esquerda
                                    dire = 3
                              elif b == pos+(9*i): #inferior direita
                                    dire = 4
                              j = i-1
                              i = i+8
                              while j>0:
                                    if dire == 1: #diagonal inferior esquerda
                                          if ch[((pos+(+(7*j)))*3)-3:(((pos+(7*j)))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(+(7*j)))*3)-3:(((pos+(7*j)))*3)]))
                                                flg = 1
                                                break

                                    elif dire == 4: #diagonal inferior direita.
                                          if ch[((pos+(9*j))*3)-3:((pos+(9*j))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(9*j))*3)-3:((pos+(9*j))*3)]))
                                                flg = 1
                                                break

                                    elif dire == 3: #diagonal superior esquerda.
                                          if ch[((pos+(-(9*j)))*3)-3:((pos+(-(9*j)))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(-(9*j)))*3)-3:((pos+(-(9*j)))*3)]))
                                                flg = 1
                                                break 

                                    elif dire == 2: #diagonal superior direita
                                          if ch[((pos+(-(7*j)))*3)-3:((pos+(-(7*j)))*3)] != '   ':
                                                print('A peça %s está no caminho.'%(ch[((pos+(-(7*j)))*3)-3:((pos+(-(7*j)))*3)]))
                                                flg = 1
                                                break
                                    j = j-1
                        else:
                              direcao = None
                              passo = 0

                              if b % 8 == pos % 8:  # mesma coluna (vertical)
                                    if b > pos:
                                          passo = 8
                                    else:
                                          passo = -8
                              elif (b - 1) // 8 == (pos - 1) // 8:  # mesma linha (horizontal)
                                    if b > pos:
                                          passo = 1
                                    else:
                                          passo = -1
                              else:
                                    flg = 1  # movimento inválido
                                    passo = 0

                              if passo != 0:
                                    y = pos + passo
                                    while y != b:
                                          if ch[(y * 3) - 3:(y * 3)] != '   ':
                                                print('A peça %s está no caminho.' % ch[(y * 3) - 3:(y * 3)])
                                                flg = 1
                                                break
                                          y += passo
                        i = i+1

                        if flg == 1:
                              direcao = None
                              passo = 0

                              if b % 8 == pos % 8:  # mesma coluna (vertical)
                                    if b > pos:
                                          passo = 8
                                    else:
                                          passo = -8
                              elif (b - 1) // 8 == (pos - 1) // 8:  # mesma linha (horizontal)
                                    if b > pos:
                                          passo = 1
                                    else:
                                          passo = -1
                              else:
                                    flg = 1  # movimento inválido
                                    passo = 0

                              if passo != 0:
                                    i = pos + passo
                                    while i != b:
                                          if ch[(i * 3) - 3:(i * 3)] != '   ':
                                                print('A peça %s está no caminho.' % ch[(i * 3) - 3:(i * 3)])
                                                flg = 1
                                                break
                                          i += passo

            if flg == 0:
                  return True
            else:
                  return False

ch = 't1pc1pb1pR1pr1pb2pc2pt2pp1pp2pp3pp4pp5pp6pp7pp8p                                                                                                p1bp2bp3bp4bp5bp6bp7bp8bt1bc1bb1bR1br1bb2bc2bt2b'


print('Isso é uma simulação de xadrez feita dentro do console do Visual Studio Code.\n'
      'Grupo: Kaio Mariano, Pedro Igor, Matheus Guilherme, Yuri e Roberto Eugênio.\n' \
      '\n' \
      'Diga primeiro a coordenada da PEÇA que planeja mover,\ncom base no nome, seguindo esse padrão:\n\n' \
      'PeçaOrdemCor\n\n'
      'Peça: t = Torre, c = Cavalo, b = Bispo, r = Rei, R = Rainha, p = Peão.\n'
      'Ordem: Os números (1-8) ditam peças repetidas e onde estavam no começo.\n'
      'Cor: p = Preta, b = Branca.\n')

s=0
c=1
cor = ''
wflg = 0
r = 1
cemb = 'Peças adquiridas: '
cemp = 'Peças adquirias: '
i = 2
pep = ''

while (s==0):
      if wflg == 1:
            print('O time %s venceu.'%(jgdcor(abs(c))))
            break
      flg = 0
      cor = jgdcor(c)
      if cor == 'branco':
            cm = cemb
      else:
            cm = cemp
      print('\n\nTurno de %s. rodada %i.\n%s'%(cor, r,cm))
      mtab(ch)
      op = input('\nO que você deseja fazer?\n1 - Mover\n2 - Passar\n3 - Desistir\n4 - Sair\n=> ')
      s= 1
      if (op=='1'):
            pc = input('Digite o nome da peça que você deseja movimentar: ')
            posp = checkp(pc, cor, ch)
            if (posp<0 or posp==False):
                  flg = 1
                  print('\nCredênciais incorretas.')
            else:
                  if pc[0]!='p':
                        ch = ch.replace(' . ','   ')
                  pos = input('Digite onde você deseja posicionar essa peça (colunalinha): ')
                  try:
                        pos = (int(pos[0])+((int(pos[1])-1)*8))
                  except:
                        print ('Credênciais incorretas.')
                        c = abs(c-1)
                  else:
                        chk = movp(pc, pos, posp,pep)
                        t = ch[(pos*3)-3:(pos*3)]
                        pp = ch[(posp*3)-3:(posp*3)]
                        if chk == True:
                              en = ch[((ch.find(' . '))):(ch.find(' . '))+3]
                              ch = ch.replace(' . ','   ')
                              if (ch[(posp*3)-3:(posp*3)-2]=='p'):
                                    if pep.find(pp)==(-1):
                                          pep = pep+pp
                                          p = 8
                                          if pp[2]=='p':
                                                p = p*(-1)
                                          if posp+(-p) != pos:
                                                ch = ch[:((pos+p)*3)-3]+' . '+ch[((pos+p)*3):]
                              if (ch[(posp*3)-3:(posp*3)-2]=='p') and (pos<9 or pos>56):
                                    i = i+1
                                    flgu = 1
                                    opc = ''
                                    while flgu == 1:
                                          flgu = 0
                                          opc = str(input('Qual peça você deseja obter?\n1 - Torre\n2 - Cavalo\n3 - Bispo\n4 - Rainha\n=> '))

                                          if opc=='1':
                                                opc = 't'
                                          elif opc=='2':
                                                opc = 'c'
                                          elif opc=='3':
                                                opc = 'b'
                                          elif opc=='4':
                                                opc = 'R'
                                          else:
                                                print('Bote uma das opções acima.')
                                                flgu = 1
                                    ch = ch[:(posp*3)-3]+opc+str(i)+pp[2]+ch[(posp*3):]
                              if t=='   ' or t==' . ':
                                    if en==' . ' and t==' . ' and pp[0]=='p':
                                          if ch[(((pos+(-(p)))*3))-1:((pos+(-(p)))*3)]=='b':
                                                cemp = cemp+ch[(((pos+(-(p)))*3))-3:((pos+(-(p)))*3)]+', '
                                          else:
                                                cemb = cemb+ch[(((pos+(-(p)))*3))-3:((pos+(-(p)))*3)]+', '
                                          ch = ch[:(((pos+(-(p)))*3))-3]+'   '+ch[((pos+(-(p)))*3):]

                                    ch = ch[:(pos*3)-3]+pp+ch[(pos*3):]
                                    ch = ch[:(posp*3)-3]+'   '+ch[posp*3:]
                              else:
                                    if ch[(pos*3)-1:(pos*3)]=='b':
                                          cemp = cemp+ch[(pos*3)-3:(pos*3)]+', '
                                    else:
                                          cemb = cemb+ch[(pos*3)-3:(pos*3)]+', '
                                    ch = ch[:(pos*3)-3]+pp+ch[(pos*3):]
                                    ch = ch[:(posp*3)-3]+'   '+ch[posp*3:]
            
                              r = r+abs(c-1)
                              if ch.find('r1b')==-1 or ch.find('r1p')==-1:
                                    wflg = 1
                        else:
                              print ('Posição incorreta.')
                              c = abs(c-1)
      if (op=='2'):
            s=0
            r = r+abs(c-1)
      elif (op=='3'):
            print('O time %s venceu em %i rodadas.'%(jgdcor(abs(c-1)), r))
            break
      elif (op=='4'):
            print('\nFechando o programa.')
            break
      elif (op!='1' and op!='2' and op!='3' and op!='4'):
            flg = 1
            print('\nCredênciais incorretas.')
      if (flg<1):
            c = abs(c-1)
      s = 0
