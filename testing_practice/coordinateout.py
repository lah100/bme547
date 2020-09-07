def interface():
    print("Determine a New Y Coordinate")
    while True:
        print("1 - Enter Your Coordinates in Integer Form")
        print("2 - Quit Program")
        choice = input("Make a selection: ")
        if choice == '2':
            return
        elif choice == '1':
            find_coord()

def find_coord():
	x_1, y_1, x_2, y_2, new_x = get_input()
	new_y = output_y(x_1, y_1, x_2, y_2, new_x)

def get_input():
    x_1 = input("Enter your first x coordinate: ")
    y_1 = input("Enter your first y coordinate: ")
    x_2 = input("Enter your second x coordinate: ")
    y_2 = input("Enter your second y coordinate: ")
    new_x = input("Enter your new x coordinate: ")
    return x_1, y_1, x_2, y_2, new_x
	

def output_y(x1, y1, x2, y2, new_x) :
    diff1 = int(y2) - int(y1)
    diff2 = int(x2) - int(x1)
    slope = diff1/diff2
    b = int(y1) - (slope*int(x1))
    new_y = int((slope*int(new_x)) + b)
    print("Your new y coordinate is: {:d}".format(new_y))
    return int(new_y)

if __name__ == "__main__":
	interface()	
