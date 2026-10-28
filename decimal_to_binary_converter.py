def binary_converter(num):
    output = ""

    while num:
        rem = num % 2
        num = num // 2

        output = str(rem) + output
    return output


def main():
    print(binary_converter(10))
    print(binary_converter(25))
    print(binary_converter(1))


if __name__ == "__main__":
    main()
