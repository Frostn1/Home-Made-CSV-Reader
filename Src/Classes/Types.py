class Reader:
    def __init__(self,filePath,deli=","):
        self.file_path = filePath
        self.lineNumber = self.getLength()
        self.deli = deli
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
                   
                    if self.deli in line:
                        new_text.append(line.rstrip("\n").split(self.deli))
                    elif line.replace(" ","") != " ":
                        
                        raise Exception("Delimeter is no correct")
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
    def write(self,text):
        with open(self.file_path,"w") as file1:
            file1.write(text)
    def writeRows(self,rows):
        with open(self.file_path,"w") as file1:
            pass
        with open(self.file_path,"a") as file1:
            for row in rows:
                file1.write(row)
                file1.write("\n")
    def writeRow(self,row,index):
        text = self.text()
        if index > len(text) - 1:
            raise Exception("Index out of range")
        else:
            text[index] = row.split(self.deli)
            new_list = []
            for item in text:
                new_list.append(";".join(item))
            self.writeRows(new_list)

        