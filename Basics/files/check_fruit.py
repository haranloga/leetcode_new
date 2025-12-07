fruit = ["apple", "banana", "orange", "mango"]
veg = ["carrot", "broccoli", "peas", "artichoke","banana"]

# if fruit in vegetable print that item only
def check(fruit,veg):
    for v in veg:
        if v in fruit:
            print(v)



if __name__ == "__main__":
    check(fruit,veg)
