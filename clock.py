import time

class LambertClock:
    def __init__(self, id, history_file):
        self.id = id
        self.time = 0
        self.history_file = history_file
        self.logical_clock = "logical_time"
        with open(self.history_file, "w") as f:
            f.write(f"{self.id},{self.logical_clock}\n")

    def tick(self):
        self.time += 1
        with open(self.history_file, "a") as f:
            f.write(f"{self.id},{self.time}\n")

    def merge(self, other):
        if self.time < other.time:
            self.time = other.time + 1
        elif self.time == other.time and self.id < other.id:
            self.time += 1
        with open(self.history_file, "a") as f:
            f.write(f"{self.id},{self.time}\n")

    def __str__(self):
        with open(self.history_file, "r") as f:
            history = [tuple(line.strip().split(",")) for line in f]
        return f"LambertClock(id={self.id}, time={self.time}, history={history})"


# clock1 = LambertClock("A", "clock1_history.csv")
# clock2 = LambertClock("B", "clock2_history.csv")


# print(clock1)  # Output: LambertClock(id=A, time=2, history=[('A', '0'), ('A', '1'), ('A', '2')])
# print(clock2) 
# # Tick clock1 a few times
# clock1.tick()
# clock1.tick()
# clock1.tick()


# # Merge clock2 with clock1
# clock2.merge(clock1)

# # Print the clocks
# print(clock1)  # Output: LambertClock(id=A, time=2, history=[('A', '0'), ('A', '1'), ('A', '2')])
# print(clock2) 