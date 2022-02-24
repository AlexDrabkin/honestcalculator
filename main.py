import operator

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


math_operators = "+ - / *"
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def is_not_number(*args):
    for i in args:
        try:
            int(i)
        except ValueError:
            try:
                float(i)
            except ValueError:
                print(msg_1)
                return True


def is_bad_operator(data: list) -> bool:
    if data[1] not in operators:
        print(msg_2)
        return True


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == '1' or y == '1' or x == 1 or y == 1) and oper == '*':
        msg = msg + msg_7
    if (x == '0' or y == '0' or x == 0 or y == 0) and (oper == '*' or oper == '+' or oper == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def zero_division(data: list) -> bool:
    if data[1] == '/' and (data[2] == '0' or data[2] == 0):
        check(float(data[0]), float(data[2]), data[1])
        print(msg_3)
        return True


def check_memory(data: list):
    if data[0] == 'M' and data[2] == 'M':
        return 'XY'
    if data[0] == 'M':
        return 'X'
    elif data[2] == 'M':
        return 'Y'


def get_processed_input(mem):
    while True:
        print(msg_0)
        calc = input().split()
        if check_memory(calc) == 'XY':
            calc[0] = mem
            calc[2] = mem
            if zero_division(calc):
                continue
            elif is_not_number(calc[0], calc[2]):
                continue
            elif is_bad_operator(calc):
                continue
            else:
                return calc
        elif check_memory(calc) == 'X':
            calc[0] = mem
            if is_not_number(calc[0], calc[2]):
                continue
            elif is_bad_operator(calc):
                continue
            else:
                return calc
        elif check_memory(calc) == 'Y':
            calc[2] = mem
            if zero_division(calc):
                continue
            elif is_not_number(calc[0], calc[2]):
                continue
            elif is_bad_operator(calc):
                continue
            else:
                return calc
        elif is_bad_operator(calc):
            continue
        elif is_not_number(calc[0], calc[2]):
            continue
        elif zero_division(calc):
            continue
        else:
            return calc


def calculation(data: list) -> float:
    check(float(data[0]), float(data[2]), data[1])
    res = operators[data[1]](float(data[0]), float(data[2]))
    print(res)
    return res


def save_result():
    print(msg_4)
    store = input()
    if store == 'y':
        return True
    elif store == 'n':
        return False


memory = 0
answer = 'y'
while answer == 'y':
    result = calculation(get_processed_input(memory))
    if save_result():
        if is_one_digit(result):
            msg_index = 10
            answer_digit = 'y'
            while answer_digit == 'y':
                print(locals()["msg_" + str(msg_index)])
                answer_digit = input()
                if answer_digit == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
                        answer_digit = 'n'
        else:
            memory = result
    print(msg_5)
    answer = input()
