class Board:
    def __init__(self):
        self.numSticks = 15
        self.file1 = [True,True,True]
        self.file2 = [True,True,True,True,True]
        self.file3 = [True,True,True,True,True,True,True]
    def paint(self):
        st1 = "  "
        for x in range(0, len(self.file1)):
            if self.file1[x]:
                st1 += "|"
            elif not self.file1[x]:
                st1 += "_"
        st1 += "  "
        print st1

        st1 = " "
        for x in range(0, len(self.file2)):
            if self.file2[x]:
                st1 += "|"
            elif not self.file2[x]:
                st1 += "_"
        st1 += " "
        print st1

        st1 = ""
        for x in range(0, len(self.file3)):
            if self.file3[x]:
                st1 += "|"
            elif not self.file3[x]:
                st1 += "_"

        print st1

    def numSticksAvaliable(self,numFile):
        counter = 0
        list_1 = []
        if numFile == 1:
            list_1 = self.file1
        elif numFile == 2:
            list_1 = self.file2
        elif numFile == 3:
            list_1 = self.file3
        for x in range(0, len(list_1)):
            if list_1[x]:
                counter += 1
        return counter

    def crossOut(self, numFile, numOfSticks):
        counter = 0
        if numFile == 1:
            for x in range(0, len(self.file1)):
                if  self.file1[x] & counter < numOfSticks:
                    self.file1[x] = False
                    counter += 1
                    self.numSticks = self.numSticks -1
        elif numFile == 2:
            for x in range(0, len(self.file2)):
                if  self.file2[x] & counter < numOfSticks:
                    self.file2[x] = False
                    counter += 1
                    self.numSticks = self.numSticks -1
        elif numFile == 3:
            for x in range(0, len(self.file3)):
                if  self.file3[x] & counter < numOfSticks:
                    self.file3[x] = False
                    counter += 1
                    self.numSticks = self.numSticks -1