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
        self.position_x = choice([x for x in range(-100, 100 + 1)])
        self.position_y = choice([y for y in range(-100, 100 + 1)])
        self.direction = choice(list(Direction))
        self.finish_x = int(finish_x)
        self.finish_y = int(finish_y)

    @property
    def coordinate_finish(self):
        return self.finish_x, self.finish_y

    @property
    def get_direction(self):
        return self.direction

    @property
    def get_self_coordinate(self):
        return self.position_x, self.position_y

    def turn_left(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP

    def turn_right(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
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


def game():
    robot = Robot(finish_x=0, finish_y=0)
    print(f'My starting coordinates: {robot.get_self_coordinate}')
    print(f'I look {robot.get_direction}')
    print(f'I need to reach the coordinates: {robot.coordinate_finish}')
    while robot.coordinate_finish != robot.get_self_coordinate:

        while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
            if robot.get_self_coordinate[0] > robot.coordinate_finish[0]:
                while robot.get_direction != Direction.LEFT:
                    robot.turn_left()
            else:
                while robot.get_direction != Direction.RIGHT:
                    robot.turn_left()
            robot.step_forward()

        while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
            if robot.get_self_coordinate[1] > robot.coordinate_finish[1]:
                while robot.get_direction != Direction.DOWN:
                    robot.turn_left()
            else:
                while robot.get_direction != Direction.UP:
                    robot.turn_left()
            robot.step_forward()

    print(f'My coordinates: {robot.get_self_coordinate}')
    print(f'I look {robot.get_direction}')
    print(f'Finish coordinates: {robot.coordinate_finish}')


start = default_timer()
game()
finish = default_timer()
print(f'I walked for {finish - start} seconds')
