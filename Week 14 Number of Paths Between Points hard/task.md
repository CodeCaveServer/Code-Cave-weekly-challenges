This challenge deals with finding and counting the number of paths between points on a rectilinear grid. A starting point (x, y) with non-negative integer coordinates is provided. You are only allowed to move horizontally and vertically along the grid. Hence, from (x, y) you may move to `(x+1, y), (x-1, y), (x, y+1), or (x, y-1)`. Your goal is to return to the origin (0, 0) in such a way that you never increase the distance to the origin. The distance is counted as the minimum number of total vertical and horizontal steps to reach the origin.

Create a function that reads a starting location, (x, y) and returns the total number of different paths back to the origin. Two paths are different if there is at least one step on the path that is different even if most of the steps are the same.
Examples
```
paths(0, 0) ➞ 1

paths(2, 1) ➞ 3

paths(2, 2) ➞ 6
```
**Notes**

    This function can be easily written using recursion. It is STRONGLY recommended (though not necessary) that you use some form of recursion in your solution.
    The return type for this function is a positive integer.
    x and y will always be integers greater than or equal to 0.

