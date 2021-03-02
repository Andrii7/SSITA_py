import math


# ===============1===============
def fizzbuzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# ===============2===============
def profit(sale: dict) -> int:
    return int(round(sale.get('sell_price') * sale.get('quantity') - sale.get('cost_price') * sale.get('quantity')))


# ===============3===============
def square_equation(a: int, b: int, c: int) -> int:
    if a == 0:
        return 0
    else:
        if b == 0 and c == 0:
            return 1
        elif c == 0 and b != 0:
            return 2
        elif b == 0 and c != 0:
            if -c / a > 0:
                return 1
            elif -c / a < 0:
                return 0


# ===============4===============
def square_area(radius: int) -> float:
    if radius <= 0:
        return 0
    area = ((2 * radius ** 2) ** 2) ** 0.5
    return area


# ===============5===============
def multiples(num: int, lenght: int) -> list:
    return [num * i for i in range(1, lenght + 1)]


# ===============6===============
def date_format(date: str) -> str:
    return ''.join(reversed(date.split("/")))


# ===============7===============
def parallel_lines(l1, l2) -> bool:
    return l1[1] / l1[0] == l2[1] / l2[0]


# ===============8===============
def volume_of_sphere(r1, r2):
    return round(math.fabs(((4 / 3) * math.pi * r1 ** 3) - ((4 / 3) * math.pi * r2 ** 3)), 3)


# ===============9===============
def greetings(name: str) -> str:
    guest_list = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    if name in guest_list:
        return f"Hi! I'm {name}, and I'm from {guest_list.get(name)}!"
    else:
        return "Hi! i'm a guest!"


# ===============10===============
def stupid_addition(a, b):
    if type(a).__name__ == type(b).__name__:
        if type(a).__name__ == 'str':
            return int(a) + int(b)
        else:
            return str(a) + str(b)
    else:
        return None


# ===============11===============
def repdigit(num: int) -> bool:
    if num == 0:
        return True
    elif num > 10:
        string = str(num)
        for i in string:
            if string[0] != i:
                return False
            else:
                pass
        return True
    else:
        return False


# ===============12===============
def concat(*lst: list) -> list:
    added = []
    for i in lst:
        added += i
    return added


# ===============13===============
def emptying_values(lst: list) -> list:
    return [type(i)() for i in lst]


# ===============14===============
def sum_fractions(lst: list) -> int:
    return int(round(sum(i[0] / i[1] for i in lst)))


# ===============15===============
def get_indices(lst: list, item) -> list:
    ind = []
    for i, value in enumerate(lst):
        if value == item:
            ind.append(i)
    return ind


# ===============16===============
def count_overlapping(lst: list, num: int):
    for a in lst:
        a.append(a[0] + 1)
        a.append(a[1] - 1)
    return len([True for i in lst if num in i])


# ===============17===============
def progress_days(count: list) -> int:
    pd = 0
    for i in range(len(count) - 1):
        if count[i + 1] > count[i]:
            pd += 1
        else:
            pass
    return pd


# ===============18===============
def square_patch(num: int) -> list:
    matrix = []
    for i in range(num):
        matrix.append([num] * num)
    return matrix


# ===============19===============
def oddish_or_evenish(num: int) -> str:
    summ = sum(map(int, str(num)))
    return 'Oddish' if summ % 2 else 'Evenish'


# ===============20===============
def dice_game(lst: list) -> int:
    score = 0
    for tp in lst:
        if tp[0] == tp[1]:
            return 0
        score += sum(tp)
    return score


# ===============21===============
def is_sastry(num: int) -> bool:
    numb_and_successor = int(str(num) * 2) + 1
    return not numb_and_successor ** 0.5 % 1


# ===============22===============
def num_of_sublists(lst: list) -> int:
    count = 0
    for i in lst:
        if type(i).__name__ == 'list':
            count += 1
    return count


# ===============23===============
def last_digit(a: int, b: int, c: int) -> bool:
    last_a = int(str(a)[-1])
    last_b = int(str(b)[-1])
    last_c = int(str(c)[-1])
    return (last_a * last_b) == last_c


# ===============24===============
def count_uppercase(lst: list) -> int:
    count = 0
    for word in lst:
        for letter in word:
            if letter.isupper():
                count += 1
    return count


# ===============25===============
def is_pandigital(num: int) -> bool:
    lst = list(map(int, str(num)))
    for i in range(10):
        if i not in lst:
            return False
    return True
