def merge_intervals(intervals):
    for i in range (0,len(intervals)-1):
        if((intervals[i][0] < intervals[i+1][1] ) and (intervals[i][1] >intervals[i+1][0])):
            nums = [intervals[i][0],intervals[i+1][1]]
            
            
        else:
             nums.append([intervals[i+1][0],intervals[i+1][1]])
    return nums
result =merge_intervals( [ [1,3], [2,4], [6,8]])
print(result)

    