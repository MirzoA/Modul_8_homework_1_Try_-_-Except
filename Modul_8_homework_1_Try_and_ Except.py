def add_everything_up(a, b):

    try:
        result = a + b
        print(f"{result:.3f}")
    except TypeError:
        print(f"{a}{b}")

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)