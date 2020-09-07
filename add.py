def interface():
    print("Adding")
    while True:
        print("1 - Add")
        print("2 - Quit")
        choice = input("Select: ")
        if choice == '2':
            return
        elif choice == '1':
            do_math()

def do_math():
    val_1, val_2 = get_input()
    c = do_add(val_1, val_2)

def get_input():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    return a, b

def do_add(a, b):
    c = int(a) + int(b)
    return c

if __name__ == "__main__":
    interface()