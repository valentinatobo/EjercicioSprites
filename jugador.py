import pygame
from pygame.sprite import Sprite
from pygame import *

class Jugador(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.sentido = 0
        self.velocidad = 10
        self.cont = 0
    
    def set_sprites(self, sprites):
        self.imagenes = sprites
        self.image = self.imagenes[self.sentido][0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(32, 32)


    def ubicar(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.image = self.imagenes[self.sentido][0]
        teclas = pygame.key.get_pressed()
        if teclas[K_UP]:
            self.rect.y -= self.velocidad
            self.sentido = 0
        elif teclas[K_DOWN]:
            self.rect.y += self.velocidad
            self.sentido = 1
        if teclas[K_LEFT]:
            self.rect.x -= self.velocidad
            self.sentido = 2
        elif teclas[K_RIGHT]:
            self.rect.x += self.velocidad
            self.sentido = 3
        if teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP] or teclas[K_DOWN]:
            self.image = self.imagenes[self.sentido][self.cont]
            self.cont += 1
            self.cont %= 3

     
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')     
                    
    def draw(self, screen):
        #screen.blit(self.image, self.rect)
        screen.blit(self.image, (50,50))