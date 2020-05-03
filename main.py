import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 720
blocks = []
wallpapers = []
game = True

layer = 2
scale = 4
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not really terraria")
Screen.fill((250,250,250))
grassBlock = pygame.image.load(r'images\grass\GrassBlock.png')
grassBlock = pygame.transform.rotozoom(grassBlock, 0, scale)
blueRocks = pygame.image.load(r'images\backgrounds\blueRocks.png')
blueRocks = pygame.transform.rotozoom(blueRocks, 0, 0.67)
dirt = pygame.image.load(r'images\dirt\dirt.png')
dirt = pygame.transform.rotozoom(dirt, 0, scale)
wallpapers.append(blueRocks)

class Block:

    def __init__(self,x,y,type):
        if type == 'grass':
            self.block = grassBlock
        if type == 'dirt':
            self.block = dirt
        self.x = x
        self.y = y

def worldGen():
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

worldGen()
while game == True:
    getEvents()
    displayImage()
