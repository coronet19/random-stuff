import random

class Sort():
    def __init__(self, listSize, listRange):
        self.listSize = listSize
        self.listRange = listRange
        self.list = []

    def createList(self):
        for i in range(self.listSize):
            self.list.append(random.randint(0, self.listRange))

    def print(self):
        print(f"{self.list}")

    def bubbleSort(self):
        for i in range(len(self.list)):
            for j in range(len(self.list) - 1):
                if self.list[j] > self.list[j + 1]:
                    temp = self.list[j + 1]
                    self.list[j + 1] = self.list[j]
                    self.list[j] = temp


def main():
    listSize = 0
    listRange = 0
    while True:
        try:
            listSize = int(input("Enter a list size: "))
            break
        except EOFError:
            pass
    while True:
        try:
            listRange = int(input("Enter a list range: "))
            break
        except EOFError:
            pass
    l1 = Sort(listSize, listRange)
    l1.createList()
    l1.print()
    l1.bubbleSort()
    l1.print()


main()