import time
import math
pi = math.pi
import sys

import PIL.Image as Image ,PIL.ImageDraw as ImageDraw

from invader import invader
from player import player
from bullet import bullet
from definitions import *

FIRE_RATE = 995
class Game:
 invaderMapDefault = [ 
        [1,1,1,1],
        [1,1,1,1],
       ]

 invaderMap = [ 
        [1,1,1,1],
       ]
 screenWidth = 16;
 screenHeight = 16;
 enemies = []
 bullets = []
 enemybullets = []
 bulletLimit = PLAYER_CLIP_DEFAULT 
 gamestate = True 
 won = False 
 level = 1

 def __init__(self,  unicornHatController, screenWidth=16, screenHeight=16): 
      self.enemies = []
      self.bullets = []
      self.enemybullets = []
      self.invaderMap = self.invaderMapDefault
      self.screenWidth = screenWidth; 
      self.screenHeight = screenHeight; 
      self.unicornHatController = unicornHatController; 
      self.image = Image.new('RGBA', (self.screenWidth, self.screenWidth)) 
      self.invaderMap = self.invaderMapDefault
      self.level = 3
      self.startScreen = True 

 def start(self):
      self.startScreen = False 

 def draw(self, velocity):
      self.image = Image.new('RGBA', (self.screenWidth, self.screenWidth)) 
      self.velocity = velocity;

      self.checkGameState() 
      if(self.startScreen):
        self.unicornHatController.splashPlayScreen()
      else:
        if(self.gamestate):
          self.drawInvaders()
          self.drawPlayer()
          self.drawBullets()
          self.unicornHatController.draw(self.image)  
        else:
          if(self.won):
              print("YOU WIN THIS LEVEL")
              self.enemybullets = []
              self.invaderMap[0].append([1])
              self.enemies = []
              self.createEnemies()
              self.gamestate = True
              self.won = False
          else:
              print("GAME OVER!")
              print("FINAL SCORE:")
              print(self.player.score)
              self.invaderMap = self.invaderMapDefault
              self.showGameOver()
              self.gamestate = False
              self.won = False
              
 def drawPlayer(self):
       self.image = self.player.draw(self.image, self.velocity)


 def createEnemies(self): 
       xoffset = 4 
       yoffset = 4
       x  = 0
       y = 0
       for row in self.invaderMap: 
          for enemyType in row:
             self.addInvader(y+1,x,enemyType)
             x = x + xoffset 
          y = y + yoffset
          x = 0

 def addInvader(self,x,y,enemyType):
        self.enemies.append( invader(self.image,x,y,enemyType, self.level) )

 def drawInvaders(self):
   for enemy in self.enemies:
     self.image = enemy.draw(self.image, self.enemybullets)

 def addPlayer(self):
   self.player = player()

 def drawBullets(self):
   for bullet in self.bullets:
     self.image = bullet.draw(self.image)
   for bullet in self.enemybullets:
     self.image = bullet.draw(self.image)

 def shoot(self):
      if len(self.bullets) < self.bulletLimit:
          self.bullets.append( bullet(self.player.x,13,-1)) 
      else:
          print("BULLETS IN SELF", len(self.bullets))

 def checkCollisions(self):
    for bullet in self.bullets:
         if bullet.live == False:
            self.bullets.remove(bullet)
         else:
           x = bullet.x
           y = bullet.y
           r = bullet.r
           for enemy in self.enemies:
               if(enemy.x == bullet.x and enemy.y == bullet.y):
                  try:
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.player.score += 1
                  except ValueError:
                              self.log("Cant remove enemies or player bullets")
    for bullet in self.enemybullets:
         if bullet.x < 0 or bullet.y > 16:
              bullet.live = False

         if bullet.live == False:
            self.enemybullets.remove(bullet)
         else:
           x = bullet.x
           y = bullet.y
           r = bullet.r
           if(self.collidesWithPlayer(self.player,bullet)):
              self.player.colour = 'rgb(255,0,0)'
              try:
                self.enemybullets.remove(bullet)
                self.player.lives -= 1 
                self.gamestate = False 
                self.won = False
                self.level += 1
              except ValueError:
                          self.log("Cant remove enemybullets")

 def collidesWithPlayer(self, player, bullet):
        x = int(bullet.x)
        y = int(bullet.y)
        if(player.x == x and player.y+1 == y 
        or player.x+1 == x and player.y == y
        or player.x == x and player.y == y
        or player.x-1 == x and player.y == y):
            return True
        return False


 def checkGameState(self):
      if len(self.enemies) < 1: 
          self.gamestate = False 
          self.won = True
          self.level += 1

 def log(self, message):
      return message

 def showGameOver(self ):
     self.unicornHatController.gameOver(self.player.score)  
           
     
