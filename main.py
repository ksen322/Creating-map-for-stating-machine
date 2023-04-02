import sys
import pygame
from map import Map
from robot import Robot

FPS = 60


class App:
    def __init__(self, screen_resolution, tilesize):

        # PYGAME SETUP
        pygame.init()
        pygame.display.set_caption('State Machine')
        self.clock = pygame.time.Clock()

        self.tilesize = tilesize
        self.screen_resolution = screen_resolution

        self.screen = pygame.display.set_mode(self.screen_resolution)

        self.keys = None

        self.app_state = 'Creating map'

        self.map = Map(self.tilesize)

        self.robots = None

        self.creating_robots = False
        self.robot_states = ('Waiting for command', 'Finding path to target', 'Path founded' 'Moving to target',
                             'Completed')
        self.robot_current_states = {}

    def robots_created(self):

        if not self.creating_robots:

            self.robots = [
                Robot((self.map.start_pos[0] + 1, self.map.start_pos[1]), self.map.goal_pos, '#FF1493',
                      self.robot_states, self.tilesize),
                Robot((self.map.start_pos[0] - 1, self.map.start_pos[1]), self.map.goal_pos, '#8A2BE2',
                      self.robot_states, self.tilesize),
                Robot((self.map.start_pos[0], self.map.start_pos[1] + 1), self.map.goal_pos, '#8B008B',
                      self.robot_states, self.tilesize)
        ]

            for robot in self.robots:
                self.robot_current_states[robot] = robot.state

            self.creating_robots = True

        return self.creating_robots

    def app_state_control(self):

        if self.keys[pygame.K_w]:
            self.app_state = 'Simulating work'

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.keys = pygame.key.get_pressed()

            self.app_state_control()
            self.map.show()

            if self.app_state == 'Creating map':
                self.map.edit()

            if self.app_state == 'Simulating work':

                if self.robots_created():

                    for robot in self.robots:
                        robot.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App(screen_resolution=(500, 500), tilesize=20)
    app.run()
