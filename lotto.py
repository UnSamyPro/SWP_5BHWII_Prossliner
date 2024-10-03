import random


def main():
    numbers = list(range(1, 46))
    statistic = {}

    for i in range(1, 46):
        statistic[i] = 0

    for i in range(0, 1000):
        for e in run(numbers):
            statistic[e] = statistic[e] + 1

    print(statistic)


def run(numbers):
    for i in range(0, 5):
        rand_index = random.randint(0, 44 - i)
        rand_element = numbers[rand_index]
        last_element = numbers[len(numbers) - 1 - i]

        numbers[rand_index] = last_element
        numbers[len(numbers) - 1 - i] = rand_element

    return numbers[len(numbers) - 6:len(numbers)]


if __name__ == "__main__":
    main()
