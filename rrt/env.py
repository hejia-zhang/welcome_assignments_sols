import matplotlib.pyplot as plt
import numpy as np

from rrt.robot import Robot, Obstacle


class World(object):
    def __init__(self, w=400):
        self.w = w  # a world is a square with this width
        self.world_map = np.zeros(shape=(self.w, self.w))  # this is used to just visualize, think it as a white board.
        self.obs_lst = []
        self.robot_lst = []

    def visualize(self):
        """With this function we can print the world with all obstacles and the robot if there is any."""
        # student implements it.
        self.world_map = np.zeros(shape=(self.w, self.w))
        for obs in self.obs_lst:
            obs.draw(self.world_map)
        # robot should be drawn after the obstacles,
        # so we can always see it.
        for robot in self.robot_lst:
            robot.draw(self.world_map)
        plt.matshow(self.world_map)
        plt.show()

    def add_obs(self, obs):
        self.obs_lst.append(obs)

    def add_robot(self, robot):
        self.robot_lst.append(robot)


if __name__ == '__main__':
    world = World()
    obs0 = Obstacle((200, 200))
    world.add_obs(obs0)
    obs1 = Obstacle((65, 340))
    world.add_obs(obs1)
    obs2 = Obstacle((340, 65))
    world.add_obs(obs2)
    robot0 = Robot((100, 100))
    world.add_robot(robot0)
    world.visualize()
    world.visualize()
