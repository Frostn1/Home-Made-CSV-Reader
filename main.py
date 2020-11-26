from Src import hmcsv

file  = hmcsv.read("testFile.csv",deli = ";")
print(file.isOpen())
print(file.raw())
print(file.text())
print(file.row(0))
print(file.col(4))
print(type(file))
print(file.lineNumber)
print(file.write("10;20;30;40;50"))
print(file.writeRows(["10;20;30;40;50","60;70;80;90;100"]))
print(file.writeRow("1;2;3;4;5",0))
