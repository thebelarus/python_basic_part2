import random


class KillError(Exception):
    name = 'Kill error exception'


class DrunkError(Exception):
    name = 'Drunk error exception'


class CarCrashError(Exception):
    name = 'Car crash error exception'


class GluttonyError(Exception):
    name = 'Gluttony error exception'


class DepressionError(Exception):
    name = 'Depression error exception'


def one_day():
    exceptions = [
        KillError,
        DrunkError,
        CarCrashError,
        GluttonyError,
        DepressionError,
    ]
    karma_random = random.randint(1, 7)
    exception_present = 1 == random.randint(1, 10)
    if exception_present:
        exception_num = random.randint(0, len(exceptions) - 1)
        raise exceptions[exception_num]
    return karma_random


def main():
    karma_goal = 500
    karma_current = 0
    while karma_current < karma_goal:
        try:
            day_karma_result = one_day()
            karma_current += day_karma_result
        except (
                KillError,
                DrunkError,
                CarCrashError,
                GluttonyError,
                DepressionError) as error:
            with open('karma.log', 'a', encoding='utf8') as file:
                file.write(f'{error.name}\n')
    print('Цель достигнута!')


if __name__ == '__main__':
    main()
