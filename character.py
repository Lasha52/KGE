import pygame
import sys
anmtnFPS = 30
class main :
	vx = 0
	vy = 0
	g = 0.02
	isJumping = False
	moveSpeed = 0.9
	jumpStrength = -3
	i=0
	i10=0
	currentImage=0
	def __init__(self,xcoordinate,ycoordinate,sizex,sizey,screenwidth,screenheight):
		self.x = xcoordinate
		self.y = ycoordinate
		self.width = sizex
		self.height = sizey
		self.HEIGHT = screenheight
		self.WIDTH = screenwidth

	def update(self,colMap):
		self.x+=self.vx
		self.vy+=self.g
		self.y+=self.vy
		if self.y>self.HEIGHT-self.height :
			self.isJumping = False
			self.vy = 0
			self.y = self.HEIGHT-self.height
	
		for i in range(3,self.height-5):
			if colMap.map[int(self.x)][int(self.y)+i] == 1 or colMap.map[int(self.x)+self.width][int(self.y)+i] == 1 :
				self.x = self.x-self.vx
				break
	
		for i in range(3,self.width-5):	
			if colMap.map[int(self.x)+i][int(self.y)] == 1 :
				self.y-=self.vy
				self.vy = 0
				break
	
			if colMap.map[int(self.x)+i][int(self.y)+self.height] == 1 :
				self.y-=self.vy
				self.vy = 0
				self.isJumping = False
				break
	
		# Experimental ablabuda collision		
		for i in range(0,self.width):
			if colMap.map[int(self.x)+i][int(self.y)] > 1 or colMap.map[int(self.x)+i][int(self.y)+self.height] > 1:
				self.vx = self.moveSpeed*(self.vx/abs(self.vx+sys.float_info.epsilon))/10
				self.vy = self.vy/10
				break
	
		for i in range(0,self.height):
			if colMap.map[int(self.x)][int(self.y)+i] > 1 or colMap.map[int(self.x)+self.width][int(self.y)+i] > 1:
				self.vx = self.moveSpeed*(self.vx/abs(self.vx+sys.float_info.epsilon))/10
				self.vy = self.vy/10
				break
			if colMap.map[int(self.x)][int(self.y)+i] > 1 or colMap.map[int(self.x)+self.width][int(self.y)+i] > 1:
				self.vx = self.moveSpeed*(self.vx/abs(self.vx+sys.float_info.epsilon))/10
				self.vy = self.vy/10
				break
	
	# Experimental animation engine, status:in progress
	def animationInit(self,name):
		self.walking = [0]*anmtnFPS
		self.jumping = [0]*anmtnFPS
		self.idle = [0]*anmtnFPS
		for j in range(0,anmtnFPS):
			self.walking[j] = pygame.image.load("animation/"+name+'00'+str((j%100-j%10)//10)+str(j%10)+'.png')
	
	def animate(self,screen):
		if(self.vx!= 0):
			self.i10+=1
			if(self.i10==10):
				self.i10 = 0
				self.i += 1
		if(self.i==anmtnFPS):
			self.i=0
		self.currentImage=self.walking[self.i]
		if(self.vx<0):
			self.currentImage = pygame.transform.flip(self.currentImage,True,False)
		screen.blit(self.currentImage,(self.x,self.y))
		


