#!/usr/bin/env checkio --domain=py run microwave-ovens
class MicrowaveBase:
    time_to_work = 0

    def set_timer(self, set_time):
        set_time = list(map(int, set_time.split(':')))
        self.time_to_work = set_time[0] * 60 + set_time[1]

    def in_timer(self):
        res = tuple(map(lambda x: str(x).zfill(2), divmod(self.time_to_work, 60)))
        return res

    @staticmethod
    def modify_time(text_time):
        if text_time[-1] == 'm':
            return int(text_time[:-1]) * 60
        return int(text_time[:-1])

    def check_range(self, seconds, positive=True):
        if not positive:
            res = self.time_to_work - seconds
            if res >= 0:
                return seconds
            else:
                return self.time_to_work
        else:
            res = self.time_to_work + seconds
            if 5400 >= res:
                return seconds
            else:
                return 5400 - self.time_to_work

    def add_seconds(self, add_time):
        self.time_to_work += self.check_range(self.modify_time(add_time))

    def del_seconds(self, del_time):
        self.time_to_work -= self.check_range(self.modify_time(del_time), False)


class Microwave1(MicrowaveBase):
    def in_timer(self):
        res = super(Microwave1, self).in_timer()
        return '_' + res[0][1:], res[1]


class Microwave2(MicrowaveBase):
    def in_timer(self):
        res = super(Microwave2, self).in_timer()
        return res[0], res[1][:1] + '_'


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def set_time(self, set_time):
        self.device.set_timer(set_time)

    def add_time(self, set_time):
        self.device.add_seconds(set_time)

    def del_time(self, set_time):
        self.device.del_seconds(set_time)

    def show_time(self):
        return f'{":".join(self.device.in_timer())}'


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("10:00")

    rc_1 = RemoteControl(microwave_1)
    rc_1.set_time("05:33")
    rc_1.del_time("30s")
    rc_1.del_time("2m")
    rc_1.show_time()

    print(rc_1.show_time())

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    remote_control_3.add_time('60s')

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
