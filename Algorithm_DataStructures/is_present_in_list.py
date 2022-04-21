def is_present_in_list(words, keywords):
    len_words = len(words)
    len_keywords = len(keywords)
    i = 0
    while i < (len_words - len_keywords + 1):
        print("infinity and beyond_1")
        j = 0
        while j < len_keywords:
            if words[i + j] != keywords[j] and keywords[j] != "anything":
                break
            j += 1
        if j == len_keywords:
            return True, i
    i = i + 1
    return False, i


words = ["apple", "orange", "orange", "banana", "banana"]
keywords = [
    ["apple", "apple"],
    [
        "apple",
        "anything",
        "apple",
    ],
]


def Is_customer_won(shopping_cart, patterns):
    len_S = len(shopping_cart)
    len_p = len(patterns)
    idx_s = 0
    idx_p = 0
    result = True
    while idx_p < len_p and idx_s < len_S:
        temp_result, temp_idx = is_present_in_list(
            shopping_cart[idx_s:], patterns[idx_p]
        )
        result = result and temp_result
        if not result:
            return 0

        idx_s += temp_idx
        idx_p += 1
    return 1


print(Is_customer_won(words, keywords))
