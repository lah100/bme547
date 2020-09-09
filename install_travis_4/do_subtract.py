def interface():
    while True:
        print("1 - Input")
        print("2 - Quit")
        choice = input("select one:")
        if choice == '2':
            return
        else:
            math()

def math():
    a, b = get_input()
    answer = subtract(a,b)

def get_input():
	a = input("First: ")
	b = input("Second: ")
	return a, b

def subtract(a,b):
    answer = int(a) - int(b)
    return answer

if __name__ == "__main__":
    interface()
