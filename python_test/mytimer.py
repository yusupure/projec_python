import time as t


class Mytimer():

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.start = t.localtime()
        print("srat")

    def stop(self):
        self.stop = t.localtime()
        self._calc()
        print("stop")

    def _calc(self):
        self.lasted = []
        self.prompt = "total"
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            self.prompt += str(self.lasted[index])
