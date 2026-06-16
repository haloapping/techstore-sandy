from string import punctuation

# 1. sorting number in ascending mode
# input:  [6, 2, 9, 10, 8]
# output: [2, 6, 8, 9, 10]


def sort_number(nums):
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


print("Answer 1")
print(sort_number([6, 2, 9, 10, 8]))
print(sort_number([6, 2, 9, 10, 8, -1, -3]), end="\n\n")

# 2. get all unique char
# input:  "BANK BXX"
# output: "BANKX"

# input: "NEGARA WAKANDA"
# output: "NEGARWKD"


def unique_char(text):
    seen = set()
    unique_chars = []

    for c in text:
        if c not in seen and c != " ":
            seen.add(c)
            unique_chars.append(c)

    return "".join(unique_chars)


print("Answer 2")
print(unique_char("BANK BXX"))
print(unique_char("NEGARA WAKANDA"), end="\n\n")


# 3. palindrome
# input: grab
# output: false

# input: Kasur rusak
# output: true

# input: No lemon, no melon
# output: true


def is_palindrome(text):
    clean_chars = []
    for c in text:
        if c not in punctuation and c != " ":
            clean_chars.append(c.lower())

    left_idx = 0
    right_idx = len(clean_chars) - 1
    while left_idx < right_idx:
        if clean_chars[left_idx] != clean_chars[right_idx]:
            return False

        left_idx += 1
        right_idx -= 1

    return True


print("Answer 3")
print(is_palindrome("grab"))
print(is_palindrome("Kasur rusak"))
print(is_palindrome("No lemon, no melon"))
