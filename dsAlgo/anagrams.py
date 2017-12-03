def make_anagram(str1, str2):
    # Create dictionary
    difference = {}

    for letter in str1:
        if letter not in difference:
            difference[letter] = 0
        difference[letter] += 1

    for letter in str2:
        if letter not in difference:
            difference[letter] = 0
        difference[letter] -= 1

    return sum(abs(n) for n in difference.values())


def check_anagram(str1, str2):
    a = list(str1)
    b = list(str2)

    # sort list
    a.sort()
    b.sort()

    # join list back to String
    a = ''.join(a)
    print("Sorted string : %s" % a)
    b = ''.join(b)
    print("Sorted string : %s" % b)

    return a == b


x = check_anagram("avinash", "aakriti")

print("Are strings anagrams : %s" % x)

y = make_anagram("avinash", "aakriti")
print("minimum characters should be deleted is : %s" % y)
