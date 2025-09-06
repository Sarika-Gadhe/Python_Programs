data = {"Name" : "Let us C","Author" :  "Y Kanetkar", "Price" : 340,"publication":"BPB Publication"}

print("Loop to display keys")
for X in data :
    print(X)

print("Loop to display values")    
for X in data.values():
    print(X)
    
print("Loop to display key and value")
for X, Y in data.items():
    print(X,Y)    