import pygame, sys, os, game_objects, maze
from pygame.locals import *
from maze import *
from game_objects import *
class Game_Runner(object):
    
    def __init__(self, level):
        pygame.init()
        size = [1105,700]
        screen = pygame.display.set_mode(size)
        self.player = Game_Object([0,0], 1, 0, pygame.image.load("arrow.png").convert(), screen)
        self.maze = Maze(level, [50,50], pygame.image.load("walk_1.png").convert()
        ,pygame.image.load("enemy_1.png").convert(),pygame.image.load("brick_tile.png").convert(),
        pygame.image.load("damaged_brick.png").convert(),pygame.image.load("damaged_brick_2.png").convert(),pygame.image.load("gold.png").convert()
        , pygame.image.load("black_square.png").convert())
        self.dest_wall = Destructable_Wall(0, 0,pygame.image.load("damaged_brick_2.png").convert(), screen)
        self.hit_counter = 0
        

    def run(self):
        pygame.init()
        size = [1105,700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Python Game")
        done = False
        clock = pygame.time.Clock()
        self.maze.draw_walls(screen)
        self.maze.add_animations(pygame.image.load("walk_2.png").convert(),pygame.image.load("walk_3.png").convert()
        ,pygame.image.load("enemy_1.png").convert(),pygame.image.load("enemy_1.png").convert())

        while done == False:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
               
            key = pygame.key.get_pressed()
            if key[K_UP]:
                self.maze.move_up(4, [0,0], 5)
            if key[K_DOWN]:
                self.maze.move_down(4, [0,0], 5)
            if key[K_LEFT]:
                self.maze.move_left(4, [0,0], 5)
            if key[K_RIGHT]:
                self.maze.move_right(4, [0,0], 5)
            if key[K_SPACE]:
                self.hit_counter+=1
                if self.hit_counter == 30 :
                    self.dest_wall.hit_wall(self.maze)
                elif self.hit_counter == 60:
                    self.dest_wall.hit_wall(self.maze)
                    self.hit_counter = 0
            if self.maze.has_lost:
                print "YOU LOSE"
                break

            self.maze.update_characters(screen)
            pygame.display.flip() 
        pygame.quit()

        def print_you_win(self):
            text1 = font.render("You win!", True, white)
            screen.blit(text1, [800, 300])






        


