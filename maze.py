import pygame, game_objects
import constants as d
from game_objects import *
from pygame.locals import *
from math import fabs

class Maze(object):
    # 0 = blank space, 1 = wall, 2 = destroyable wall 3 = repairable wall
    # 4 = end, 5 = character, 6 = monster, 7 = gold 
    level_one = ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,1,1,1,1,1,1,1,0,0,7,1],
                 [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,1,1,1,5,1,1,1,0,1,0,1],
                 [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
                 [1,0,1,3,1,0,2,2,2,0,1,1,0,1,1],
                 [1,0,6,0,0,0,2,7,2,0,0,6,0,1,1],
                 [1,0,1,3,1,0,2,2,2,0,1,1,0,1,1],
                 [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
                 [1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
                 [1,1,1,0,1,1,1,0,0,0,0,0,1,0,1],
                 [1,1,0,0,0,0,0,0,1,0,1,0,0,0,1],
                 [1,1,0,1,1,1,1,1,1,0,1,1,0,1,1],
                 [1,7,2,0,0,0,0,0,0,2,7,1,0,7,1],
                 [1,1,1,1,1,1,1,1,4,1,1,1,1,1,1])

    level_two = ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,5,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,1,1,1,2,1,1,1,1,1,6,1],
                 [1,0,1,6,0,0,0,0,0,0,0,0,1,0,1],
                 [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
                 [1,0,1,0,1,7,0,0,0,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,2,1,0,1,0,1,0,1],
                 [1,0,1,0,2,0,1,7,1,0,2,0,1,0,1],
                 [1,0,1,0,1,0,1,2,1,0,1,0,1,0,1],
                 [1,0,1,0,1,6,0,0,0,0,1,0,1,0,1],
                 [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
                 [1,0,1,0,0,0,0,0,0,0,0,7,1,0,1],
                 [1,0,1,1,1,1,1,2,1,1,1,1,1,0,1],
                 [1,7,0,0,0,0,0,0,0,0,0,0,0,0,4],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

    level_three=([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,6,3,3,1,0,0,0,0,1,2,6,2,7,1],
                 [1,0,1,3,1,7,1,1,0,1,0,1,1,1,1],
                 [1,0,1,0,1,0,1,0,0,3,0,3,0,0,1],
                 [1,0,1,0,0,0,1,0,1,1,1,1,1,0,1],
                 [1,0,1,1,1,0,1,0,0,0,1,7,1,0,1],
                 [1,0,0,0,1,0,3,0,1,0,1,0,1,0,1],
                 [1,0,1,0,0,0,3,0,1,0,2,0,1,0,1],
                 [1,0,1,1,0,1,1,1,1,0,1,0,0,0,1],
                 [1,0,1,6,0,1,0,2,2,2,1,0,1,0,1],
                 [1,0,1,1,0,1,0,2,7,2,1,0,1,0,1],
                 [1,0,3,0,0,1,0,2,2,2,1,0,1,0,1],
                 [1,0,1,0,1,1,0,2,2,2,2,0,1,0,1],
                 [1,5,2,0,0,0,0,0,0,0,0,0,2,0,1],
                 [1,1,1,4,1,1,1,1,1,1,1,1,1,1,1])

    level_four =([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,7,2,0,0,0,2,0,2,0,0,0,0,0,1],
                 [1,6,1,0,1,0,1,0,1,0,1,3,1,0,1],
                 [1,2,0,0,1,0,1,0,1,0,3,0,0,2,1],
                 [1,0,0,1,1,0,1,0,1,0,1,0,1,6,1],
                 [1,0,0,0,0,0,2,0,2,0,0,0,1,7,1],
                 [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,5,0,0,0,0,0,0,1],
                 [1,2,1,1,1,1,1,3,1,1,1,1,1,2,1],
                 [1,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
                 [1,0,0,0,1,0,1,0,1,0,1,0,1,0,1],
                 [1,0,1,0,0,2,1,0,1,0,0,0,1,0,1],
                 [1,0,1,0,1,6,1,0,1,1,1,0,1,0,1],
                 [1,0,0,0,1,7,1,0,1,7,6,2,0,0,1],
                 [1,1,1,1,1,1,1,4,1,1,1,1,1,1,1])

    # pos_init is the top left corner of maze, first is regular wall, second is repairable wall
    # all positions in the array are turned into nodes
    def __init__(self,  maze_number, pos_init, player, enemy, wall_1, wall_2, wall_3, gold, space):
        self.direction = d.EAST
        self.pos_init = pos_init
        self.maze_number = maze_number
        self.wall_1 = wall_1
        self.wall_1_rect = wall_1.get_rect()
        self.wall_2 = pygame.transform.scale(wall_2, (self.wall_1_rect.width, self.wall_1_rect.height))
        self.wall_3 = pygame.transform.scale(wall_3, (self.wall_1_rect.width, self.wall_1_rect.height))
        self.gold = pygame.transform.scale(gold, (self.wall_1_rect.width, self.wall_1_rect.height))
        self.player = pygame.transform.scale(player, (self.wall_1_rect.width-8, self.wall_1_rect.height-8))
        self.player_2 = self.player
        self.player_3 = self.player
        self.enemy = pygame.transform.scale(enemy, (self.wall_1_rect.width-8, self.wall_1_rect.height-8))
        self.space = pygame.transform.scale(space, (self.wall_1_rect.width, self.wall_1_rect.height))
        if(self.maze_number==1):
            self.maze_array = self.level_one
        elif(self.maze_number==2):
            self.maze_array = self.level_two
        elif(self.maze_number==3):
            self.maze_array = self.level_three
        elif(self.maze_number==4):
            self.maze_array = self.level_four
        self.make_node_list()
        self.gold_counter = 0
        self.ai_list = ([])
        self.has_lost = False
        self.calc_new_path = 0
        self.speed_ai_1 = 2
        self.speed_ai_2 = 2
        self.speed_ai_3 = 2
        self.speed_ai_4 = 2
        
    def add_animations(self, anim_2_player, anim_3_player, anim_2_enemy, anim_3_enemy):
        self.player_2 = pygame.transform.scale(anim_2_player, (self.wall_1_rect.width-8, self.wall_1_rect.height-8))
        self.player_3 = pygame.transform.scale(anim_3_player, (self.wall_1_rect.width-8, self.wall_1_rect.height-8))
        self.enemy_2 = anim_2_enemy
        self.enemy_3 = anim_3_enemy
        self.anim_count_player = 0

    #creates a list, in order 0-224, of nodes for every index in array
    def make_node_list(self):                
        self.node_list = []
        for y in range(15):
            for x, value in enumerate(self.maze_array[y]):
                self.node_list.append(self._Node([x, y], value))
                if value == 5:
                    self.player_coords = [x, y]

    #draws everything except walls based on the array.  The robots and player are drawn last to make sure they are on top
    def update_characters(self, screen):
        pygame.init()
        maze_number = 0
        pos_now = [0,0]
        ai_number = 0
        i = -1
        temp_pos_player = [0,0]
        temp_pos_ai_1 = [0,0]
        temp_pos_ai_2 = [0,0]
        temp_pos_ai_3 = [0,0]
        temp_pos_ai_4 = [0,0]
        calc_path = False
        self.calc_new_path += 1
        if self.calc_new_path % 1 == 0:
            calc_path = True
            self.calc_new_path = 0
        pos_start = self.pos_init
        pos_now[0] = self.pos_init[0]
        pos_now[1] = self.pos_init[1]

        for y, row in enumerate(self.maze_array):
            for x,cell in enumerate(row):
                if cell == 1:
                    pass
                if cell == 0:
                    screen.blit(self.space, pos_now)
                elif cell == 2 or cell == 3:
                    screen.blit(self.wall_2, pos_now)
                elif cell == 7:
                    screen.blit(self.gold, pos_now)
                elif cell == 5:
                        temp_pos_player[0] = pos_now[0]
                        temp_pos_player[1] = pos_now[1]
                        screen.blit(self.space, pos_now)
                elif cell == 6:
                    coords = [x,y]
                    for ai in self.ai_list:
                        if coords == ai.coord:
                            if ai.number == 0:
                                if len(self.get_adjacent_empty_nodes(ai.coord)) > 2:
                                    if calc_path:
                                        in_center = self.node_list[self.get_equiv_list_num(ai.coord)]
                                        if in_center.dir_ai[0] > -4 and in_center.dir_ai[0] < 4 and in_center.dir_ai[1] > -4 and in_center.dir_ai[1] < 4: 
                                            path_finder = self.Pathfinder(self._Node(ai.coord, 6), self.maze_array[:],
                                            self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                                            z = path_finder.calculate_path()
                                            self.ai_list[0] = self.AI_object(ai.coord, self.speed_ai_1, z, ai.number)
                                temp_pos_ai_1[0] = pos_now[0]
                                temp_pos_ai_1[1] = pos_now[1]
                            elif ai.number == 1:
                                if len(self.get_adjacent_empty_nodes(ai.coord)) > 2:
                                    if calc_path:
                                        in_center = self.node_list[self.get_equiv_list_num(ai.coord)]
                                        if in_center.dir_ai_2[0] > -4 and in_center.dir_ai_2[0] < 4 and in_center.dir_ai_2[1] > -4 and in_center.dir_ai_2[1] < 4: 
                                            path_finder = self.Pathfinder(self._Node(ai.coord, 6), self.maze_array[:],
                                            self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                                            z = path_finder.calculate_path()
                                            self.ai_list[1] = self.AI_object(ai.coord, self.speed_ai_2, z, ai.number)
                                temp_pos_ai_2[0] = pos_now[0]
                                temp_pos_ai_2[1] = pos_now[1]
                            elif ai.number == 2:
                                if len(self.get_adjacent_empty_nodes(ai.coord)) > 2:
                                    if calc_path:
                                        in_center = self.node_list[self.get_equiv_list_num(ai.coord)]
                                        if in_center.dir_ai_3[0] > -4 and in_center.dir_ai_3[0] < 4 and in_center.dir_ai_3[1] > -4 and in_center.dir_ai_3[1] < 4: 
                                            path_finder = self.Pathfinder(self._Node(ai.coord, 6), self.maze_array[:],
                                            self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                                            z = path_finder.calculate_path()
                                            self.ai_list[2] = self.AI_object(ai.coord, self.speed_ai_3, z, ai.number)
                                temp_pos_ai_3[0] = pos_now[0]
                                temp_pos_ai_3[1] = pos_now[1]
                            elif ai.number == 3:
                                if len(self.get_adjacent_empty_nodes(ai.coord)) > 2:
                                    if calc_path:
                                        in_center = self.node_list[self.get_equiv_list_num(ai.coord)]
                                        if in_center.dir_ai_4[0] > -4 and in_center.dir_ai_4[0] < 4 and in_center.dir_ai_4[1] > -4 and in_center.dir_ai_4[1] < 4: 
                                            path_finder = self.Pathfinder(self._Node(ai.coord, 6), self.maze_array[:],
                                            self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                                            z = path_finder.calculate_path()
                                            self.ai_list[3] = self.AI_object(ai.coord, self.speed_ai_4, z, ai.number)
                                temp_pos_ai_4[0] = pos_now[0]
                                temp_pos_ai_4[1] = pos_now[1]
                            break
                    screen.blit(self.space, pos_now)
                elif cell == 4:
                    if self.has_won():
                        screen.blit(self.space, pos_now)
                elif cell == 8:
                    screen.blit(self.wall_3, pos_now)
                else:
                    pass
                pos_now[0] += self.wall_1_rect.width
            pos_now[1] += self.wall_1_rect.height
            pos_now[0] = pos_start[0]
        if round(self.anim_count_player, 0) % 3 == 0:
            screen.blit(self.player_3, [temp_pos_player[0] + 5 + self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0], temp_pos_player[1] - self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1]])
        elif round(self.anim_count_player, 0) % 2 == 0:
            screen.blit(self.player_2, [temp_pos_player[0] + 5 + self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0], temp_pos_player[1] - self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1]])
        else:
            screen.blit(self.player, [temp_pos_player[0] + 5 + self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0], temp_pos_player[1] - self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1]])

        screen.blit(self.enemy, [temp_pos_ai_1[0] + 3 + self.node_list[self.get_equiv_list_num(self.ai_list[0].coord)].dir_ai[0], temp_pos_ai_1[1] - self.node_list[self.get_equiv_list_num(self.ai_list[0].coord)].dir_ai[1]])
        if temp_pos_ai_2 != [0,0]:
            screen.blit(self.enemy, [temp_pos_ai_2[0] + 3 + self.node_list[self.get_equiv_list_num(self.ai_list[1].coord)].dir_ai_2[0], temp_pos_ai_2[1] - self.node_list[self.get_equiv_list_num(self.ai_list[1].coord)].dir_ai_2[1]])
        if temp_pos_ai_3 != [0,0]:
            screen.blit(self.enemy, [temp_pos_ai_3[0] + 3 + self.node_list[self.get_equiv_list_num(self.ai_list[2].coord)].dir_ai_3[0], temp_pos_ai_3[1] - self.node_list[self.get_equiv_list_num(self.ai_list[2].coord)].dir_ai_3[1]])
        if temp_pos_ai_4 != [0,0]:
            screen.blit(self.enemy, [temp_pos_ai_4[0] + 3 + self.node_list[self.get_equiv_list_num(self.ai_list[3].coord)].dir_ai_4[0], temp_pos_ai_4[1] - self.node_list[self.get_equiv_list_num(self.ai_list[3].coord)].dir_ai_4[1]])
        direction = self.ai_list[0].direction_to_go()
        if direction == -1:
            if calc_path:
                path_finder = self.Pathfinder(self._Node(self.ai_list[0].coord, 6), self.maze_array[:],
                self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                z = path_finder.calculate_path()
                self.ai_list[0] = self.AI_object(self.ai_list[0].coord, self.speed_ai_1, z, 0)
        if direction == d.NORTH:
            self.move_up(self.ai_list[0].speed, self.ai_list[0], 6)
        if direction == d.SOUTH:
            self.move_down(self.ai_list[0].speed, self.ai_list[0], 6)
        if direction == d.WEST:
            self.move_left(self.ai_list[0].speed, self.ai_list[0], 6)
        if direction == d.EAST:
            self.move_right(self.ai_list[0].speed, self.ai_list[0], 6)
        if len(self.ai_list) > 1:
            direction = self.ai_list[1].direction_to_go()
            if direction == -1:
                if calc_path:
                    path_finder = self.Pathfinder(self._Node(self.ai_list[1].coord, 6), self.maze_array[:],
                    self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                    z = path_finder.calculate_path()
                    self.ai_list[1] = self.AI_object(self.ai_list[1].coord, self.speed_ai_2, z, 1)
            if direction == d.NORTH:
                self.move_up(self.ai_list[1].speed, self.ai_list[1], 6, 1)
            if direction == d.SOUTH:
                self.move_down(self.ai_list[1].speed, self.ai_list[1], 6, 1)
            if direction == d.WEST:
                self.move_left(self.ai_list[1].speed, self.ai_list[1], 6, 1)
            if direction == d.EAST:
                self.move_right(self.ai_list[1].speed, self.ai_list[1], 6, 1)
        if len(self.ai_list) > 2:
            direction = self.ai_list[2].direction_to_go()
            if direction == -1:
                if calc_path:
                    path_finder = self.Pathfinder(self._Node(self.ai_list[2].coord, 6), self.maze_array[:],
                    self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                    z = path_finder.calculate_path()
                    self.ai_list[2] = self.AI_object(self.ai_list[2].coord, self.speed_ai_3, z, 2)
            if direction == d.NORTH:
                self.move_up(self.ai_list[2].speed, self.ai_list[2], 6, 2)
            if direction == d.SOUTH:
                self.move_down(self.ai_list[2].speed, self.ai_list[2], 6, 2)
            if direction == d.WEST:
                self.move_left(self.ai_list[2].speed, self.ai_list[2], 6, 2)
            if direction == d.EAST:
                self.move_right(self.ai_list[2].speed, self.ai_list[2], 6, 2)
        if len(self.ai_list) > 3:
            direction = self.ai_list[3].direction_to_go()
            if direction == -1:
                if calc_path:
                    path_finder = self.Pathfinder(self._Node(self.ai_list[3].coord, 6), self.maze_array[:],
                    self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                    z = path_finder.calculate_path()
                    self.ai_list[3] = self.AI_object(self.ai_list[3].coord, self.speed_ai_4, z, 3)
            if direction == d.NORTH:
                self.move_up(self.ai_list[3].speed, self.ai_list[3], 6, 3)
            if direction == d.SOUTH:
                self.move_down(self.ai_list[3].speed, self.ai_list[3], 6, 3)
            if direction == d.WEST:
                self.move_left(self.ai_list[3].speed, self.ai_list[3], 6, 3)
            if direction == d.EAST:
                self.move_right(self.ai_list[3].speed, self.ai_list[3], 6, 3)
                
    #only draws the walls and should be called once to save processing; also counts gold pieces and initializes ai
    def draw_walls(self, screen):
        pygame.init()
        maze_number = 0
        pos_now = [0,0]
        pos_start = self.pos_init
        pos_now[0] = self.pos_init[0]
        pos_now[1] = self.pos_init[1]
        ai_number = -1

        for y, row in enumerate(self.maze_array):
            for x,cell in enumerate(row):
                if cell == 1 or cell == 4:
                    screen.blit(self.wall_1, pos_now)
                elif cell == 7:
                    self.gold_counter += 1
                elif cell == 6:
                    ai_number += 1
                    path_finder = self.Pathfinder(self._Node([x, y], 6), self.maze_array[:],
                    self.node_list[:], self.node_list[self.get_equiv_list_num(self.player_coords)])
                    z = path_finder.calculate_path()
                    self.ai_list.append(self.AI_object([x,y], 2, z, ai_number))
                else:
                    pass
                pos_now[0] += self.wall_1_rect.width
            pos_now[1] += self.wall_1_rect.height
            pos_now[0] = pos_start[0]

    #moves the thing up by the distance; coords refer to the ai's coords if the type_of_character is not 5
    def move_up(self, distance, ai_object, type_of_character, ai_number = 0):
        if type_of_character == 5:
            if self.can_move_up(self.player_coords, 5):
                self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] += distance
                move = self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player
                if move[1] > 20:
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] = 0 
                    self.player_coords[1] -= 1
                    if self.maze_array[self.player_coords[1]][self.player_coords[0]] == 7:
                        self.gold_counter -= 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 5
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] = -10
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 5
            else:
                self.node_list[self.player_coords[1]*15 + self.player_coords[0]].dir_player[1] = -4
                return
            self.anim_count_player += .25
        else:
            if ai_number == 0:
                if self.can_move_up(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai
                    if move[1] > 25:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = 0
                        self.ai_list[0].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = 0
                        ai_object.coord[1] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = -6
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6

                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai[1] = -1
                    return
            elif ai_number == 1:
                if self.can_move_up(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2
                    if move[1] > 25:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = 0
                        self.ai_list[1].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = 0
                        ai_object.coord[1] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = -6
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                    
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_2[1] = -1
                    return
            elif ai_number == 2:
                if self.can_move_up(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3
                    if move[1] > 25:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = 0
                        self.ai_list[2].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = 0
                        ai_object.coord[1] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = -6
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                    
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_3[1] = -1
                    return
            elif ai_number == 3:
                if self.can_move_up(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4
                    if move[1] > 25:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = 0
                        self.ai_list[3].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = 0
                        ai_object.coord[1] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = -6
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_4[1] = -1
                    return
            
    #moves the thing down by the distance; coords refer to the ai's coords if the type_of_character is not 5
    def move_down(self, distance, ai_object, type_of_character, ai_number = 0):
        if type_of_character == 5:
            if self.can_move_down(self.player_coords, 5):
                self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] -= distance
                move = self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player
                if move[1] < -20:
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] = 0 
                    self.player_coords[1] += 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 5
                    if self.maze_array[self.player_coords[1]][self.player_coords[0]] == 7:
                        self.gold_counter -= 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] = 10
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 5
            else:
                self.node_list[self.player_coords[1]*15 + self.player_coords[0]].dir_player[1] = -4
                return
            self.anim_count_player += .25
        else:
            if ai_number == 0:
                if self.can_move_down(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai
                    if move[1] < -33:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = 0
                        self.ai_list[0].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = 0
                        ai_object.coord[1] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6

                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai[1] = -1
                    return
            if ai_number == 1:
                if self.can_move_down(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2
                    if move[1] < -33:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = 0
                        self.ai_list[1].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = 0
                        ai_object.coord[1] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6                   
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_2[1] = -1
                    return
            if ai_number == 2:
                if self.can_move_down(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3
                    if move[1] < -33:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = 0
                        self.ai_list[2].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = 0
                        ai_object.coord[1] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6                   
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_3[1] = -1
                    return
            if ai_number == 3:
                if self.can_move_down(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4
                    if move[1] < -33:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = 0
                        self.ai_list[3].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = 0
                        ai_object.coord[1] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6                   
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_4[1] = -1
                    return
            
    #moves the thing left by the distance; coords refer to the ai's coords if the type_of_character is not 5
    def move_left(self, distance, ai_object, type_of_character, ai_number = 0):
        if type_of_character == 5:
            if self.direction == d.EAST:
                self.player = pygame.transform.flip(self.player, 1, 0)
                self.player_2 = pygame.transform.flip(self.player_2, 1, 0)
                self.player_3 = pygame.transform.flip(self.player_3, 1, 0)
                self.direction = d.WEST
            if self.can_move_left(self.player_coords, 5):               
                self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] -= distance
                move = self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player
                if move[0] < -20:
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] = 0 
                    self.player_coords[0] -= 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 5
                    if self.maze_array[self.player_coords[1]][self.player_coords[0]] == 7:
                        self.gold_counter -= 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] = 8
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 5

            else:
                self.node_list[self.player_coords[1]*15 + self.player_coords[0]].dir_player[0] = -2
                return
            self.anim_count_player += .25
        else:
            if ai_number == 0:
                if self.can_move_left(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai
                    if move[0] < -30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = 0
                        self.ai_list[0].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = 0
                        ai_object.coord[0] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = 2
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai[0] = 3
                    return
            elif ai_number == 1:
                if self.can_move_left(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2
                    if move[0] < -30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = 0
                        self.ai_list[1].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = 0
                        ai_object.coord[0] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = 2
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_2[0] = 3
                    return
            elif ai_number == 2:
                if self.can_move_left(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3
                    if move[0] < -30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = 0
                        self.ai_list[2].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = 0
                        ai_object.coord[0] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = 2
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_3[0] = 3
                    return
            elif ai_number == 3:
                if self.can_move_left(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] -= distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4
                    if move[0] < -30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = 0
                        self.ai_list[3].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = 0
                        ai_object.coord[0] -=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = 2
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_4[0] = 3
                    return
            
    #moves the thing up by the distance; coords refer to the ai's coords if the type_of_character is not 5
    def move_right(self, distance, ai_object, type_of_character, ai_number = 0):
        if type_of_character == 5:
            if self.direction == d.WEST:
                self.player = pygame.transform.flip(self.player, 1, 0)
                self.player_2 = pygame.transform.flip(self.player_2, 1, 0)
                self.player_3 = pygame.transform.flip(self.player_3, 1, 0)
                self.direction = d.EAST
            if self.can_move_right(self.player_coords, 5):
                self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] += distance
                move = self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player
                if move[0] > 20:
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 0
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] = 0 
                    self.player_coords[0] += 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].value = 5
                    if self.maze_array[self.player_coords[1]][self.player_coords[0]] == 7:
                        self.gold_counter -= 1
                    self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] = -10
                    self.maze_array[self.player_coords[1]][self.player_coords[0]] = 5
            else:
                self.node_list[self.player_coords[1]*15 + self.player_coords[0]].dir_player[0] = 1
                return
            self.anim_count_player += .25
        else:
            if ai_number == 0:
                if self.can_move_right(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai
                    if move[0] > 30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[1] = 0
                        self.ai_list[0].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = 0
                        ai_object.coord[0] += 1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai[0] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6

                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai[0] = 0
                    return
            if ai_number == 1:
                 if self.can_move_right(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2
                    if move[0] > 30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[1] = 0
                        self.ai_list[1].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = 0
                        ai_object.coord[0] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_2[0] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                 else:       
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_2[0] = 0
                    return
            if ai_number == 2:
                if self.can_move_right(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3
                    if move[0] > 30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[1] = 0
                        self.ai_list[2].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = 0
                        ai_object.coord[0] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_3[0] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_3[0] = 0
                    return
            if ai_number == 3:
                if self.can_move_right(ai_object.coord, 6):
                    self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] += distance
                    move = self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4
                    if move[0] > 30:
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[1] = 0
                        self.ai_list[3].path.pop(0)
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 0
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = 0
                        ai_object.coord[0] +=  1
                        if self.maze_array[ai_object.coord[1]][ai_object.coord[0]] == 5:
                            self.has_lost = True
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].value = 6
                        self.node_list[self.get_equiv_list_num(ai_object.coord)].dir_ai_4[0] = -1
                        self.maze_array[ai_object.coord[1]][ai_object.coord[0]] = 6
                else:
                    self.node_list[ai_object.coord[1]*15 + ai_object.coord[0]].dir_ai_4[0] = 0
                    return

    #checks if the square above is a wall or ai; additionally unit must be close to centered to move up
    def can_move_up(self, coords, type_of_character):
        one_above_num = self.get_equiv_list_num([coords[0], coords[1] - 1])
        above_value = self.node_list[one_above_num].value

        if type_of_character == 6:
            if above_value == 1 or above_value == 2 or above_value == 3 or above_value == 6 or above_value == 8:
                return False
            return True
        if self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] > 4:
            return False
        if self.node_list[one_above_num + 15].dir_player[1] < -9 and coords == self.player_coords:
            return True
        elif self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] < -4:
            return False
        elif above_value == 1 or above_value == 2 or above_value == 3 or above_value == 6 or above_value == 8:
            return False
        else:
            return True

    def can_move_down(self, coords, type_of_character):
        one_below_num = self.get_equiv_list_num([coords[0], coords[1] + 1])
        below_value = self.node_list[one_below_num].value
        
        if type_of_character == 6:
            if below_value == 1 or below_value == 2 or below_value == 3 or below_value == 6 or below_value == 8:
                return False
            return True
        if self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] > 4:
            return False
        elif self.node_list[one_below_num - 15].dir_player[1] > 2 and coords == self.player_coords:
            return True
        elif self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[0] < -4:
            return False
        elif below_value == 1 or below_value == 2 or below_value == 3 or below_value == 6 or below_value == 8:
            return False
        else:
            return True

    def can_move_left(self, coords, type_of_character):
        one_left_num = self.get_equiv_list_num([coords[0] - 1, coords[1]])
        left_value = self.node_list[one_left_num].value

        if type_of_character == 6:
            if left_value == 1 or left_value == 2 or left_value == 3 or left_value == 6 or left_value == 8:
                return False
            return True
        if self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] > 2:
            return False
        elif self.node_list[one_left_num + 1].dir_player[0] > 4 and coords == self.player_coords:
            return True
        elif self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] < -6:
            return False
        elif left_value == 1 or left_value == 2 or left_value == 3 or left_value == 6 or left_value == 8:
            return False
        else:
            return True

    def can_move_right(self, coords, type_of_character):
        one_right_num = self.get_equiv_list_num([coords[0] + 1, coords[1]])
        right_value = self.node_list[one_right_num].value
        
        if type_of_character == 6:
            if right_value == 1 or right_value == 2 or right_value == 3 or right_value == 6 or right_value == 8:
                return False
            return True
        elif self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] > 2:
            return False
        elif self.node_list[one_right_num - 1].dir_player[0] < -4 and coords == self.player_coords:
            return True
        elif self.node_list[self.get_equiv_list_num(self.player_coords)].dir_player[1] < -6:
            return False
        elif right_value == 1 or right_value == 2 or right_value == 3 or right_value == 6 or right_value == 8:
            return False
        else:
            return True

    def get_adjacent_empty_nodes(self, coords):
        adjacent_empty = ([])
        right_node = self.node_list[coords[1] * 15 + coords[0] + 1]
        left_node = self.node_list[coords[1] * 15 + coords[0] - 1]
        above_node = self.node_list[coords[1] * 15 + coords[0] - 15]
        below_node = self.node_list[coords[1] * 15 + coords[0] + 15]
        if right_node.value != 1 and right_node.value != 2 and right_node.value != 3:
            adjacent_empty.append(right_node)
        if left_node.value != 1 and left_node.value != 2 and left_node.value != 3:
            adjacent_empty.append(left_node)
        if above_node.value != 1 and above_node.value != 2 and above_node.value != 3:
            adjacent_empty.append(above_node)
        if below_node.value != 1 and below_node.value != 2 and below_node.value != 3:
            adjacent_empty.append(below_node)
        return adjacent_empty

    def get_equiv_list_num(self, coords):
        return coords[1]*15 + coords[0]

    def has_won(self):
        return self.gold_counter == 0

    def change_array_value(self, pos, num):
        self.maze_array[pos[1]][pos[0]] = num
        self.node_list[self.get_equiv_list_num(pos)].value = num
        
    class _Node(object):
        def __init__(self, coord, value, g_cost = 0, h_cost = 0, f_cost= 0, pred= None, direction_amount_player = [0,0], direction_amount_ai_1 = [0,0], direction_amount_ai_2 = [0,0], direction_amount_ai_3 = [0,0], direction_amount_ai_4 = [0,0]):
            self.coord = coord
            self.value = value
            self.g_cost = g_cost
            self.h_cost = h_cost
            self.f_cost = f_cost
            self.pred = pred
            self.dir_player = direction_amount_player
            self.dir_ai = direction_amount_ai_1
            self.dir_ai_2 = direction_amount_ai_2
            self.dir_ai_3 = direction_amount_ai_3
            self.dir_ai_4 = direction_amount_ai_4

        def compute_g_cost(self, current_path_g_cost):
            self.g_cost = current_path_g_cost + 1
            return self.g_cost
        def compute_h_cost(self, goal_node):
            self.h_cost = fabs(self.coord[0] - goal_node.coord[0]) + fabs(self.coord[1] - goal_node.coord[1])
            return self.h_cost
        def compute_f_cost(self):
            self.f_cost = self.g_cost + self.h_cost
            return self.f_cost
        
    class Pathfinder(object):
        def __init__(self, ai_node, maze, node_list, goal_node):
            self.ai_node = ai_node
            self.maze_array = maze
            self.node_list = node_list
            self.goal_node = goal_node
            self.node_list[self.ai_node.coord[1] * 15 + self.ai_node.coord[0]] = self.ai_node

        def calculate_path(self):
            open_list = set()
            closed_list = ([self.ai_node])
            max_tries = 0
            current = self.ai_node
            
            while max_tries < 50:
                right_node = self.node_list[current.coord[1] * 15 + current.coord[0] + 1]
                left_node = self.node_list[current.coord[1] * 15 + current.coord[0] - 1]
                above_node = self.node_list[current.coord[1] * 15 + current.coord[0] - 15]
                below_node = self.node_list[current.coord[1] * 15 + current.coord[0] + 15]
                if right_node.value != 1 and right_node.value != 2 and right_node.value != 3 and right_node.value != 4 and right_node.value != 6 and right_node.value != 7 and right_node.value != 8 and right_node not in open_list and right_node not in closed_list:
                    right_node.compute_g_cost(current.g_cost)
                    right_node.compute_h_cost(self.goal_node)
                    right_node.compute_f_cost()
                    right_node.pred = current
                    open_list.add(right_node)
                if left_node.value != 1 and left_node.value != 2 and left_node.value != 3 and left_node.value != 4 and left_node.value != 6 and left_node.value != 7 and left_node.value != 8 and left_node not in open_list and left_node not in closed_list:
                    left_node.compute_g_cost(current.g_cost)
                    left_node.compute_h_cost(self.goal_node)
                    left_node.compute_f_cost()
                    left_node.pred = current
                    open_list.add(left_node)
                if above_node.value != 1 and above_node.value != 2 and above_node.value != 3 and above_node.value != 4 and above_node.value != 6 and above_node.value != 7 and above_node.value != 8 and above_node not in open_list and above_node not in closed_list:
                    above_node.compute_g_cost(current.g_cost)
                    above_node.compute_h_cost(self.goal_node)
                    above_node.compute_f_cost()
                    above_node.pred = current
                    open_list.add(above_node)
                if below_node.value != 1 and below_node.value != 2 and below_node.value != 3 and below_node.value != 4 and below_node.value != 6 and below_node.value != 7 and below_node.value != 8 and below_node not in open_list and below_node not in closed_list:
                    below_node.compute_g_cost(current.g_cost)
                    below_node.compute_h_cost(self.goal_node)
                    below_node.compute_f_cost()
                    below_node.pred = current
                    open_list.add(below_node)
                if len(open_list) == 0:
                    return
                current_lowest = open_list.pop()
                open_list.add(current_lowest)
                for nodes in open_list:
                    if nodes.f_cost < current_lowest.f_cost:
                        current_lowest = nodes
                open_list.remove(current_lowest)
                closed_list.append(current_lowest)
                current = current_lowest
                if current.coord == self.goal_node.coord:
                    self.goal_node = current
                    break
                max_tries += 1
            if max_tries == 40:
                return []
            path = []
            while current.coord != self.ai_node.coord:
                path.append(current)
                current = current.pred
            path.reverse()
            return path
    
    class AI_object(object):
        def __init__(self, coord, speed, path, number):
            self.coord = coord
            self.speed = speed
            self.path = path
            self.number = number

        def direction_to_go(self):
            if self.path == None or len(self.path) == 0:
                return -1
            if self.coord[0] < self.path[0].coord[0]:
                return d.EAST
            if self.coord[0] > self.path[0].coord[0]:
                return d.WEST
            if self.coord[1] < self.path[0].coord[1]:
                return d.SOUTH
            if self.coord[1] > self.path[0].coord[1]:
                return d.NORTH
            













    
