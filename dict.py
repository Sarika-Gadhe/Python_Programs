# dict

# Syntax : {key : Value}
# Hetrogeneous
# ordered
# indexed (Not numeric)
# key duplicates allowed but old gets overwritten
# value duplicate allowed
# data mutable (value)

data = {"Name" : "Let us C","Author" :  "Y Kanetkar", "Price" : 340,"publication":"BPB Publication"}

print("data type : ",type(data))
print("Length is :",len(data))
print(data)

print(data["Author"])

data["Price"] = 400
print(data)
