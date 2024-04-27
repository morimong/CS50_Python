def main():
    convert()


def convert():
    word = input("Input: ")
    print(word.replace(":)", "🙂").replace(":(", "🙁"))


main()
