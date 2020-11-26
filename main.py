from Src import hmcsv

file  = hmcsv.read("testFile.csv")
print(file.isOpen())
print(file.raw())
print(file.text())
print(file.row(1))
print(file.col(4))
print(type(file))
print(file.lineNumber)
