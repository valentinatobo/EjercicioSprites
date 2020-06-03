import pygame
pygame.init()

#Colores
black = (0,0,0)
white = (255,255,255)
screen_size = (800,600)


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

	screen.fill(black)

	pygame.display.flip()
	clock.tick(60)
pygame.quit()


