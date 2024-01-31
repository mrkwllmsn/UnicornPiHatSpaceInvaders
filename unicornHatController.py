import time
import colorsys
from colorsys import hsv_to_rgb
import numpy
import itertools
import unicornhathd 
from definitions import *

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

font_file, font_size = FONT
font = ImageFont.truetype(font_file, font_size)

class UnicornHatController: 
    def __init__(self):
      self.image = None
      self.brightness = 10
      rising = range(5, 10, 1)    # [1...9]
      falling = range(10, 5, -1)  # [10...1]
      pattern = (rising,  falling)
      self.brightness_levels = list(itertools.chain.from_iterable(pattern))
      self.sinWave = self.brightness_levels
      self.brightness_delay=0.005
      self.framecount=1
      self.splashScreenToggle=False
      self.showScore=True

    def pulseBrightness(self):
      self.brightness = self.brightness_levels.pop()
      self.brightness_levels = [self.brightness] + self.brightness_levels

    def draw(self, image):  
      self.framecount += 1
      unicornhathd.brightness(self.brightness)
      offset_x = 0
      self.image = image
      display_width,display_height = image.size
      for y in range(display_height):
          for x in range(display_width):
              hue = ((time.time() / 100.0) + (x / float(display_width * 2)))
              r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1, self.brightness/20)] 
              try: 
                  xc = image.getpixel((x + offset_x, y)) 
                  xr =int(xc[0])
                  xg =int(xc[1])
                  xb =int(xc[2])
                  unicornhathd.set_pixel(x, y, xr, xg, xb)

              except IndexError:
                  offset_x = 0

      offset_x += 1

      if offset_x + display_width > image.size[0]:
          offset_x = 0

      unicornhathd.show()


    def splashPlayScreen(self):
          self.pulseBrightness()
          width, height = unicornhathd.get_shape()
          img = Image.open('assets/play_start2.png')

          display_width,display_height = img.size
          for y in range(display_height):
                    for x in range(display_width):
                        hue = ((time.time() / 100.0) + (x / float(display_width * 2)))
                        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1, self.brightness/20)] 
          for o_x in range(int(img.size[0] / width)):
              for o_y in range(int(img.size[1] / height)):

                  valid = False
                  for x in range(width):
                      for y in range(height):
                          pixel = img.getpixel(((o_x * width) + y, (o_y * height) + x))
                          rx, gx, bx = int(pixel[0]), int(pixel[1]), int(pixel[2])
                          if rx or gx or bx:
                              valid = True
                          if rx == 255:
                              rx=r
                          if gx == 255:
                              gx=g
                          if bx == 255:
                              bx=b

                          unicornhathd.set_pixel(x, y, rx, gx, bx)

                  if valid:
                      unicornhathd.show()
                      time.sleep(0.5)

    def showScoreBoard(self, score):

        lines = ["SCORE... ", str(score)]
        colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x / float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]
        width, height = unicornhathd.get_shape()
        text_x = width
        text_y = 2
        font_file, font_size = FONT
        font = ImageFont.truetype(font_file, font_size)
        text_width, text_height = width, 0
        unicornhathd.rotation(-90)
        try:
            for line in lines:
                w, h = font.getsize(line)
                text_width += w + width
                text_height = max(text_height, h)

            text_width += width + text_x + 1

            image = Image.new('RGB', (text_width, max(16, text_height)), (0, 0, 0))
            draw = ImageDraw.Draw(image)

            offset_left = 0

            for index, line in enumerate(lines):
                draw.text((text_x + offset_left, text_y), line, colours[index], font=font)
                offset_left += font.getsize(line)[0] + width

            for scroll in range(text_width - width):
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel((x + scroll, y))
                        r, g, b = [int(n) for n in pixel]
                        unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

                unicornhathd.show()
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("STOP")
        unicornhathd.rotation(0)




    def gameOver(self, score ):
          
          if self.showScore==True:
              self.showScoreBoard(score)
              self.showScore=False

          colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x / float(len(str(score))), 1.0, 1.0)]) for x in range(len(str(score)))]
          self.pulseBrightness()
          width, height = unicornhathd.get_shape()
          text_width, text_height = width, 0


          img = Image.open('assets/gameover1.png')
          draw = ImageDraw.Draw(img)
          display_width,display_height = img.size
          for y in range(display_height):
                    for x in range(display_width):
                        hue = ((time.time() / 10.0) + (x ))
                        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1, self.brightness/20)] 
          for o_x in range(int(img.size[0] / width)):
              for o_y in range(int(img.size[1] / height)):

                  valid = False
                  for x in range(width):
                      for y in range(height):
                          pixel = img.getpixel(((o_x * width) + y, (o_y * height) + x))
                          rx, gx, bx = int(pixel[0]), int(pixel[1]), int(pixel[2])
                          if rx or gx or bx:
                              valid = True
                          if rx == 255:
                              rx=r
                          if gx == 255:
                              gx=g
                          if bx == 255:
                              bx=b

                          unicornhathd.set_pixel(x, y, rx, gx, bx)

                  if valid:
                      unicornhathd.show()
                      time.sleep(0.5)




