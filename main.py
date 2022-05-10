# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
first_word, second_word = input().split()

def is_anagram(first,second):
    new_first=first.lower()
    new_second=second.lower()
    i=0
    if len(first)!=len(second):
        return False
    else:
        list_second = list(new_second)
        while i<=len(new_first)-1:
            if new_first[i] in list_second:
                list_second.remove(new_first[i])
            i=i+1
        if len(list_second)==0:
            return True
        else:
            return False
result = is_anagram(first_word, second_word)
print(result)