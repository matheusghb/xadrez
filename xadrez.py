def mtab(aa, ab, ac, ad, ae, af, ag, ah, 
         ba, bb, bc, bd, be, bf, bg, bh, 
         ca, cb, cc, cd, ce, cf, cg, ch,
         da, db, dc, dd, de, df, dg, dh,
         ea, eb, ec, ed, ee, ef, eg, eh, 
         fa, fb, fc, fd, fe, ff, fg, fh,
         ga, gb, gc, gd, ge, gf, gg, gh,
         ha, hb, hc, hd, he, hf, hg, hh):
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
          '  -   -   -   -   -   -   -   -   -   -   -   -   -\n' %(aa, ab, ac, ad, ae, af, ag, ah, 
                                                           ba, bb, bc, bd, be, bf, bg, bh,
                                                           ca, cb, cc, cd, ce, cf, cg, ch,
                                                           da, db, dc, dd, de, df, dg, dh,
                                                           ea, eb, ec, ed, ee, ef, eg, eh,
                                                           fa, fb, fc, fd, fe, ff, fg, fh,
                                                           ga, gb, gc, gd, ge, gf, gg, gh,
                                                           ha, hb, hc, hd, he, hf, hg, hh))

def checkp(a, b, chk):
      c = a[2]

      if (b == 'preto' and c == 'b') or (b == 'branco' and c == 'p'):
            return False
      else:
            return (((chk.find(a))/3)+1)

def movp (a, b, pos):
      
      #a = peça
      #b = posição desejada
      #pos = posição atual

      pc = a[1]

      if pc == 'p':
            if b == (pos+7) or b == (pos+9):
                  print ('válido')
            else:
                  print ('inválido')
      
      if pc == 'b':
            i = 1
            flg = 0
            while flg<1:
                  if b == (pos+(7*i)) or b == (pos+(9*i)):
                        pass
                  else:
                        flg = 1
            if flg == 0:
                  print ('válido.')
            else:
                  print ('inválido.')
      
      if pc == 't':
            m = pos//8
            if (b!=pos) and (b>((8*m))):
                  pass
      
      if pc == 'c':
            if b == (pos-17 or pos-15 or pos-6 or pos+10 or pos+17 or pos+15 or pos+6 or pos-10):
                  print('válido')
            else:
                  print('inválido')
      
      if pc == 'r':
            if b == (pos+8 or pos-8 or pos-1 or pos+1 or pos+9 or pos+7 or pos-7 or pos-9):
                  print ('válido')
            else:
                  print ('inválido')
      
ch = 't1pc1pb1pR1pr1pb2pc2pt2pp1pp2pp3pp4pp5pp6pp7pp8p                                                                                                p1bp2bp3bp4bp5bp6bp7bp8bt1bc1bb1bR1br1bb2bc2bt2b'

a1=ch[0:3] 
a2=ch[3:6]
a3=ch[6:9]
a4=ch[9:12]
a5=ch[12:15]
a6=ch[15:18]
a7=ch[18:21]
a8=ch[21:24]
b1=ch[24:27]
b2=ch[27:30]
b3=ch[30:33]
b4=ch[33:36]
b5=ch[36:39]
b6=ch[39:42]
b7=ch[42:45]
b8=ch[45:48]
c1=ch[48:51]
c2=ch[51:54]
c3=ch[54:57]
c4=ch[57:60]
c5=ch[60:63]
c6=ch[63:66]
c7=ch[66:69]
c8=ch[69:72]
d1=ch[72:75]
d2=ch[75:78]
d3=ch[78:81]
d4=ch[81:84]
d5=ch[84:87]
d6=ch[87:90]
d7=ch[90:93]
d8=ch[93:96]
e1=ch[96:99]
e2=ch[99:102]
e3=ch[102:105]
e4=ch[105:108]
e5=ch[108:111]
e6=ch[111:114]
e7=ch[114:117]
e8=ch[117:120]
f1=ch[120:123]
f2=ch[123:126]
f3=ch[126:129]
f4=ch[129:132]
f5=ch[132:135]
f6=ch[135:138]
f7=ch[138:141]
f8=ch[141:144]
g1=ch[144:147]
g2=ch[147:150]
g3=ch[150:153]
g4=ch[153:156]
g5=ch[156:159]
g6=ch[159:162]
g7=ch[162:165]
g8=ch[165:168]
h1=ch[168:171]
h2=ch[171:174]
h3=ch[174:177]
h4=ch[177:180]
h5=ch[180:183]
h6=ch[183:186]
h7=ch[186:189]
h8=ch[189:192]

ch = a1+a2+a3+a4+a5+a6+a7+a8+b1+b2+b3+b4+b5+b6+b7+b8+c1+c2+c3+c4+c5+c6+c7+c8+d1+d2+d3+d4+d5+d6+d7+d8+e1+e2+e3+e4+e5+e6+e7+e8+f1+f2+f3+f4+f5+f6+f7+f8+g1+g2+g3+g4+g5+g6+g7+g8+h1+h2+h3+h4+h5+h6+h7+h8

print('Isso é uma simulação de xadrez feita dentro do console do Visual Studio Code.\n'
      'Grupo: Kaio Mariano, Pedro Igor, Matheus Guilherme e Yuri.\n' \
      '\n' \
      'Diga primeiro a coordenada da PEÇA que planeja mover,\ncom base no nome, seguindo esse padrão:\n\n' \
      'PeçaOrdemCor\n\n'
      'Peça: t = Torre, c = Cavalo, b = Bispo, r = Rei, R = Rainha, p = Peão.\n'
      'Ordem: Os números (1-8) ditam peças repetidas e onde estavam no começo.\n'
      'Cor: p = Preta, b = Branca.\n')

s=0
c=1
cor = ''

print(ch)

while (s==0):

      flg = 0
      if (c==1):
            cor = 'branco'
      else:
            cor = 'preto'
      print('\n\nTurno de %s.\n'%(cor))
      print(mtab(a1,a2,a3,a4,a5,a6,a7,a8,
            b1,b2,b3,b4,b5,b6,b7,b8,
            c1,c2,c3,c4,c5,c6,c7,c8,
            d1,d2,d3,d4,d5,d6,d7,d8,
            e1,e2,e3,e4,e5,e6,e7,e8,
            f1,f2,f3,f4,f5,f6,f7,f8,
            g1,g2,g3,g4,g5,g6,g7,g8,
            h1,h2,h3,h4,h5,h6,h7,h8))
      op = int(input('\nO que você deseja fazer?\n1 - Mover\n2 - Passar\n3 - Desistir\n4 - Sair\n=> '))
      s= 1
      if (op==1):
            pc = input('Digite o nome da peça que você deseja movimentar: ')
            t = checkp(pc, cor, ch)
            if (t<0 or t==False):
                  flg = 1
                  print('\nCredênciais incorretas.')
            else:
                  pos = int(input('Digite onde você deseja posicionar essa peça: '))
      if (op==2):
            s=0
      if (op==3):
            s=0
      if (op==4):
            print('\nFechando o programa.')
      if (flg>0):
            pass
            s = 0
      else:
            c = abs(c-1)
            s = 0
