class Solution:
    def answer(self,nums,target)->List[int]:
        nums =[9,7,8,2]
        target = 9
        prevMap ={} # index , value 
        
        
        for i,v in enumerate(nums):
            0 , 9
            diff = target - v 
            if diff in prevMap:
                return [prevMap[diff],i]   # [  1    ,  3  ]

            prevMap[v] = i
            # hashmap {index:value , index:value}
            #{9:0 ,7:1 ,  }
            
        return 

i=0, v=9 diff = 0
i=1, v=7      2
i=2, v=2      7
i=3, v=8      1

----------------------------------------------------

hashmap = {
    "mena": "Alice",
    "age": 25,
    "city": "London"
}

print(hashmap["name"])  # Output: Alice



    
    