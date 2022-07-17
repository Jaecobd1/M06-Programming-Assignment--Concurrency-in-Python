# 13
import random
import multiprocessing
import time

print("13:")
with open('today.txt') as f:
    date = f.readlines()
    print(date)

print("15:")
# 15


def test():
    _time = random.uniform(0, 1)
    time.sleep(_time)
    print(f"Wait time: {_time}")
    print(date)


if __name__ == "__main__":
    #     first(random.uniform(0,1))
    #     second(random.uniform(0,1))
    #     third(random.uniform(0,1))

    for n in range(3):
        p = multiprocessing.Process(
            target=test)
        p.start()
