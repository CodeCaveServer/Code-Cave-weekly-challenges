array = [10, 9, 2, 5, 3, 7, 101, 18]

def longestIncreasing(arr):
    longest = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > longest[-1]:
            longest.append(arr[i])
        else:
            longest = [arr[i]]
    return len(longest)
