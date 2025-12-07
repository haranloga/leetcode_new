class Solution:
    def containDuplicate(self,nums):
        # List  12341   =>  
        seen =set(nums)   # 1234
        
        for num in nums:
            if num in seen: # set efficient 
                return True
            
            seen.add(num) #1,2,3,4
        return False

    
    def duplicate(nums):
        return (len(nums) != len(set[Any](nums)))
           
num 8
num += 1 # num = num + 1
num-- 
num++


number = 4

match number:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case 4:
        print("Number is 4")
    case _:
        print("Number is something else")


value = "jpg"

match value:
    case "jpg" | "png" | "gif":
        print("Image file")
    case "mp3" | "wav":
        print("Audio file")
    case _:
        print("Unknown file type")


age = 20

match age:
    case a if a < 13:
        print("Child")
    case a if 13 <= a < 18:
        print("Teen")
    case a if a >= 18:
        print("Adult")



fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i)


for i in range(10): 0...9
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)
0 skip 
1 print
2 skip
# 1


for i in range(10): 0...9
    if i % 2 == 0:
        break  # skip even numbers
    print(i)

# 