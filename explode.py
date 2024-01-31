
class explodeAnimation: 

	def explodeAnimation(self):
		draw = ImageDraw.Draw(self.image) 
		draw.point((int(self.screenWidth/2), int(self.screenHeight/2)), fill="red") 
		for x in self.circle((self.screenWidth/3)): 
				xx = self.screenWidth/2 - x[0];
				xy = self.screenHeight/2 - x[1];
				draw.point([xx,xy-1], fill="white") 


	def circle(self,r,n=12):
			return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]



