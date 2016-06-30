# d for direction
import constants as d
import pygame, sys, os, maze
from pygame.locals import *
class Game_Object(pygame.sprite.Sprite):

    # takes a position in terms of x,y list, speed as int, direction as 0,
    # 90, 180, or 270 degrees, the image, and the screen
    def __init__(self, pos, speed, direction, image, screen):
        self.image, self.rect = image, image.get_rect()
        self.screen = screen
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.image = pygame.transform.rotate(image, direction)

    def update(self):
        return

    def draw(self):
        self.screen.blit(self.image, self.pos)

class Wall(Game_Object):
    
    def __init__(self, pos, speed, direction, image, screen):
        Game_Object.__init__(self, pos, speed, direction, image, screen)

class Destructable_Wall(Game_Object):

    number_of_hits=0
    repairable_wall = False

    def __init__(self, speed, direction, image, screen):
        Game_Object.__init__(self,[0,0],speed,direction,image,screen)

    def hit_wall(self,maze_obj):
        
        for y,row in enumerate(maze_obj.maze_array):
            for x,cell in enumerate(row):
                if (cell == 2 or cell == 8 or cell == 3) and x == (maze_obj.player_coords[0]-1) and y == (maze_obj.player_coords[1]):
                    if cell == 3:
                        repairable_wall = True
                    self.number_of_hits+=1
                    self.change_image(cell,maze_obj,[x,y])
                elif (cell == 2 or cell ==8 or cell == 3) and x == (maze_obj.player_coords[0]+1) and y == (maze_obj.player_coords[1]):
                    if cell == 3:
                        repairable_wall = True
                    self.number_of_hits+=1
                    self.change_image(cell,maze_obj,[x,y])
                elif (cell == 2 or cell == 8 or cell == 3) and x == (maze_obj.player_coords[0]) and y == (maze_obj.player_coords[1]-1):
                    if cell == 3:
                        repairable_wall = True
                    self.number_of_hits+=1
                    self.change_image(cell,maze_obj,[x,y])
                elif (cell == 2 or cell == 8 or cell == 3) and x == (maze_obj.player_coords[0]) and y == (maze_obj.player_coords[1]+1):
                    if cell == 3:
                        repairable_wall = True
                    self.number_of_hits+=1
                    self.change_image(cell,maze_obj,[x,y])

    def change_image(self, cell,maze_obj, pos):
        
        if self.number_of_hits == 1:
            maze_obj.change_array_value(pos, 8)
        elif self.number_of_hits > 1:
            maze_obj.change_array_value(pos, 0)
            self.number_of_hits = 0
            if self.repairable_wall:
                self.repair_wall(maze_obj,pos)

    def repair_wall(self,maze_obj, pos):
        
        num = 0
        while True:
            num+=1
            if num > 999999:
                maze_obj.change_array_value(pos, 3)


    
    
            





                    
