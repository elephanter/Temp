import math


def is_balanced(braces):
    square_open = "["
    square_close = "]"
    square_open_num = 0
    square_close_num = 0

    curly_open = "{"
    curly_close = "}"
    curly_open_num = 0
    curly_close_num = 0

    round_open = "("
    round_close = ")"
    round_open_num = 0
    round_close_num = 0

    def equal(a, b):
        if (a == square_open and b == square_close) or (a == square_close and b == square_open):
            return True
        if (a == curly_open and b == curly_close) or (a == curly_close and b == curly_open):
            return True
        if (a == round_open and b == round_close) or (a == round_close and b == round_open):
            return True
        if a == " " and b == " ":
            return True
        else:
            return False

    for b in braces:
        if b == square_open: square_open_num = square_open_num + 1
        if b == square_close: square_close_num = square_close_num + 1
        if b == curly_open: curly_open_num = curly_open_num + 1
        if b == curly_close: curly_close_num = curly_close_num + 1
        if b == round_open: round_open_num = round_open_num + 1
        if b == round_close: round_close_num = round_close_num + 1

    if square_open_num == square_close_num and curly_open_num == curly_close_num:
        length = math.floor(len(braces) / 2)
        left_side = braces[:length]
        right_side = ''.join(reversed(braces[-length:]))
        if False in [equal(left_side[l], right_side[l]) for l in range(length)]:
            return False
        else:
            return True
    else:
        return False

print(is_balanced("{ [ ] } )"))
print(is_balanced("{ [ } ]"))
print(is_balanced("{ [ ] }"))

print(is_balanced("{[[[[[[[[[[[[[[((((((((((({{{{{{{{{}}}}}}}}})))))))))))]]]]]]]]]]]]]]}"))
print(is_balanced("{} {} {}"))
print(is_balanced("{} { } {}"))
print(is_balanced(" { } { } { } "))
print(is_balanced(" { } {   } { } "))
print(is_balanced(" { } {   } { }    "))


