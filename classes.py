import pygame

class Block:

    def __init__(self,x,y):
        self.block = pygame.image.load(r'images\GrassBlock.png')
        self.x = x
        self.y = y