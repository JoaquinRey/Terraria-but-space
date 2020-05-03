import pygame
from models import *

pygame.init()
WIDTH = 1280
HEIGHT = 720
blocks = []
game = True

layer = 2
scale = 4
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not really terraria")
Screen.fill((250,250,250))


class Block:

    def __init__(self,x,y,type):
        if type == 'grass':
            self.block = grassBlock
        if type == 'dirt':
            self.block = dirt
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x,self.y,10*scale,10*scale)

def worldGenV1():
    for i in range(int(WIDTH / (10 * scale))):
        blocks.append(Block(i*(10*scale),HEIGHT-((10*scale)*layer),('grass')))
    for i in range(int(WIDTH / (10 * scale))):
        blocks.append(Block(i*(10*scale),HEIGHT-((10*scale)*(layer-1)),('dirt')))

def displayImage():
    pygame.event.pump()
    for wallpaper in wallpapers:
        Screen.blit(wallpaper,(0,0))
    for block in blocks:
        Screen.blit(block.block,(block.x,block.y))
    pygame.display.update()

def getEvents():
    global game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False

def worldGen(size):
    blanks = '[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]'
    with open("worldGen.txt","a") as f:
        print('works')
        if size == 'small':
            f.write(f'world = [')
            for i in range(20):
                if i == 0:
                    f.write(f'{blanks},\n')
                if i < 19 and i > 0:
                    f.write(f'        {blanks},\n')
                if i == 19:
                    f.write(f'        {blanks}]')
            f.close()
    

if __name__ == '__main__':
    worldGenV1()
    worldGen('small')
    while game == True:
        getEvents()
        displayImage()
