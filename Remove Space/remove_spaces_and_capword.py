def remove_space_capital(words):
    cap = ""
    no_space = ""
    make_cap = True
    for i in range(len(words)):
        if make_cap:
            chra = chr(ord(words[i])-32)
            cap += chra
            no_space += chra
            make_cap = False
            continue
        if words[i] == " ":
            make_cap = True
            cap += words[i]
        else:
            cap += words[i]
            no_space += words[i]
    return f"""Capitalized: {cap}
No Spaces: {no_space}"""


def main():
    print(remove_space_capital("hello world from python"))


if __name__ == "__main__":
    main()
