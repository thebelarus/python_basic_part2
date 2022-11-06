import random


def generate_team(size=20):
    return [round(random.uniform(5, 10), 2) for _ in range(size)]


def compare_two_teams(team_1, team_2):
    if len(team_1) != len(team_2):
        return ValueError('Списки имеют разные размеры.')
    return [team_1[enum] if team_1[enum] > team_2[enum]
            else team_2[enum] for enum in range(len(team_1))]


if __name__ == '__main__':
    first_team = generate_team()
    second_team = generate_team()
    compared_teams = compare_two_teams(first_team, second_team)
    print(f'Первая команда: {first_team}')
    print(f'Вторая команда: {second_team}')
    print(f'Победители тура: {compared_teams}')
