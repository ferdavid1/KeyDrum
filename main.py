import pygame
import time
from curtsies import Input
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# kick = pygame.mixer.Sound('samples/kick.wav')
# clap = pygame.mixer.Sound('samples/clap.wav')
# cymbal = pygame.mixer.Sound('samples/cymbal.wav')
# snare = pygame.mixer.Sound('samples/snare.wav')
# champion = pygame.mixer.Sound('samples/champion.wav')
# closed = pygame.mixer.Sound('samples/closed.wav')
# ahems = pygame.mixer.Sound('samples/ahem.wav')
# doit = pygame.mixer.Sound('samples/doit.wav')
# force = pygame.mixer.Sound('samples/force.wav')

'''
matrix format for each bank:
(kick)       k1 k2 k3 k4 k5 k6
(snare)      s1 s2 s3 s4 s5 s6
(open hat)   o1 o2 o3 o4 o5 o6
(closed hat) c1 c2 c3 c4 c5 c6
(808s/Bass)  b1 b2 b3 b4 b5 b6
(percs)      p1 p2 p3 p4 p5 p6

                   ^
                   |
                   |

             1  2  3  4  5  6
             q  w  e  r  t  y
             a  s  d  f  g  h
             z  x  c  v  b  n
             7  8  9  0  j  k
             u  i  o  p  l  n

name each file 1.wav 2.wav q.wav etc in each sample bank
'''

banks = iter(list(["Bank1_Trap", "Bank2_BoomBap", "Bank3_Experimental", "Bank4_HouseTechno", "Bank5_RockJazz"]))
current_bank = next(banks) # default
print(current_bank)
# print current bank to LCD Display
with Input(keynames='curses') as input_generator:
  for e in input_generator:
    if e == "KEY_DOWN":
      if current_bank == "Bank5_RockJazz":
        banks = iter(list(["Bank1_Trap", "Bank2_BoomBap", "Bank3_Experimental", "Bank4_HouseTechno", "Bank5_RockJazz"])) # reset the iterator
        current_bank = next(banks)
      else:
        current_bank = next(banks)
      print(current_bank) # print it out to LCD display
    else:
      pygame.mixer.Sound("samples/" + current_bank + "/" + e+".wav").play()

# time.sleep(0.001)   #sleep for 1ms