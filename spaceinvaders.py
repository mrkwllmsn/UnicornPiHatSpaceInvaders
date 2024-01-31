#!/usr/bin/env python3
import time
import math
pi = math.pi
import sys

import subprocess 
import threading

from signal import pause

from colorsys import hsv_to_rgb
from datetime import datetime
import numpy
import itertools

from PIL import Image, ImageDraw, ImageFont, ImageOps
import unicornhathd 

import PIL
import PIL.Image as Image ,PIL.ImageDraw as ImageDraw

import threading

#SpaceInvaders stuff
import curses
from game import Game
from unicornHatController import UnicornHatController
from definitions import * 

try:
    rotation = 0 
    if len(sys.argv) > 1:
        try:
            rotation = int(sys.argv[1])
        except ValueError:
            print("Usage: {} <rotation>".format(sys.argv[0]))
            sys.exit(1)

    unicornhathd.rotation(rotation)




except KeyboardInterrupt:
    unicornhathd.off()


def saveHighScore(playerScore):
  try: 
        with open(HIGHSCORE_FILE, "w+") as f: 
             current_highscore = f.read()  
        if(int(current_highscore) < int(playerScore) or current_highscore == ""):
             with open(HIGHSCORE_FILE, "w+") as f: 
                f.write(playerScore)  
        current_highscore = playerScore
  except ValueError:
      print("Can't save high scores.")
      sys.exit(1)




def main(stdscr):
    global PLAYER_VELOCITY

    game = Game(UnicornHatController(),16,16)
    game.createEnemies()
    game.addPlayer()

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(1)  

    # Game loop
    while True:
        # Listen for arrow key input to move the ship
        key = stdscr.getch()
        if key == curses.KEY_LEFT :
            PLAYER_VELOCITY = -1
        elif key == curses.KEY_RIGHT :
            PLAYER_VELOCITY = 1
        elif key == curses.KEY_UP or key == ord(' '):
            if(game.startScreen == True):
                game.start()
            if(game.gamestate == False and game.won == False):
                game.gamestate = True
                game.won = False
                game = Game(UnicornHatController(),16,16)
                game.enemies = [] 
                game.bullets = [] 
                game.enemybullets = [] 
                game.level = 0

                game.createEnemies()
                game.addPlayer()
            else:
                game.shoot()

        elif key == ord('q'):
            unicornhathd.off()
            break

        stdscr.clear()
        game.checkCollisions()
        game.draw(PLAYER_VELOCITY)
        PLAYER_VELOCITY = 0
        stdscr.refresh()


        time.sleep(1/120)  # 60fps @ 16x16 you knows it!

if __name__ == "__main__":
  try:
      PLAYER_VELOCITY = 0
      curses.wrapper(main)

  except KeyboardInterrupt:
      unicornhathd.off()


