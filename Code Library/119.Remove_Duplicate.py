def remove_duplicates(sentence: str) -> str:
    sen_list = sentence.split(" ")
    check = set()

    for a_word in sen_list:
        check.add(a_word)

    return " ".join(sorted(check))


if __name__ == "__main__":
    print(remove_duplicates("INPUT_SENTENCE"))
