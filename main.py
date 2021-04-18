import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

np.set_printoptions(linewidth=120)
na = np.nan


class Puzzle():
    def __init__(self):
        self.move_1 = 0
        self.move_2 = 0
        self.move_3 = 0

        circle_0 = [23, 19, 3, 2, 3, 27, 20, 11, 27, 10, 19, 10, 13, 10, 2, 15]
        self.circle_0 = np.array(circle_0)

        self.wheel_1 = [17, na, 2, na, 2, na, 10, na, 15, na, 6, na, 9, na, 16, na]
        self.inner_1 = [5, 10, 5, 1, 24, 2, 10, 9, 7, 3, 12, 24, 10, 9, 22, 9]

        self.wheel_2 = [22, na, 2, na, 17, na, 15, na, 14, na, 5, na, 10, na, 2, na]
        self.inner_2 = [14, 5, 5, 7, 8, 24, 8, 3, 6, 15, 22, 6, 1, 1, 11, 27]

        self.inner_3 = [10, 2, 6, 10, 4, 1, 5, 5, 4, 8, 6, 3, 1, 6, 10, 6]
        self.wheel_3 = [13, na, 3, na, 3, na, 6, na, 10, na, 10, na, 10, na, 6, na]


    def get_circle(self, default, wheel):
        wheel = np.array(wheel)
        default = np.array(default)
        circle = np.where(~np.isnan(wheel), wheel, default)
        return circle


    def check_circles(self):
        circle_0 = self.circle_0
        circle_1 = self.get_circle(self.inner_1, self.wheel_1)
        circle_2 = self.get_circle(self.inner_2, self.wheel_2)
        circle_3 = self.get_circle(self.inner_3, self.wheel_3)

        matrix = np.array([circle_0, circle_1, circle_2, circle_3])
        out = np.unique(matrix.sum(0)).shape[0] != 1

        logging.debug(matrix)
        logging.debug(matrix.sum(0))
        logging.debug(out)

        return out

    def rotate_1(self):
        self.wheel_1[:] = np.roll(self.wheel_1, 1)
        self.inner_2[:] = np.roll(self.inner_2, 1)
        self.move_1 += 1

    def rotate_2(self):
        self.wheel_2[:] = np.roll(self.wheel_2, 1)
        self.inner_3[:] = np.roll(self.inner_3, 1)
        self.move_2 += 1

    def rotate_3(self):
        self.wheel_3[:] = np.roll(self.wheel_3, 1)
        self.move_3 += 1

    def find(self):
        loop_num = 0

        while self.check_circles():
            print("loop %s" % loop_num)
            if loop_num > 1024: break

            while self.move_1 < 16:
                self.rotate_1()
                if not self.check_circles(): break

                while self.move_2 < 16:
                    self.rotate_2()
                    if not self.check_circles(): break

                    while self.move_3 < 16:
                        self.rotate_3()
                        if not self.check_circles(): break

                    self.move_3 = 0
                self.move_2 = 0
            self.move_1 = 0

            loop_num += 1


if __name__ == '__main__':
    p = Puzzle()
    p.find()
