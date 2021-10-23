import random

from rrt.env import World
from rrt.robot import Robot, Obstacle


def check_collision(obj0, obj1):
    """
    Check if the obj0 collides with the obj1.
    Return True, if the obj0 collides with obj1,
    Return False, if the obj0 doesn't collide with obj1.
    """
    # student implements it.
    if obj0.coord[0] + obj0.w / 2 < obj1.coord[0] - obj1.w / 2:
        return False
    elif obj0.coord[0] - obj0.w / 2 > obj1.coord[0] + obj1.w / 2:
        return False
    elif obj0.coord[1] + obj0.w / 2 < obj1.coord[1] - obj1.w / 2:
        return False
    elif obj0.coord[1] - obj0.w / 2 > obj1.coord[1] + obj1.w / 2:
        return False
    else:
        return True


def create_random_world():
    """With this function we can create 2 obstacles and 1 robot."""
    # student implements it.
    world = World()
    # sample coord for obs0
    obs0 = Obstacle((200, 200))
    world.add_obs(obs0)
    obs0_low = 0 + obs0.w / 2
    obs0_high = world.w - obs0.w / 2
    obs0.reset_pos((random.randint(obs0_low, obs0_high),
                    random.randint(obs0_low, obs0_high)))
    obs1 = Obstacle((200, 200))
    world.add_obs(obs1)
    obs1_low = 0 + obs1.w / 2
    obs1_high = world.w - obs1.w / 2
    while True:
        obs1.reset_pos((random.randint(obs1_low, obs1_high),
                        random.randint(obs1_low, obs1_high)))
        if not check_collision(obs0, obs1):
            break

    robot = Robot((200, 200))
    world.add_robot(robot)
    robot_low = 0 + robot.w / 2
    robot_high = world.w - robot.w / 2
    while True:
        robot.reset_pos((random.randint(robot_low, robot_high),
                         random.randint(robot_low, robot_high)))
        if not check_collision(robot, obs0) and not check_collision(robot, obs1):
            break
    return world
