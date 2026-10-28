def fib_sequence(n):
    a = 0
    b = 1
    even_sum = 0
    sequence = ""
    rev_seq = ""

    for i in range(n):
        if i == 0:
            sequence = str(a)
            rev_seq = str(a)
        else:
            sequence += ", " + str(a)
            rev_seq = str(a) + ", " + rev_seq
        a, b = b, a+b
        if a % 2 == 0:
            even_sum += a

    return f"""Sequence: {sequence}
Even Sum: {even_sum}
Reversed: {rev_seq}"""


def main():
    print(fib_sequence(8))


if __name__ == "__main__":
    main()
