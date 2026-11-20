import sys

def calculate_square(num):
    return num * num

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(calculate_square(num))