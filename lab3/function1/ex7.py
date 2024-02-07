def has_33(nums):
    bool = False
    for i in range(len(nums)):
        if (nums[i]==3 and nums[i+1]==3):
            bool = True
    print(bool)
nums=[3,1,2,5,3,4]
has_33(nums)
        