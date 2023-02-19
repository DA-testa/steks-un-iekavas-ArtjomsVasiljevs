# python3
# Artjoms Vasiļjevs 221RDB330 17.grupa 
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    count = 0
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next in ")]}":
            if(len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char,next)):
                count = i + 1
                break
            opening_brackets_stack.pop()
    if(count == 0 and len(opening_brackets_stack)==0):
        return 'Success'
    else:
        return count
            


def main():
    inputW = input()

    if inputW == "F":
        file_path = input("file path:")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            print(mismatch)

    else: 
        if "I" in inputW:
            text = input()
            mismatch = find_mismatch(text)
            print (mismatch)
    


if __name__ == "__main__":
    main()
