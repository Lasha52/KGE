import pygame
import sys

anmtnFPS = 20

class main :
	vx = 0
	vy = 0
	g = 0.02
	isJumping = False
	isOnWeb = False
	moveSpeed = 0.9
	jumpStrength = -3
	webAdd = False
	webCount = 0 
	# animation variables
	i = 1
	i10 = 1
	currentImage = 0
	flipState = 0
	# 
	def __init__(self,x,y,width,height,WIDTH,HEIGHT):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT

	def update(self,colMap):
		print(self.isOnWeb)

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
			if colMap.map[int(self.x)+i][int(self.y)] == 2 or colMap.map[int(self.x)+i][int(self.y)+self.height] == 2:
				self.vx = self.moveSpeed*(self.vx/abs(self.vx+sys.float_info.epsilon))/10
				self.vy = self.vy/10
				break
	
		for i in range(0,self.height):
			if colMap.map[int(self.x)][int(self.y)+i] == 2 or colMap.map[int(self.x)+self.width][int(self.y)+i] == 2:
				self.vx = self.moveSpeed*(self.vx/abs(self.vx+sys.float_info.epsilon))/10
				self.vy = self.vy/10
				break
		


		#experimental web collision
		self.isOnWeb = False
		self.g = 0.02
		for i in range(0,self.width):
			if colMap.map[int(self.x)+i][int(self.y)] == 3 or colMap.map[int(self.x)+i][int(self.y)+self.height] == 3:
				self.isOnWeb = True
				self.g = 0 

					

	# Experimental animation engine, status:in progress
	def animationInit(self,name):
		self.walking = [0]*anmtnFPS
		self.jumping = [0]*anmtnFPS
		self.idle = [0]*anmtnFPS
		for j in range(1,anmtnFPS):
			self.currentImage = pygame.image.load("animation/"+name+'00'+str((j%100-j%10)//10)+str(j%10)+'.png')
			self.walking[j] = pygame.transform.scale(self.currentImage,(self.width,self.height))
			
	def animate(self,screen):
		if(self.vx != 0):
			self.i10 += 1
			if(self.i10 == 5):
				self.i10 = 0
				self.i += 1
		if(self.i == anmtnFPS):
			self.i = 1
		self.currentImage = self.walking[self.i]
		if(self.vx < 0):
			self.flipState = -1
		if(self.vx > 0):
			self.flipState = 1
		if(self.flipState < 0):	
			self.currentImage = pygame.transform.flip(self.currentImage,True,False)
		screen.blit(self.currentImage,(self.x,self.y))
		# if self.flipState*self.vx < 0:
		# 	self.flipState = self.vx
		# 	for i in range(0,anmtnFPS):
		# 		pygame.transform.flip(self.walking[i],True,True)
		


