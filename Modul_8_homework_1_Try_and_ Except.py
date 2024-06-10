def add_everything_up(a, b):

    try:
        result = a + b
        return result

    except TypeError:
        print(f"{a}{b}")

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
print(f'{(add_everything_up(123.456, 7)):.3f}')
