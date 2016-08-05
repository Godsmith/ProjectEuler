def main():
    count = 0
    for power in range(1, 42):
        i = 1
        while True:
            value = str(i ** power)
            length = len(value)
            if length == power:
                print(value)
                count += 1
            elif length > power:
                break
            i += 1
    print(count)


if __name__ == '__main__':
    main()
