import random
import timeit


class Robot:

    def __init__(self, finish_x, finish_y):
        self.position_x = random.choice([x for x in range(-100, 100 + 1)])
        self.position_y = random.choice([y for y in range(-100, 100 + 1)])
        self.sight_side = random.choice(['Up', 'Down', 'Left', 'Right'])
        self.finish_x = int(finish_x)
        self.finish_y = int(finish_y)

    @property
    def coordinate_finish(self):
        return self.finish_x, self.finish_y

    @property
    def get_direction(self):
        return self.sight_side

    @property
    def get_self_coordinate(self):
        return self.position_x, self.position_y

    def turn_left(self):
        if self.sight_side == 'Up':
            self.sight_side = 'Left'
        elif self.sight_side == 'Left':
            self.sight_side = 'Down'
        elif self.sight_side == 'Down':
            self.sight_side = 'Right'
        elif self.sight_side == 'Right':
            self.sight_side = 'Up'

    def turn_right(self):
        if self.sight_side == 'Up':
            self.sight_side = 'Right'
        elif self.sight_side == 'Right':
            self.sight_side = 'Down'
        elif self.sight_side == 'Down':
            self.sight_side = 'Left'
        elif self.sight_side == 'Left':
            self.sight_side = 'Up'

    def step_forward(self):
        if self.sight_side == 'Up':
            self.position_y += 1
        elif self.sight_side == 'Left':
            self.position_x -= 1
        elif self.sight_side == 'Down':
            self.position_y -= 1
        elif self.sight_side == 'Right':
            self.position_x += 1


def game():
    robot = Robot(finish_x=16, finish_y=-78)
    print(f'My starting coordinates: {robot.get_self_coordinate}')
    print(f'I look {robot.get_direction}')
    print(f'I need to reach the coordinates: {robot.coordinate_finish}')
    while robot.coordinate_finish != robot.get_self_coordinate:

        while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
            if robot.get_self_coordinate[0] > robot.coordinate_finish[0]:
                while robot.get_direction != 'Left':
                    robot.turn_left()
            else:
                while robot.get_direction != 'Right':
                    robot.turn_left()
            robot.step_forward()

        while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
            if robot.get_self_coordinate[1] > robot.coordinate_finish[1]:
                while robot.get_direction != 'Down':
                    robot.turn_left()
            else:
                while robot.get_direction != 'Up':
                    robot.turn_left()
            robot.step_forward()

    print(f'My coordinates: {robot.get_self_coordinate}')
    print(f'I look {robot.get_direction}')
    print(f'Finish coordinates: {robot.coordinate_finish}')


start = timeit.default_timer()
game()
finish = timeit.default_timer()
print(f'I walked for {finish - start} seconds')
