
class Fabric(object):
    def __init__(self, reservations:str, width:int=1000, height:int=1000):
        self.width = width
        self.height = height

        self.fabric = [[0 for i in range(self.width)] for j in range(self.height)]
        self.reservations = open(reservations).readlines()

    def parse_reservation(self, reservation):
        output = reservation.split(' ')
        index = int(output[0].replace('#',''))
        loc = output[2].replace(':','').split(',')
        size = output[3].replace('\n','').split('x')
        loc_x = int(loc[0])
        loc_y = int(loc[1])
        size_x = int(size[0])
        size_y = int(size[1])

        return index, loc_x, loc_y, size_x, size_y

    def mark_reservation(self, index, loc_x, loc_y, size_x, size_y):
        for y in range(loc_y, loc_y+size_y):
            for x in range(loc_x, loc_x+size_x):
                if self.fabric[y][x] != 0:
                    self.fabric[y][x] = 'X'
                else: self.fabric[y][x] = index

    def run_reservations(self):
        for reservation in self.reservations:
            self.mark_reservation(*self.parse_reservation(reservation))

    def count_overlap(self):
        return sum([i.count('X') for i in self.fabric])

    def check_reservation(self, index, loc_x, loc_y, size_x, size_y):
        is_broken = False
        for y in range(loc_y, loc_y+size_y):
            for x in range(loc_x, loc_x+size_x):
                if self.fabric[y][x] == 'X':
                    is_broken = True
        if not is_broken:
            print(index)

    def run_check(self):
        for reservation in self.reservations:
            self.check_reservation(*self.parse_reservation(reservation))




fabric = Fabric('input.txt')

fabric.run_reservations()
print(fabric.count_overlap())
fabric.run_check()