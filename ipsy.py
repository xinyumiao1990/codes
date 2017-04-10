# 16/10
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def twoSum(target, arr):
    d = {}
    pair = set([])
    # fill a dictionary d e.g. d[-1] = [0, 4]
    for i in xrange(len(arr)):
        if d.get(arr[i]) is None:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
    for j in xrange(len(arr)):
        # pass when it's a duplicate item
        # because it should already solved in the first item case
        if d.get(arr[j]) is not None and d[arr[j]][0] != j:
            continue

        if d.get(target - arr[j]) is not None:
            if j in d[target - arr[j]]:  # remove current index from the list
                d[target - arr[j]].remove(j)
            if len(d[target - arr[j]]) > 0:
                if j > d[target - arr[j]][0]:
                    pair.add((d[target - arr[j]][0], j))
                else:
                    pair.add((j, d[target - arr[j]][0]))

    return list(pair)  # return index

print twoSum(0, [0, 0, 1, 2, -1, -4, 0])

def threeSum(arr):
    if len(arr) <= 2:
        return None

    solution = set([])

    for i in xrange(len(arr)):
        new_arr = arr[:i] + arr[(i + 1):]
        result = twoSum(0 - arr[i], new_arr)
        if result:
            for (x, y) in result:
                solution.add(tuple(sorted([arr[i], new_arr[x], new_arr[y]])))

    return map(list, list(solution))

print threeSum([-1, 0, 1, 2, -1, -4, 1])