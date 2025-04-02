import math

def min_attempts(a, b):
    return math.ceil(math.log2(b - a + 1))

# Foydalanuvchi kiritishi uchun
if __name__ == "__main__":
    a = int(input("a ni kiriting: "))
    b = int(input("b ni kiriting: "))
    print("Eng kam urinishlar soni:", min_attempts(a, b))