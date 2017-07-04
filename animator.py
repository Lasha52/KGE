import pygame

def animationInit(self,name)
	self.frames = []
	self.framesRect = []
	for j in range(0,30):
		self.frames[j] = pygame.image.load(name+str(j)+'.png')
		self.framesRect = self.frames[j].get_rect()
def animate(self,screen):
	self.i10+=1
	if(self.i10==10):
		self.i10 = 0
		self.i += 1
	screen.blit(frames[self.i],self.framesRect[self.i])
	


