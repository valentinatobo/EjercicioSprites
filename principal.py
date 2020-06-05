import sys
import pygame
import util
from constructores import *
from jugador import Jugador

WHITE = (255, 255, 255)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bienvenido Presentación del Personaje")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
director = Director()
director.setBuilder(ConstructorJugador_dos())
jugador = director.getJugador()


def game():
    pygame.init()
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
        #jugador.update()
        #jugador.draw(screen)
                
screen.fill(WHITE)
jugador.update()
jugador.draw(screen)
pygame.display.flip()
clock.tick(30)

if __name__ == '__main__':
    game()