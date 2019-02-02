
def print_dictionary(dictionary) -> str:
    final_dictionary = "{\n"
    for key in dictionary:
        final_dictionary += f"\t{key}: {dictionary[key]},\n"
    final_dictionary += "}"
    print(final_dictionary)


def get_bin(num) -> int:
    if num >= 0 and num <= 63:
        return 0
    elif num >= 64 and num <= 127:
        return 1
    elif num >= 128 and num <= 191:
        return 2
    elif num >= 192 and num <= 255:
        return 3


def task1(pixel_image):
    dict = {
        "red": [0, 0, 0, 0],
        "green": [0, 0, 0, 0],
        "blue": [0, 0, 0, 0],
    }

    for row in pixel_image:
        for color in row:
            dict["red"][get_bin(color[0])] += 1
            dict["green"][get_bin(color[1])] += 1
            dict["blue"][get_bin(color[2])] += 1

    print_dictionary(dict)


if __name__ == "__main__":
    my_list = [
        [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
        [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
        [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
        [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
    ]

    task1(my_list)
