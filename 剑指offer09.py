class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        while(self.s1 != []):
            self.s2.append(self.s1.pop())
        self.s1.append(value)
        while(self.s2 != []):
            self.s1.append(self.s2.pop())
    def deleteHead(self) -> int:
        if len(self.s1) == 0:
            return -1
        else:
            return self.s1.pop()