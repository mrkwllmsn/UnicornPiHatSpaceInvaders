import PIL.Image as Image ,PIL.ImageDraw as ImageDraw

class bullet:
  
  def __init__(self, x, y, v=1, colour="white"):
      self.x = x
      self.y = y
      self.v = v
      self.r = 1
      self.colour = colour
      self.live = True

  def draw(self, image ):
      self.image = image
      draw = ImageDraw.Draw(self.image)
      draw.point((self.y, self.x), fill=self.colour) 
      self.y += self.v
      if(self.x < 0):
        self.live = False
      if(self.x > 15):
        self.live = False
      if(self.y < -1):
        self.live = False
      if(self.y > 17):
        self.live = False
          
      return self.image
