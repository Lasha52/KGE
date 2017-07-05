import pygame 
import character
import controls
import objects
import collisions
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('KATABALAXA 0.0.1')

windowclose = False

colmap = collisions.map(WIDTH,HEIGHT)
oboba = character.main(400,0,70,50,WIDTH,HEIGHT)
block1 = objects.block(100,550,90,50,colmap)
block2 = objects.block(150,450,90,50,colmap)
block3 = objects.block(300,300,300,50,colmap)
block4 = objects.block (500,250,200,200,colmap)
abla1 = objects.ablabuda(400,100,10,colmap)
abla2 = objects.ablabuda(100,200,10,colmap)
oboba.animationInit("yle")

while not windowclose:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				windowclose = True
			controls.updateControls(event,oboba)

	
	screen.fill((100,100,100))				
	
	oboba.animate(screen)
	
	oboba.update(colmap)
	
	block4.draw(screen)
	block1.draw(screen)
	block2.draw(screen)
	block3.draw(screen)
	abla1.draw(screen)
	abla2.draw(screen)
	
	pygame.display.update()
	
	clock.tick(300)