# Merge Sort

[PR Link](https://github.com/bran2miz/data-structures-and-algorithms/pull/68)

Merge Sort divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Challenge Summary

Review the pseudo code, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudo code provided.

## Pseudo Code

```python
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

Sample Array:

```python
[8,4,23,42,16,15]
```

### Pass 1

#### Step 1: Merge Sort

In the first pass of Mergesort, n is declared as the length of the array. Using the example array, the length would be 6 (n=6). The next statement verifies if n is greater than 1. Because the length of the array is 6, it is greater than 1 and it enters the next set of declarations.

The first declaration identifies the middle of the array. We divide the array length by half, so the middle of the array would be 42. The next declaration identifies the left half of the array. It defines the first half at the array at the index of 0 to the middle, which would be before 42. The first half of the array would equal [8,4,23]. The next declaration identifies the right half of the array. It defines the second half at the array at the middle, to the total length of the array which is 6.
The second half of the array would equal [42, 16, 15]. Mergesort(left) = [8, 4, 23], Mergesort(right) = [42, 16, 15]. Merge(left, right, arr) = Merge([8, 4, 23], [42, 16, 15], [8,4,23,42,16,15]).

![Merge Sort 1](./images/merge-sort-1.png)

#### Step 2: Merge Sort the Separated Arrays (Left)

The next portion of the Mergesort will first sort the left side of the array [8, 4, 23]. We divide the array length by half, so the middle of the array would be 4. The next declaration identifies the left half of the array. It defines the first half at the array at the index of 0 to the middle, which would be before 4. The first half of the array would equal [8]. The next declaration identifies the right half of the array. It defines the second half at the array at the middle, to the total length of the array which is 3. The second half of the array would equal [4, 23]. Mergesort(left) = [8], Mergesort(right) = [4, 23]. Merge(left, right, arr) = Merge([8], [4, 23], [8, 4, 23]).

![Merge Sort 2](./images/merge-sort-2.png)

The next portion of the Mergesort will sort the left side of the second half of the left array [4,23]. We divide the array length by half, so the middle of the array would be 23. The next declaration identifies the left half of the array. It defines the first half at the array at the index of 0 to the middle, which would be before 23. The first half of the array would equal [4]. The next declaration identifies the right half of the array. It defines the second half at the array at the middle, to the total length of the array which is 2. The second half of the array would equal [23].  Mergesort(left) = [4], Mergesort(right) = [23]. Merge(left, right, arr) = Merge([4], [23], [4, 23]).

![Merge Sort 3](./images/merge-sort-3.png)

The next portion of the Mergesort will sort the left side of the second half of the left array [8]. It will break out of the if statement because the length of the array is 1 which is not greater than 1. It will then go to the next integer in the separated array [4]. It will break out again of the if statement. Again, it will then go to the next integer in the separated array [23]. It will break out again of the if statement.

#### Merge Left (last separated array)

Now that the left array are all separated, we need to merge them together in sequential order. We first will merge [4] and [23]. We first declare variables, i, j, and k, and set them to 0. Entering the while loop, we will then verify whether i and j are less than the length of the left and the right array. i = 0 which is less than left.length = 1 and j = 0 which is less than right.length = 1. Both check out so we enter the while loop.

We first check to see if the left at [i] is less than the right at [j]. The left[0] =4 < right[0] = 23 so we then enter the if statement. The left[i] will now replace the array[k]. Thus, left[0]= 4 will now replace the array[0] which is 4, so the number remains the same. Variable i will also increment by 1, so i=0 + 1 = 1. Variable k will also increment by 1, so k = 0 + 1 = 1.

We then try to enter the while loop again. However, it will now end because the variable i is now equal to 1 which is not less than 1. Now we will verify whether i = left.length. Variable i is now 1 = left.length. It finally will set the remaining entries in array to remaining values in right. We finally end up getting the merged array: **[4, 23]**.

#### Merge Left (All of left array merged)

![Merge All Left](./images/merge-1.png)

Now that we merged the right portion of the original left array, we now need to merge all of it. We will merge the left array, [8], and the right array, [4, 23]. We first declare variables, i, j, and k, and set them to 0. Entering the while loop, we will then verify whether i and j are less than the length of the left and the right array. i = 0 which is less than left.length = 1 and j = 0 which is less than right.length = 2. Both check out so we enter the while loop. We first check to see if the left at [i] is less than the right at [j]. The left at i = 8 which is not less than the right at j = 4. We will skip and move to the else statement, where we set the array at k (0) = 8 to the right at the index of j which is 0 (right[0] = 4). 4 will now replace the number 8 at the index of 0. Variable j will also increment by 1, so j = 0 + 1 = 1. Variable k will also increment by 1, so k = 0 + 1 = 1.

new pass: **[4, 8, 23]**

We then try to enter the while loop again. i = 0 which is less than left.length = 1 and j = 1 which is less than right.length = 2. Both check out so we enter the while loop. We first check to see if the left at [i] is less than the right at [j]. The left at i = 0 is 8, which is less than the right at j = 23, so we then enter the if statement. We set the array at the index of 1 = 8 to equate the left[i = 0] = 8; the number at index 1 remains the same in the array. i is incremented to 1 and k is incremented by 2.

We then try to enter the while loop again. i = 1 which is not less than left.length. Then it exits out of the while loop. Now we will verify whether i = left.length. Variable i is now 1 = left.length. It finally will set the remaining entries in array to remaining values in right. We finally end up getting the merged array: **[4, 8, 23]**.

#### Step 2: Merge Sort the Separated Arrays (Right)

The next portion of the Mergesort will first sort the right side of the array [42, 16, 15]. We divide the array length by half, so the middle of the array would be 16. The next declaration identifies the left half of the array. It defines the first half at the array at the index of 0 to the middle, which would be before 16. The first half of the array would equal [42]. The next declaration identifies the right half of the array. It defines the second half at the array at the middle, to the total length of the array which is 3. The second half of the array would equal [16, 15]. Mergesort(left) = [42], Mergesort(right) = [16, 15]. Merge(left, right, arr) = Merge([42], [16, 15], [42, 16, 15]).

![Merge Sort 4](./images/merge-sort-2.png)

The next portion of the Mergesort will sort the right side of the second half of the right array [16, 15]. We divide the array length by half, so the middle of the array would be 15. The next declaration identifies the left half of the array. It defines the first half at the array at the index of 0 to the middle, which would be before 15. The first half of the array would equal [16]. The next declaration identifies the right half of the array. It defines the second half at the array at the middle, to the total length of the array which is 2. The second half of the array would equal [15].  Mergesort(left) = [16], Mergesort(right) = [15]. Merge(left, right, arr) = Merge([16], [15], [16, 15]).

![Merge Sort 5](./images/merge-sort-3.png)

The next portion of the Mergesort will sort the left side of the second half of the right array [42]. It will break out of the if statement because the length of the array is 1 which is not greater than 1. It will then go to the next integer in the separated array [16]. It will break out again of the if statement. Again, it will then go to the next integer in the separated array [15]. It will break out again of the if statement.

#### Merge Right (last separated array)

Now that the integers of the right array are all separated, we need to merge them together in sequential order. We first will merge [15] and [16]. We first declare variables, i, j, and k, and set them to 0. Entering the while loop, we will then verify whether i and j are less than the length of the left and the right array. i = 0 which is less than left.length = 1 and j = 0 which is less than right.length = 1. Both check out so we enter the while loop.

We first check to see if the left at [i] is less than the right at [j]. The left[0] =16 which is not less than the right[0] = 15. Therefore, it will now enter the else statement. The array at the index of k = 0 is now replaced with the right value at the index of j at 0. arr[0] = 16 is replaced by right[0] = 15.  Variable i will also increment by 1, so i=0 + 1 = 1. Variable k will also increment by 1, so k = 0 + 1 = 1.

We then try to enter the while loop again. However, it will now end because the variable i is now equal to 1 which is not less than 1. Now we will verify whether i = left.length. Variable i is now 1 = left.length = 1. It finally will set the remaining entries in array to remaining values in right. We finally end up getting the new merged array: **[15, 16]**.

#### Merge Right (All of right array merged)

![Merge All Right](./images/merge-2.png)

Now that we merged the right portion of the original right array, we now need to merge all of it. We will merge the left array, [42], and the right array, [15, 16]. We first declare variables, i, j, and k, and set them to 0. Entering the while loop, we will then verify whether i and j are less than the length of the left and the right array. i = 0 which is less than left.length = 1 and j = 0 which is less than right.length = 2. Both check out so we enter the while loop. We first check to see if the left at [i] is less than the right at [j]. The left at i([0]) = 42 which is not less than the right at j([0]) = 15. We will skip and move to the else statement, where we set the array at k (0) = 42 to the right at the index of j which is 0 (right[0] = 15). 15 will now replace the number 42 at the index of 0. Variable j will also increment by 1, so j = 0 + 1 = 1. Variable k will also increment by 1, so k = 0 + 1 = 1.

new pass: **[15, 42, 16]**

We then try to enter the while loop again. i = 0 which is less than left.length = 1 and j = 1 which is less than right.length = 2. Both check out so we enter the while loop. We first check to see if the left at [i] is less than the right at [j]. The left at i = 0 is 42, which is not less than the right at j([1]) = 16, so we then enter the else statement. We will set the array at k (1) = 42 to the right at the index of j which is 1 (right[1] = 16). 16 will now replace the number 42 at the index of 1. Variable j will also increment by 1, so j = 1 + 1 = 2. Variable k will also increment by 1, so k = 1 + 1 = 2.

We then try to enter the while loop again. j = 2 which is not less than left.length. Then it exits out of the while loop. Now we will verify whether i = left.length. Variable i is now 0 which does not equal left.length. It finally will set the remaining entries in array to remaining values in left. We finally end up getting the merged array: [15, 16, 42].

#### Merge Left and Right

Merge(left = [4, 8, 23], right= [15, 16, 42], arr= [4, 8, 23, 15, 16, 42])

We now have two arrays that are in sequential order. We must now combine the two arrays using the merge method. We first declare variables, i, j, and k, and set them to 0. Entering the while loop, we will then verify whether i and j are less than the length of the left and the right array. i = 0 which is less than left.length = 3 and j = 0 which is less than right.length = 3. Both check out so we enter the while loop. We first check to see if the left at [i] is less than the right at [j]. The left at i = 4 which is less than the right at j = 15. We then enter the for loop. The array at 0, which is 4, is now replaced by the left[i=0] = 4, maintaining the same position. Variable i will also increment by 1, so i = 0 + 1 = 1. Variable k will also increment by 1, so k = 0 + 1 = 1.

We now will re-enter the while loop where i = 1. We will then verify whether i and j are less than the length of the left and the right array. i = 1 which is less than left.length = 3 and j = 0 which is less than right.length = 3. Both check out so we enter the while loop. We then check to see if the left at [i] is less than the right at [j]. The left at i=1 is 8 which is less than the right at j= 0 = 15. We then enter the for loop. The array at k = 1, which is 8, is now replaced by the left[i=1] = 8, maintaining the same position. Variable i will also increment by 1, so i = 1 + 1 = 2. Variable k will also increment by 1, so k = 1 + 1 = 2.

We now will re-enter the while loop where i = 2. We will then verify whether i and j are less than the length of the left and the right array. i = 2 which is less than left.length = 3 and j = 0 which is less than right.length = 3. Both check out so we enter the while loop. We then check to see if the left at [i] is less than the right at [j]. The left at i=2 is 23 which is not less than the right at j= 0 = 15, so we then enter the else statement. We will set the array at k (2) = 23 to the right at the index of j which is 0 (right[0] = 15). 15 will now replace the number 23 at the index of 2. Variable j will also increment by 1, so j = 0 + 1 = 1. Variable k will also increment by 1, so k = 2 + 1 = 3.

new pass: **[4, 8, 15, 23, 16, 42]**

We now will re-enter the while loop where i = 2 and j = 1. We will then verify whether i and j are less than the length of the left and the right array. i = 2 which is less than left.length = 3 and j = 1 which is less than right.length = 3. Both check out so we enter the while loop. We then check to see if the left at [i] is less than the right at [j]. The left at i=2 is 23 which is not less than the right at j= 1 = 16, so we then enter the else statement. We will set the array at k (3) = 23 to the right at the index of j which is 1 (right[1] = 16). 16 will now replace the number 23 at the index of 3. Variable j will also increment by 1, so j = 1 + 1 = 2. Variable k will also increment by 1, so k = 3 + 1 = 4.

new pass: **[4, 8, 15, 16, 23, 42]**

We then try to enter the while loop again. However, it will now end because the variable i is now equal to 3 which is not less than 3. Now we will verify whether i = left.length. Variable i is now 3 = left.length = 3. It finally will set the remaining entries in array to remaining values in right. We finally end up getting the new merged array: **[4, 8, 15, 16, 23, 42])**.

## Approach & Efficiency

BigO:

time: O(N^2)
space: 0(1) the variables are independent from the array length.

## Testing

![Tests](./images/tests.png)

![Pytest](./images/pytest.png)
