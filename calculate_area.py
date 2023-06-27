
import math
int_radius =  int(input("enter radius --->>"))

def calculate_area (int_radius):
    out_num = math.pi * (int_radius**2)

    return out_num

print(calculate_area(int_radius))

