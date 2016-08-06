from primes import primes_up_to


def rotate_nested_list(nested_list):
    translation = zip(*nested_list)
    return [list(reversed(list_)) for list_ in translation]


def spiral_square(d):
    square = [[1]]
    while len(square) < d:
        square = add_2_to_diameter_of_spiral_square(square)
    return square


def add_2_to_diameter_of_spiral_square(square):
    d = len(square)
    n = d ** 2
    new_first_row_start = n+d
    new_first_row = list(range(new_first_row_start + d + 2, new_first_row_start, -1))
    new_last_row_end = (d + 2) ** 2
    new_last_row = list(reversed(range(new_last_row_end, new_last_row_end - d - 2, -1)))
    first_column = range(new_first_row[0] + 1, new_last_row[0])
    last_column = range(new_first_row[-1] - 1, new_first_row[-1] - d - 1, -1)

    new_square = [new_first_row]
    for first, last, row in zip(first_column, last_column, square):
        new_square.append([first] + row + [last])
    new_square.append(new_last_row)
    return new_square


def get_spiral_square_diagonals(side_length):
    highest_number_in_previous_layer = (side_length - 2) ** 2
    first_corner_number = highest_number_in_previous_layer + side_length - 1
    return {
        first_corner_number,
        first_corner_number + side_length - 1,
        first_corner_number + 2 * (side_length - 1),
        first_corner_number + 3 * (side_length - 1)
    }

def main():
    all_primes = set(primes_up_to(100000000))
    prime_diagonals = set()
    nonprime_diagonals = {1}

    side_length = 1
    while True:
        side_length += 2
        diagonals = get_spiral_square_diagonals(side_length)
        for diagonal in diagonals:
            if diagonal in all_primes:
                prime_diagonals.add(diagonal)
            else:
                nonprime_diagonals.add(diagonal)
        quotient = len(prime_diagonals) / (len(prime_diagonals) + len(nonprime_diagonals))
        if quotient < 0.1:
            print(side_length, quotient)
            break


if __name__ == '__main__':
    main()
