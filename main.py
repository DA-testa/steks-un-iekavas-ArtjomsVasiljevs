# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    count = -1
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next in ")]}":
             if(len(opening_brackets_stack)==0 or not opening_brackets_stack[-1].are_matching(next)):
                count = i +1
        if(count == -1 and len(opening_brackets_stack)==0):
            return 'Success'
        else:
            return count
            


def main():
    inputW = input("F or I")

    if inputW == "F":
        file_path = input("file path:")
        with open("input.txt", "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == 'Success':
                print("Success")
            else:
                print(mismatch)

    elif inputW == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == 'Success':
            print("Success")
        else:
            print(mismatch)
    


if __name__ == "__main__":
    main()
