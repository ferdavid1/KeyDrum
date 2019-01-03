import pygame
import os
from curtsies import Input
"""
!!!!!!!!!!!!!!!!!!!!!
WHEN YOU START SETTING UP FOR LCD (16x2, 4 bit mode)
http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/
sudo pip install RPLCD
"""
# from RPLCD import CharLCD
# lcd = CharLCD(cols=16, rows=1, pin_rs=37, pin_e=35, pins_data=[33,31,29,23])

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
'''
switch matrix format for each bank:
(kick)       k1 k2 k3 k4 k5 k6
(snare)      s1 s2 s3 s4 s5 s6
(closed hat) c1 c2 c3 c4 c5 c6
(open hat)   o1 o2 o3 o4 o5 o6
(percs/fx)   p1 p2 p3 p4 p5 p6
(808s/inst)  b1 b2 b3 b4 b5 b6

                   ^
                   |
                   |

             1  2  3  4  5  6
             q  w  e  r  t  y
             a  s  d  f  g  h
             z  x  c  v  b  n
             7  8  9  0  j  k
             u  i  o  p  l  m

name each file 1.wav 2.wav q.wav etc in each sample bank
808s are only for the trap bank. the other banks have instrument samples in those spots.
'''

banks = iter(list(["Bank1_Trap", "Bank2_BoomBap", "Bank3_Experimental", "Bank4_HouseTechno", "Bank5_AcousticNoise"]))
current_bank = next(banks) # default
print(current_bank)

# print current bank to LCD Display:
# lcd.write_string(current_bank)
with Input(keynames='curses') as input_generator:
  for e in input_generator:
    print(repr(e))
    if e == "KEY_DOWN":
      if current_bank == "Bank5_AcousticNoise":
        banks = iter(list(["Bank1_Trap", "Bank2_BoomBap", "Bank3_Experimental", "Bank4_HouseTechno", "Bank5_AcousticNoise"])) # reset the iterator
        current_bank = next(banks)
      else:
        current_bank = next(banks)
      print(current_bank) # print it out to LCD display:
      # lcd.write_string(current_bank)
    else:
      try:
        pygame.mixer.Sound("samples/" + current_bank + "/" + e+".wav").play()
      except pygame.error:
        pass