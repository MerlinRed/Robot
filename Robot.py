from enum import Enum
from random import choice
from timeit import default_timer


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'


class Robot:

    def __init__(self, finish_x, finish_y):
        self.position_x = choice([x for x in range(-1000, 1000 + 1)])
        self.position_y = choice([y for y in range(-1000, 1000 + 1)])
        self.direction = choice(list(Direction))
        assert isinstance(finish_x, int)
        assert isinstance(finish_y, int)
        self.finish_x = finish_x
        self.finish_y = finish_y

    @property
    def coordinate_finish(self):
        return self.finish_x, self.finish_y

    @property
    def get_direction(self):
        return self.direction

    @property
    def get_self_coordinate(self):
        return self.position_x, self.position_y

    def turn_self(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP

    def step_forward(self):
        if self.direction == Direction.UP:
            self.position_y += 1
        elif self.direction == Direction.LEFT:
            self.position_x -= 1
        elif self.direction == Direction.DOWN:
            self.position_y -= 1
        elif self.direction == Direction.RIGHT:
            self.position_x += 1


def game(*, finish_x, finish_y):
    robot = Robot(finish_x=finish_x, finish_y=-finish_y)
    print(f'My starting coordinates: {robot.get_self_coordinate}')
    print(f'I look {robot.get_direction}')
    print(f'I need to reach the coordinates: {robot.coordinate_finish}')
    while robot.coordinate_finish != robot.get_self_coordinate:

        self_variable = robot.position_x if robot.position_x != robot.finish_x else robot.position_y
        finish_variable = robot.finish_x if robot.position_y != robot.finish_y else robot.finish_y
        direction_x = Direction.LEFT if robot.position_x > robot.finish_x else Direction.RIGHT
        direction_y = Direction.DOWN if robot.position_y > robot.finish_y else Direction.UP
        direction_variable = direction_x if robot.position_x != robot.finish_x else direction_y

        if self_variable > finish_variable:
            while robot.get_direction != direction_variable:
                robot.turn_self()
        else:
            while robot.get_direction != direction_variable:
                robot.turn_self()
        robot.step_forward()

    print(f'I look {robot.get_direction}')
    print(f'Finish coordinates: {robot.coordinate_finish}')


start = default_timer()
game(finish_x=1500, finish_y=-1500)
finish = default_timer()
print(f'I walked for {finish - start: 2f} seconds')
