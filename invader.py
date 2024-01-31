import PIL.Image as Image ,PIL.ImageDraw as ImageDraw
from definitions import * 
import random 
from bullet import bullet
invaderColours = ['blue', 'rgb(255,0,255)', 'pink', 'orange', 'rgb(190,5,220)']

class invader:
  def __init__(self,  unicornHatController, y, x, enemyType, level): 
      self.x = x
      self.y = y
      self.r =2 
      self.enemyType = enemyType
      self.unicornHatController = unicornHatController
      self.velocity = 1
      self.direction = RIGHT
      self.frameCount=0
      self.speedModulatorBase = 10
      self.speedModulator = 10
      self.level = level

      if(self.level >= len(invaderColours)):
        self.colour = invaderColours[random.randint(0,len(invaderColours)-1)]
      else:
        if self.level < 0:
            self.level = 0

        self.colour = invaderColours[self.level]


  def draw(self, image, bullets): 
      if(self.speedModulator > 1):
          if(self.level > 2):
              self.speedModulator = self.speedModulatorBase - self.level


      # randomly fire a bullet
      if(random.randint(1,1000) > ENEMY_SHOOT_MODIFIER - ((self.level+1)/2)):
         bullet_colour = 'rgb(255,2,3)'
         bullet_velocity = ENEMY_SHOOT_VELOCITY + (self.level*0.05)
         bullets.append( bullet(self.x+1,self.y,bullet_velocity,bullet_colour)) 



      self.image = image
      draw = ImageDraw.Draw(self.image) 
      self.frameCount = self.frameCount+1;

      if(self.y > INVADE_LIMIT):
          if(self.x < 0):
            self.x=0
          self.y = INVADE_LIMIT
          if(self.x < 1 or self.x > 14):
            self.direction = UP

      if(self.y > SCREEN_HEIGHT):
          self.y=-2;
      
      

      if(self.direction == RIGHT):
        draw.point((self.y, self.x), fill=self.colour) 
        draw.point((self.y+1, self.x), fill="rgb(0,255,0)") 
        draw.point((self.y+1, self.x-1), fill=self.colour) 
        if(self.speedModulator < 1):
            self.speedModulator = 1; # Max speed

        if(self.frameCount % self.speedModulator == 0):
            self.x = int(self.x + self.velocity)
        if(self.x > SCREEN_WIDTH-1):
                if(self.frameCount % INVADERDOWN):
                  self.direction = DOWNLEFT
                else:
                  self.direction = LEFT


      if(self.direction == LEFT):
        draw.point((self.y, self.x), fill=self.colour) 
        draw.point((self.y-1, self.x), fill="rgb(0,255,0)") 
        draw.point((self.y-1, self.x+1), fill=self.colour) 
        if(self.frameCount % self.speedModulator == 0):
            self.x = self.x - self.velocity
        if(self.x < 1):
            if(self.frameCount % INVADERDOWN):
                self.direction = DOWNRIGHT
            else:
                self.direction = RIGHT

      if(self.direction == UP):
        draw.point((self.y-self.velocity, self.x), fill=self.colour) 
        draw.point((self.y+1, self.x), fill="orange") 
        self.y = self.y - self.velocity 
        draw.point((self.y-1, self.x), fill="rgb(0,255,0)") 
        draw.point((self.y-1, self.x+1), fill=self.colour) 
        if(self.y < 2):
            self.direction = RIGHT



      if(self.direction == DOWNLEFT):
          self.y = self.y+1 + self.velocity
          self.x = self.x+1 - self.velocity
          self.direction = LEFT

      if(self.direction == DOWNRIGHT):
          self.y = self.y+1 + self.velocity
          self.x = self.x - self.velocity
          self.direction = RIGHT

      return self.image

  def circle(self,r,n=12):
        return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

  def set_interval(func, sec):
      def func_wrapper():
          set_interval(func, sec)
          func()
      t = threading.Timer(sec, func_wrapper)
      t.start()
      return t 



