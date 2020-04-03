def reverse_words(input_str: str) -> str:
    input_str = input_str.split(" ")
    new_str = list()

    for a_word in input_str:
        new_str.insert(0, a_word)

    return " ".join(new_str)


if __name__ == "__main__":
    print(reverse_words("INPUT STRING"))
