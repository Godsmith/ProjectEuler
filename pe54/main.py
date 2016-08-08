from pe54.hand import Hand


def main():
    with open('poker.txt') as f:
        p1_wins = 0
        for line in f.readlines():
            h1 = Hand(line[:14])
            h2 = Hand(line[15:])
            does_p1_win = h1 > h2
            print(h1, h2, h1 > h2)
            if does_p1_win:
                p1_wins += 1
    print(p1_wins)


if __name__ == '__main__':
    main()
