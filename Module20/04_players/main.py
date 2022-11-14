players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


def parse_players(data):
    return [
        tuple(
            [elem for elem in key] + [elem for elem in value]
        )
        for key, value in data.items()
    ]


def main():
    print(parse_players(players))


if __name__ == '__main__':
    main()
