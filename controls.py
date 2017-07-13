import pygame

def updateControls(event,oboba): 	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			oboba.vx = oboba.moveSpeed
		if event.key == pygame.K_LEFT:
			oboba.vx = - oboba.moveSpeed
		if event.key == pygame.K_SPACE and oboba.isJumping == False:
			oboba.vy = oboba.jumpStrength
			oboba.isJumping = True
		if event.key == pygame.K_UP and oboba.isOnWeb == True:
			oboba.vy = -0.5
		if event.key == pygame.K_DOWN and oboba.isOnWeb == True:
			oboba.vy = 0.5
		if event.key == pygame.K_z:
			oboba.webAdd = True

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT and oboba.vx>0:
			oboba.vx = 0
		if event.key == pygame.K_LEFT and oboba.vx<0:
			oboba.vx = 0
		if event.key == pygame.K_UP and oboba.isOnWeb == True:
			oboba.vy = 0
	
				