
class Road:

    def __init__(self, length, width, weigh, num_m):
        self._length = length
        self._width = width
        self.weigh = weigh
        self.num_m = num_m

    def weight_culculator(self):
        res = self._length * self._width * self.weigh * self.num_m
        if res >= 100 and res < 1000:
            print("{}м * {}м * {}кг * {}м = {}ц".format(self._length, self._width, self.weigh, self.num_m, res / 100))
        elif res >= 1000:
            print("{}м * {}м * {}кг * {}м = {}т".format(self._length, self._width, self.weigh, self.num_m, res / 1000))
        else:
            print("{}м * {}м * {}кг * {}м = {}кг".format(self._length, self._width, self.weigh, self.num_m, res))


if __name__ == '__main__':
    a = Road(20, 5000, 25, 0.05)
    a.weight_culculator()