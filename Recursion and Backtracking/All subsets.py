#return all subsets of the set
def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(list(path))  # Add current subset
        for i in range(start, len(nums)):
            path.append(nums[i])         # Choose
            backtrack(i + 1, path)       # Explore
            path.pop()                   # Un-choose (backtrack)

    backtrack(0, [])
    return res

print("enter a list")
l=list(map(int,input().split()))
print(subsets(l))