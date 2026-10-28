def rom_to_int(rom):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    valid_subtractions = {"IV", "IX", "XL", "XC", "CD", "CM"}

    for i in range(len(rom)):
        if i < len(rom) - 1 and roman[rom[i]] < roman[rom[i+1]]:
            pair = rom[i:i+2]
            if pair in valid_subtractions:
                result -= roman[rom[i]]
            else:
                return "Invalid roman figure"
        else:
            result += roman[rom[i]]

    return result


def main():
    print(rom_to_int("III"))
    print(rom_to_int("LVIII"))
    print(rom_to_int("MCMXCIV"))
    print(rom_to_int("IC"))


if __name__ == "__main__":
    main()
