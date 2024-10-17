import random


def main(max_numbers=45, count_per_draw=6, max_draws=1000):
    numbers = [i for i in range(0, max_numbers)]
    statistic = {k: 0 for k in range(0, max_numbers)}

    for _ in range(0, max_draws):
        for num in run(numbers, max_numbers, count_per_draw):
            statistic[num] += 1

    return statistic


def run(numbers, max_numbers, count_per_draw):
    for i in range(0, count_per_draw):
        rand_index = random.randint(0, max_numbers - i)
        numbers[rand_index], numbers[max_numbers - i] = numbers[max_numbers - i], numbers[rand_index]

    return numbers[-count_per_draw:]


if __name__ == "__main__":
    print(main())
