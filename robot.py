import pygame
from support import draw_tile


class Robot:
    def __init__(self, robot_pos, goal_pos, color, states, tilesize):

        self.robot_pos = robot_pos
        self.goal_pos = goal_pos
        self.tilesize = tilesize
        self.color = color
        self.states = states

        self.state = states[0]

        self.screen = pygame.display.get_surface()

    def find_path(self):
        pass
        # self.state = 'Finding path to target'
        #
        # return True

    def move_to_target(self):
        pass
        # self.state = 'Moving to target'
        #
        # return True

    def draw_robot(self):

        draw_tile(self.robot_pos, self.tilesize, self.color)

    def run(self):

        self.draw_robot()

        if self.state == 'Waiting for command':
            self.find_path()
        if self.state == 'Path found':
            self.move_to_target()