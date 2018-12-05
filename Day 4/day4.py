from datetime import datetime, timedelta

class Timetable(object):
    def __init__(self, input:str):
        self.events = []
        with open(input) as f:
            self.events = [self.parse_event(event) for event in f.readlines()]
        self.events.sort()

    def parse_event(self, event:str):
        timestamp = event[1:17]
        event_desc = event[19:]
        return Event(timestamp, event_desc)

    def calculate_events(self):
        guards = dict()
        activeguard = None
        fall_asleep_time = None
        for event in self.events:
            if event.is_change_of_guard():
                guardno = event.get_guard_number()
                if guardno in guards:
                    activeguard = guards[guardno]
                else:
                    guards[guardno] = Guard(guardno)
                    activeguard = guards[guardno]
            else:
                if event.is_fall_asleep():
                    fall_asleep_time = event.timestamp
                elif event.is_wake_up():
                    elapsedtime = event.timestamp - fall_asleep_time
                    elapsedtime_minutes = elapsedtime / timedelta(minutes=1)
                    activeguard.add_sleep(elapsedtime_minutes, fall_asleep_time, event.timestamp)

        for key, value in guards.items():
            print("===GUARD===")
            print(value.id)
            print(value.asleepminutes)
            print(value.max_asleep())

        sleepiest_guard = (max(guards, key=guards.get))
        print("Sleepiest guard:")
        print(guards[sleepiest_guard].id)
        print(guards[sleepiest_guard].asleepminutes)
        print(guards[sleepiest_guard].max_asleep())

        # Part 2
        max_value = 0
        max_guard = 0
        for key, value in guards.items():
            for sleepkey, val in value.asleeptime.items():
                if val > max_value:
                    max_value = val
                    max_guard = guards[key]
        


        print("Most consistent guard:")
        print(max_guard.id)
        print(max_guard.asleepminutes)
        print(max_guard.max_asleep())
            
class Event(object):
    def __init__(self, timestamp, event):
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
        self.event = event[:-1]

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __repr__(self):
        return (str(self.timestamp) + ' ' + self.event)

    def is_change_of_guard(self):
        if "Guard" in self.event:
            return True
        else:
            return False
    
    def is_fall_asleep(self):
        if "asleep" in self.event:
            return True
        else:
            return False

    def is_wake_up(self):
        if "wakes" in self.event:
            return True
        else:
            return False

    def get_guard_number(self):
        event_parts = self.event.split(' ')
        guardnumber = int(event_parts[1].replace('#',''))
        return guardnumber


class Guard(object):
    def __init__(self, identifier:int):
        self.id = identifier
        self.asleepminutes = 0
        self.asleeptime = {}

    def __lt__(self, other):
        return self.asleepminutes < other.asleepminutes

    def add_sleep(self, minutes:int, fall_asleep_time, wakeup_time):
        fat = fall_asleep_time
        wat = wakeup_time
        while fat != wat:
            if fat.time() in self.asleeptime:
                self.asleeptime[fat.time()] += 1
            else:
                self.asleeptime[fat.time()] = 1
            fat += timedelta(minutes=1)

        self.asleepminutes += minutes

    def max_asleep(self):
        try:
            return max(self.asleeptime, key=self.asleeptime.get)
        except ValueError:
            return 0

timetable = Timetable('input.txt')
timetable.calculate_events()