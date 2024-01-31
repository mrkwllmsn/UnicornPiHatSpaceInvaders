import PIL.Image as Image ,PIL.ImageDraw as ImageDraw

class player:
  def __init__(self): 
      self.lives = 5
      self.velocity = 0
      self.direction = 0
      self.x = 7 
      self.y = 15 
      self.colour = 'yellow'
      self.score = 0

  def draw(self, image, velocity): 
      self.image = image
      self.velocity = velocity
      self.x = self.x + velocity

      if(self.x < 0):
          self.x = 0;
      if(self.x > 15):
          self.x = 15;

      draw = ImageDraw.Draw(self.image)
      draw.point((self.y, self.x), fill=self.colour) 
      draw.point((self.y-1, self.x), fill=self.colour) 
      draw.point((self.y, self.x-1), fill=self.colour) 
      draw.point((self.y, self.x+1), fill=self.colour) 
      return self.image

