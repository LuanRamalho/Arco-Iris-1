# -*- coding: utf-8 -*-
import time                             #Importar biblioteca time
import pygame, sys                      #Importar biblioteca pygame e sys
from pygame.locals import *             #Importar todas (*) as funções do pygame.locals

def main():                             #Definindo a função principal
    larguradatela=600                   #Definindo uma variável "larguradatela" com o valor de 600
    alturadatela=600                    #Definindo uma variável "alturadatela" com o valor de 600
    pygame.init()                       #Iniciar o módulo PyGame
    DISPLAY=pygame.display.set_mode([larguradatela,alturadatela]) #Definindo as dimensõess da tela
    vermelho=(255,0,0)                  #Definindo a cor Vermelha
    laranja=(255,127,0)                 #Definindo a cor Laranja
    amarelo=(255,255,0)                 #Definindo a cor Amarela
    verde=(0,255,0)                     #Definindo a cor Verde
    azul=(0,0,255)                      #Definindo a cor Azul
    anil=(80,50,255)                    #Definindo a cor Anil
    violeta=(120,0,255)                 #Definindo a cor Violeta
    clock = pygame.time.Clock()         #Função para auxiliar na contagem do tempo
    k=6                                 #Definindo uma constande K com o valor 6
    x1=-larguradatela/k                 #Definindo uma constande x1 com o valor -larguradatela/k
    x2=x1+larguradatela/k               #Definindo uma constande x2 com o valor -larguradatela/k
    x3=x2+larguradatela/k               #Definindo uma constande x3 com o valor -larguradatela/k
    x4=x3+larguradatela/k               #Definindo uma constande x4 com o valor -larguradatela/k
    x5=x4+larguradatela/k               #Definindo uma constande x5 com o valor -larguradatela/k
    x6=x5+larguradatela/k               #Definindo uma constande x6 com o valor -larguradatela/k
    x7=x6+larguradatela/k               #Definindo uma constande x7 com o valor -larguradatela/

    while x1 < larguradatela:           #Enquanto o x1 for menor que larguradatela, fazer
      pygame.draw.rect(DISPLAY,vermelho,(x1,0,larguradatela/k,alturadatela))  #Desenhar retângulo vermelho
      x1=x1+1                           #Somar +1 ao valor de x1
      if x1 == larguradatela:           #Se x1 for igual a larguradatela, fazer:
        x1=-larguradatela/k             #Definir x1 como -larguradatela/k
      pygame.draw.rect(DISPLAY,laranja,(x2,0,larguradatela/k,alturadatela))  #Desenhar retângulo laranja
      x2=x2+1                           #Somar +1 ao valor de x2
      if x2 == larguradatela:           #Se x2 for igual a larguradatela, fazer:
        x2=-larguradatela/k             #Definir x2 como -larguradatela/k
      pygame.draw.rect(DISPLAY,amarelo,(x3,0,larguradatela/k,alturadatela))  #Desenhar retângulo amarelo
      x3=x3+1                           #Somar +1 ao valor de x3
      if x3 == larguradatela:           #Se x3 for igual a larguradatela, fazer:
        x3=-larguradatela/k             #Definir x3 como -larguradatela/k
      pygame.draw.rect(DISPLAY,verde,(x4,0,larguradatela/k,alturadatela))  #Desenhar retângulo verde
      x4=x4+1                           #Somar +1 ao valor de x4
      if x4 == larguradatela:           #Se x4 for igual a larguradatela, fazer:
        x4=-larguradatela/k             #Definir x4 como -larguradatela/k
      pygame.draw.rect(DISPLAY,azul,(x5,0,larguradatela/k,alturadatela))  #Desenhar retângulo azul
      x5=x5+1                           #Somar +1 ao valor de x5
      if x5 == larguradatela:           #Se x5 for igual a larguradatela, fazer:
        x5=-larguradatela/k             #Definir x5 como -larguradatela/k
      pygame.draw.rect(DISPLAY,anil,(x6,0,larguradatela/k,alturadatela))  #Desenhar retângulo anil
      x6=x6+1                           #Somar +1 ao valor de x6
      if x6 == larguradatela:           #Se x6 for igual a larguradatela, fazer:
        x6=-larguradatela/k             #Definir x6 como -larguradatela/k
      pygame.draw.rect(DISPLAY,violeta,(x7,0,larguradatela/k,alturadatela))  #Desenhar retângulo violeta
      x7=x7+1                           #Somar +1 ao valor de x7
      if x7 == larguradatela:           #Se x7 for igual a larguradatela, fazer:
        x7=-larguradatela/k             #Definir x7 como -larguradatela/k
      clock.tick(40)                    #Definindo 40 imagens / segundo
      pygame.display.update()           #Atualizações da tela para as novas posições dos

      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              pygame.quit()
              exit(0)



main()                                  #Executar a função principal

