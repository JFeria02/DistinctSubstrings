def distinct_substrings(s):
    results = []
    sub_results = []
    string_lst = list(s)
    # print(string_lst)
    for j in range(0, len(string_lst)):
        first_pt = j
        last_pt = len(string_lst)
        while last_pt != first_pt:
            for i in range(first_pt, last_pt):
                sub_results.append(string_lst[i])
                # print(string_lst[i], end="")
            # print()
            results.append("".join(sub_results))
            sub_results = []
            last_pt -= 1
    return results


if __name__ == '__main__':
    input_string = input("Enter a string: ")
    substring_results = distinct_substrings(input_string)
    print(f"\nDistinct substrings:\n{substring_results}\n\nCount: {len(substring_results)}")
