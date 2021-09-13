def combinationSum( candidates, target) :
    if target == 0:
        return True
    elif target < 0:
        return False
    a = []
    for i in candidates:
        target = target-i
        if combinationSum(candidates, target) :
            a.append(i)
        target = target+i
    return False
if __name__ == '__main__':
    ar=[3,2]
    print(combinationSum(ar, 8))