import pygame
scale = 4
wallpapers = []

grassBlock = pygame.image.load(r'images\grass\GrassBlock.png')
grassBlock = pygame.transform.rotozoom(grassBlock, 0, scale)
blueRocks = pygame.image.load(r'images\backgrounds\blueRocks.png')
blueRocks = pygame.transform.rotozoom(blueRocks, 0, 0.67)
dirt = pygame.image.load(r'images\dirt\dirt.png')
dirt = pygame.transform.rotozoom(dirt, 0, scale)
wallpapers.append(blueRocks)