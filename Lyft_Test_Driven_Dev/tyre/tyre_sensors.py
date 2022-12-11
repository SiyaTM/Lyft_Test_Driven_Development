from dataclasses import dataclass, field
import random


@dataclass
class TyreSensors:
    count: int
    sensor_array: int
    value: int
    sum: int = 0

    @property
    def initialize_array(self) -> int:
        # initializing list
        self.sensor_array = [random.randint(1, 5) for _ in range(10)]
        return self.sensor_array

    @property
    def carrigan_tyres(self) -> int:
        initialize_array()

        # initializing k
        k = 0.9

        # using list comprehension
        # to get numbers > k
        self.count = len([i for i in self.sensor_array if i > k])
        return self.count

    @property
    def octoprime_tyres(self) -> int:
        # initialize_array()

        # iterate through the array
        # and add each element to the sum variable
        # one at a time
        for i in self.sensor_array:
            self.sum = sum + i
        return self.sum

        initialize_array()

        n = len(self.sensor_array)

        self.value = octoprime_tyres(self.sensor_array)

        # self.ans = sum(self.sensor_array)

        # self.total = np.sum(array1)

        if self.value:
            return "Octoprime tyres are in need of service"
        else:
            return "Octoprime tyres are in working order"
