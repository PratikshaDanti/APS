def palindromic_string(input_string):
    max_length = 0
    new_input_string = ""
    output_string = ""
    for i in input_string[: len(input_string) - 1]:
        new_input_string += i + "|"
    new_input_string += input_string[-1]

    l, r = 0, 0
    length = [1 for i in range(len(new_input_string))]
    for i in range(len(new_input_string)):
        k = 1 if i > r else min(length[l + r - i] // 2, r - i + 1)
        while (
            i - k >= 0
            and i + k < len(new_input_string)
            and new_input_string[k + i] == new_input_string[i - k]
        ):
            k += 1

        length[i] = 2 * k - 1
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

        if max_length < length[i]:
            max_length = length[i]
            start = i

    s = new_input_string[start - max_length // 2 : start + max_length // 2 + 1]
    for i in s:
        if i != "|":
            output_string += i

    return output_string

s=input('Enter the string : ')
x=palindromic_string(s)
print(x)
