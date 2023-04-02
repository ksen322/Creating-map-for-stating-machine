import pygame
from support import draw_tile, draw_text


class Map:
    def __init__(self, tilesize):

        self.screen = pygame.display.get_surface()

        self.tilesize = tilesize

        self.cols = self.screen.get_width() // self.tilesize  # x
        self.rows = self.screen.get_height() // self.tilesize  # y

        self.created_map = self.create_map()
        self.obstacles = self.get_obstacles()

        self.start_pos = None
        self.goal_pos = None

        self.mkeys = None
        self.keys = None

        self.states = ('Setting start postion', 'Setting goal postion', 'Setting obstacles postion')
        self.state = None

    def draw_background(self):

        self.screen.fill('gray')

        for x in range(self.cols):
            if x % 2 == 0:
                for y in range(0, self.rows, 2):
                    draw_tile((x, y), self.tilesize, 'light gray')
            else:
                for y in range(1, self.rows, 2):
                    draw_tile((x, y), self.tilesize, 'light gray')

    def set_start_pos(self):

        cursor_pos = (pygame.mouse.get_pos()[0] // self.tilesize, pygame.mouse.get_pos()[1] // self.tilesize)

        if cursor_pos not in self.obstacles and cursor_pos != self.goal_pos and self.mkeys[0]:
            self.start_pos = cursor_pos

        return self.start_pos

    def draw_start_pos(self):

        if self.start_pos is not None:
            draw_tile(self.start_pos, 20, 'green')

    def set_goal_pos(self):

        cursor_pos = (pygame.mouse.get_pos()[0] // self.tilesize, pygame.mouse.get_pos()[1] // self.tilesize)

        if cursor_pos not in self.obstacles and cursor_pos != self.goal_pos and self.mkeys[0]:
            self.goal_pos = cursor_pos

        return self.goal_pos

    def draw_goal_pos(self):

        if self.goal_pos is not None:
            draw_tile(self.goal_pos, 20, 'red')

    def set_obstacles_pos(self):

        cursor_pos = (pygame.mouse.get_pos()[0] // self.tilesize, pygame.mouse.get_pos()[1] // self.tilesize)

        if cursor_pos not in self.obstacles and cursor_pos != self.goal_pos and cursor_pos != self.goal_pos and self.mkeys[0]:
            self.obstacles.append(cursor_pos)
        elif cursor_pos in self.obstacles and self.mkeys[2]:
            self.obstacles.remove(cursor_pos)

    def create_map(self):

        created_map = []

        for x in range(self.cols):
            row = []
            for y in range(self.rows):
                row.append(0)

            created_map.append(row)

        return created_map

    def get_obstacles(self):

        obstacles = []

        for x in range(self.cols):
            for y in range(self.rows):
                if self.created_map[x][y] == 1:
                    obstacles.append((x, y))

        return obstacles

    def draw_obstacles(self):

        for obstacle_pos in self.obstacles:
            draw_tile(obstacle_pos, self.tilesize, 'blue')

    def state_control(self):

        if self.keys[pygame.K_s]:
            self.state = 'Setting start postion'

        if self.keys[pygame.K_g]:
            self.state = 'Setting goal postion'

        if self.keys[pygame.K_o]:
            self.state = 'Setting obstacles postion'

        if self.state is not None and self.keys[pygame.K_SPACE]:
            self.state = None

    def show(self):

        self.draw_background()
        self.draw_obstacles()
        self.draw_start_pos()
        self.draw_goal_pos()

    def edit(self):

        self.mkeys = pygame.mouse.get_pressed()
        self.keys = pygame.key.get_pressed()

        self.state_control()

        if self.state is not None:
            draw_text(f"State - {self.state}", 'black', (150, 485))

        if self.state == 'Setting start postion':
            self.set_start_pos()

        if self.state == 'Setting goal postion':
            self.set_goal_pos()

        if self.state == 'Setting obstacles postion':
            self.set_obstacles_pos()
