def point_inputs():
    print("Enter first point")
    print("Examples: x y   1 2   -5 15")
    point1 = input("Enter first point coordinates: ")
    coordinate_data1 = point1.split(" ")
    x1 = int(coordinate_data1[0])
    y1 = int(coordinate_data1[1])
    print("--------------------")
    print("Enter second point")
    print("Examples: x y   1 2   -5 15")
    point2 = input("Enter second point coordinates: ")
    coordinate_data2 = point2.split(" ")
    x2 = int(coordinate_data2[0])
    y2 = int(coordinate_data2[1])
    print("--------------------")
    x = int(input("Enter x value: "))
    return x1, y1, x2, y2, x


def y_return(x1, y1, x2, y2, x):
    m = (y2 - y1)/(x2-x1)
    b = y1 - m*x1
    y = m*x + b
    print("--------------------")
    return y


def main():
    (x1, y1, x2, y2, x) = point_inputs()
    y = y_return(x1, y1, x2, y2, x)
    print("The corresponding y value is {}".format(y))


if __name__ == "__main__":
    main()
