import random

color_list1 = [str(i) for i in input(
    "enter colors only with commans and spaces: ").split(", ")]


def color_list():
    color_list2 = [str(i) for i in input(
        "perheps u forgot comman or space please try again like this: red, green and so on... \ntry again: ").split(", ")]
    color_str1 = ""
    random_color1 = []

    random_color1.append(random.choice(color_list2))

    for k in random_color1:
        if k.isalpha():
            color_str1 += k
            return f"your favorite color is {color_str1.strip()}! \N{slightly smiling face}"
        return "u have no more chance!"


def favorite_color(arr):
    color_str = ""
    random_color = []

    random_color.append(random.choice(arr))
    for i in random_color:
        if i.isalpha():
            color_str += i
            return f"your favorite color is {color_str.strip()}! \N{slightly smiling face}"
        return color_list()


print(favorite_color(color_list1))
