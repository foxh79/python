#Using functions
def calculate_area(length, width):
    return length * width


def main():
    length = float(input("Length: "))
    width = float(input("Width: "))


    area = calculate_area(length, width)
    print(f"Area of a rectangle of length{length} and width{width} is: {area}")
if __name__ == "__main__":
    main()
