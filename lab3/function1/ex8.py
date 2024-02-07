def spy_game(nums):
    b=0
    bool = False
    for i in range(len(nums)):
        if nums[i] == 0:
            b=b+1
        elif nums[i] == 7 and b>=2:
            bool = True
    print(bool)    
nums = [1,0,7,0,1,7,5]
spy_game(nums) 