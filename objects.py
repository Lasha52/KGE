import pygame

class block : 
	def __init__(self,x,y,width,height,colmap):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		for i in range(x,x+width):
			for j in range(y,y+height):
				colmap.map[i][j] = 1
	def draw(self,screen):
		pygame.draw.rect(screen,(0,0,255),(self.x,self.y,self.width,self.height))

class  ablabuda:
	width = 30
	height = 30
	def __init__(self,x,y,strength,colmap):
		self.x = x
		self.y = y
		self.strength=strength
		for i in range(x,x+self.width):
			for j in range(y,y+self.height):
				colmap.map[i][j] = strength
	def draw(self,screen):
		pygame.draw.rect(screen,(0,255,0),(self.x,self.y,self.width,self.height))


