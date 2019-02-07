
class count:
    def __init__(self):
        self.mathematics = []
list1 = [12, 15, 18, 20, 45, 88, 8, 25, 6, 78, 25, 2, 4, 66]
for n in list1:
    print n * 3

list2 = [21, 51, 81, 40, 54, 88, 7, 52, 5, 87, 52, 3, 2, 66]
for n in list2:
    print n - 5

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b
print div(25, 5)
