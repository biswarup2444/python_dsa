def summation(nums):
    a=[]
    nums.sort()
    i=0
    while nums[i]<0:
        l=i+1
        r=len(nums)-1
        t=0-nums[i]
        tracker=set()
        while l<r:

            if nums[r]+nums[l]==t:
                b=[nums[i],nums[l],nums[r]]
                l+=1
                r-=1
                if b not in a:
                    a.append(b)

                    b=[]
            elif t> nums[r]+nums[l]:
                l+=1
            else:
                r-=1
        i+=1
    return a




a=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(summation(a))