class Reader:
    def __init__(self,filePath):
        self.file_path = filePath
        self.lineNumber = self.getLength()
    def getLength(self):
       with open(self.file_path) as file1:
           return len(file1.readlines()) 
    def raw(self):
        if self.isOpen():
            with open(self.file_path) as file1:
                return file1.read()
        else:
            raise Exception("File doesnt exist")
    def text(self):
        if self.isOpen():
            with open(self.file_path) as file1:
                text = file1.readlines()
                new_text = []
                for line in text:
                    new_text.append(line.rstrip("\n").split(','))
                return new_text
        else:
            raise Exception("File doesnt exist")
    def isOpen(self):
        try:
            with open(self.file_path) as file1:
                return True
        except FileNotFoundError:
            return False
    def row(self,index):
        text = self.text()
        if index > len(text)-1:
            raise Exception("Row index out of range")
        else:
            return text[index]
    def col(self,index):
        new_text = []
        flag = False
        for line in self.text():
            if index < len(line):
                new_text.append(line[index])
                flag = True
            else:
                new_text.append("NOT DEFINED")
        if flag:
            return new_text
        else:
            raise Exception("Column index out of range")


        