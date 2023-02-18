# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            if opening_brackets_stack:
                return opening_brackets_stack[0].position
            else:
                return "Success"
            


def main():
    inputW = input()

    if inputW == "F":
        file_path = input("file path:")
        with open("input.txt", "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == 'Success':
                print("Success")
            else:
                print(mismatch)

    else: 
        
        mismatch = find_mismatch(inputW)
        if mismatch == 'Success':
            print("Success")
        else:
            print(mismatch)
    


if __name__ == "__main__":
    main()
