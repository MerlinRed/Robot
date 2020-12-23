import timeit


class Robot:

    def __init__(self, position_x, position_y, sight_side, finish_x, finish_y):
        self.position_x = int(position_x)
        self.position_y = int(position_y)
        self.sight_side = str(sight_side).title()
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
    robot = Robot(position_x=65.45, position_y=4, sight_side='lEFT', finish_x=-8, finish_y=10/2)
    sight_side = ['Up', 'Down', 'Left', 'Right']
    print(f'My starting coordinates: {robot.get_self_coordinate}')
    print(f'I need to reach the coordinates: {robot.coordinate_finish}')
    while robot.coordinate_finish != robot.get_self_coordinate:

        if robot.coordinate_finish[0] < 0:
            if robot.get_direction in sight_side:
                if robot.get_self_coordinate[0] > robot.coordinate_finish[0]:
                    while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
                        while robot.get_direction != 'Left':
                            robot.turn_left()
                        robot.step_forward()
                else:
                    while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
                        while robot.get_direction != 'Right':
                            robot.turn_left()
                        robot.step_forward()
        elif robot.coordinate_finish[0] == 0:
            if robot.get_direction in sight_side:
                while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
                    while robot.get_self_coordinate != 'Right' or 'Left':
                        robot.turn_right()
                    if robot.get_direction == 'Right':
                        robot.turn_left()
                        robot.turn_left()
                    elif robot.get_direction == 'Left':
                        robot.turn_right()
                        robot.turn_right()
                    robot.step_forward()
        elif robot.coordinate_finish[0] > 0:
            if robot.get_direction in sight_side:
                if robot.get_self_coordinate[0] > robot.coordinate_finish[0]:
                    while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
                        while robot.get_direction != 'Left':
                            robot.turn_right()
                        robot.step_forward()
                else:
                    while robot.get_self_coordinate[0] != robot.coordinate_finish[0]:
                        while robot.get_direction != 'Right':
                            robot.turn_right()
                        robot.step_forward()

        if robot.coordinate_finish[1] < 0:
            if robot.get_direction in sight_side:
                if robot.get_self_coordinate[1] > robot.coordinate_finish[1]:
                    while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
                        while robot.get_direction != 'Down':
                            robot.turn_left()
                        robot.step_forward()
                else:
                    while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
                        while robot.get_direction != 'Up':
                            robot.turn_left()
                        robot.step_forward()
        elif robot.coordinate_finish[1] == 0:
            if robot.get_direction in sight_side:
                while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
                    while robot.get_direction != 'Up' or 'Down':
                        robot.turn_left()
                    if robot.get_direction == 'Up':
                        robot.turn_left()
                        robot.turn_left()
                    elif robot.get_direction == 'Down':
                        robot.turn_right()
                        robot.turn_right()
                    robot.step_forward()
        elif robot.coordinate_finish[1] > 0:
            if robot.get_direction in sight_side:
                if robot.get_self_coordinate[1] > robot.coordinate_finish[1]:
                    while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
                        while robot.get_direction != 'Down':
                            robot.turn_right()
                        robot.step_forward()
                else:
                    while robot.get_self_coordinate[1] != robot.coordinate_finish[1]:
                        while robot.get_direction != 'Up':
                            robot.turn_right()
                        robot.step_forward()
    print(f'My coordinates: {robot.get_self_coordinate}')
    print(f'Finish coordinates: {robot.coordinate_finish}')


start = timeit.default_timer()
game()
finish = timeit.default_timer()
print(f'I walked for {finish-start} seconds')
