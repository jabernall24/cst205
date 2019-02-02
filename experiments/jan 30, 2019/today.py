#########################################################
#       Tuples are immutable(cannot be changed)         #
#########################################################


# coordinates = (45, 2056)
#
# my_tuple = ([45, 67], 45)
#
# my_tuple[0][1] = 25
#
# print(my_tuple)
#
# hot_pink = (255, 105, 180)
#
# print(hot_pink)


#########################################################
#                    f-strings                          #
#########################################################


# f"hello"
#
# # with f strings
# f"hello{my_tuple}"
#
# # without f strings
# "hello" + str(my_tuple)


#########################################################
#                    range()                            #
#########################################################


# print("range: ", list(range(5)))
#
# print("range: ", list(range(2, 5)))
#
# print("range: ", list(range(0, 100, 5)))
#
# print("range: ", list(range(100, 0, -5)))


#########################################################
#                        loops                          #
#########################################################


#####################
#     for loops     #
#####################


# cities_in_california = ["salinas", "marina", "monterrey", "seaside"]
#
# for city in cities_in_california:
#     print(f"{city.capitalize()} is in california")
#
# for number in range(2):
#     print("This is number ", number)
#
# for i in range(5, 0, -1):
#     print(f"{i}!")
#     if i == 1:
#         print("Blast off!")


#####################
#    while loops    #
#####################


# secret_number = 4
# guess = None
# guess_counter = 0
#
# while guess != secret_number:
#     if guess_counter == 0:
#         guess = int(input("Guess the secret number between 0 and 10: "))
#     else:
#         guess = int(input("Try again: "))
#     guess_counter += 1
#
# if guess_counter == 1:
#     print("\nGreat job! It took you only one guess!")
# elif guess_counter < 6:
#     print(f"\nPretty good. It took you {guess_counter} guesses")
# else:
#     print(f"\nGet a new crystal ball. It took you {guess_counter} guesses")


#########################################################
#                     Functions                         #
#########################################################


# # no parameter
# def say_hello():
#     print("Hello!")
#
#
# # one parameter
# def hello_you(your_name):
#     print(f"Hello, {your_name}!")
#
#
# # return
# def name_year(your_name, birth_year):
#     your_age = 2018 - birth_year
#     return f"Hi {your_name}, you are {your_age} years old."
#
#
# # call the funtions
# say_hello()
#
# hello_you("Jesus")
#
# print(name_year("Jesus", 1845))


#########################################################
#                    Dictionaries                       #
#########################################################

# dictionary = {
#     "year_founded": 1994,
#     "num_students": 7200,
#     "first_gen_percent": 65,
#     "location": "Marina, California"
# }
#
# print(dictionary)
