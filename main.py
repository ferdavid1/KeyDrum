import pygame
import time
from curtsies import Input
pygame.mixer.pre_init(44100, -16, 2, 448)
pygame.init()
pygame.mixer.init()

kick = pygame.mixer.Sound('samples/kick.wav')
clap = pygame.mixer.Sound('samples/clap.wav')
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
snare = pygame.mixer.Sound('samples/snare.wav')
champion = pygame.mixer.Sound('samples/champion.wav')
closed = pygame.mixer.Sound('samples/closed.wav')
ahems = pygame.mixer.Sound('samples/ahem.wav')
doit = pygame.mixer.Sound('samples/doit.wav')
force = pygame.mixer.Sound('samples/force.wav')

with Input(keynames='curses') as input_generator:
  for e in input_generator:
    if (e == 'a'):  
      kick.play()  #west
    elif (e == "s"):
      snare.play() #center
    elif (e == "d"):
      closed.play() #east
    elif (e == "f"):
      cymbal.play() #south
    elif (e == "g"):
      clap.play() #north
    elif (e == "h"):
      champion.play() #swipe right
    elif (e == "j"):
      ahems.play() #swipe left
    elif (e == "k"):
      force.play() #swipe down
    elif (e == "l"):
      doit.play()

# time.sleep(0.001)   #sleep for 1ms