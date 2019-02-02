'''
Name: Jesus Andres Bernal Lopez
Title: Lab 2- Color Space Models
Date: January 29, 2019
'''

def task1():
    # print()
    red, green, blue = input("Enter color values separated by a space: ").split()
    color = (int(red), int(green), int(blue))

    dominant_color = 0
    largest_number = -1

    for i in range(len(color)):
        if color[i] > largest_number:
            largest_number = color[i]
            dominant_color = i

    print(one_dominant_color(dominant_color))

def task2():
    red, green, blue = input("Enter color values separated by a space: ").split()
    color = (int(red), int(green), int(blue))

    dominant_colors = []
    largest_number = -1

    for i in range(len(color)):
        if color[i] > largest_number:
            dominant_colors.clear()
            dominant_colors.append(i)
            largest_number = color[i]
        elif color[i] == largest_number:
            dominant_colors.append(i)

    print(two_dominant_colors(dominant_colors))

def task3():
    color_hex = input("Hex value: ")

    red = int(color_hex[1] + color_hex[2], 16)
    green = int(color_hex[3] + color_hex[4], 16)
    blue = int(color_hex[5] + color_hex[6], 16)

    rgb_tuple = (red, green, blue)
    print(rgb_tuple)

def task4():
    red, green, blue = input("Enter color values separated by a space: ").split()
    rgb_tuple = (int(red), int(green), int(blue))

    hex_color = "#%02x%02x%02x" % rgb_tuple

    print(hex_color)

def task5():
    red, green, blue = input("Enter color values separated by a space: ").split()
    color_tuple = (int(red), int(green), int(blue))

    dominant_colors = []
    largest_number = -1

    for i in range(len(color_tuple)):
        if(color_tuple[i] > largest_number):
            dominant_colors.clear()
            dominant_colors.append(i)
            largest_number = color_tuple[i]
        elif(color_tuple[i] == largest_number):
            dominant_colors.append(i)

    if(len(dominant_colors) == 1):
        dominant_color = dominant_colors[0]
        print(one_dominant_color(dominant_color))
    else:
        print(two_dominant_colors(dominant_colors))

def one_dominant_color(dominant_color):
    if dominant_color == 0:
        return "The color is reddish"
    elif dominant_color == 1:
        return "The color is greenish"
    else:
        return "The color is blueish"

def two_dominant_colors(dominant_colors):
    if dominant_colors.__contains__(0) and dominant_colors.__contains__(1):
        return "The color is a shade of yellow."
    elif dominant_colors.__contains__(0) and dominant_colors.__contains__(2):
        return "The color is a shade of magenta."
    elif dominant_colors.__contains__(1) and dominant_colors.__contains__(2):
        return "The color is a shade of cyan."

if __name__ == "__main__":
    run_again = True
    while run_again:
        task = int(input("What task would you like to run(1-5)(Any other number to stop): "))
        if task == 1:
            task1()
        elif task == 2:
            task2()
        elif task == 3:
            task3()
        elif task == 4:
            task4()
        elif task == 5:
            task5()
        else:
            run_again = False
