first_word, second_word = input().split()

def is_anagram(first, second):
    new_first = first.lower()
    new_second = second.lower()
    i = 0
    if len(first) != len(second):
        return False
    else:
        list_second = list(new_second)
        while i <= len(new_first) - 1:
            if new_first[i] in list_second:
                list_second.remove(new_first[i])
            i = i + 1
        if len(list_second) == 0:
            return True
        else:
            return False


result = is_anagram(first_word, second_word)
print(result)

# !!! compact solution
first_word, second_word = input().split()

def is_anagram(a, b):
    return sorted(a) == sorted(b)

result = is_anagram(first_word, second_word)
print(result)
#
