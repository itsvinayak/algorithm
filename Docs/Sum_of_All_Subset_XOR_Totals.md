# Sum of All Subset XOR Totals

**Problem Statement:**

We are provided with an array of length '**n**', for the given array we have to return the sum of all **XOR** totals for every subset of an array.

**Example:**

```TXT
array = [1,3]
output = 6
Explanation :
         subset => { [ ] ,[ 1 ] ,[ 3 ] , [ 1, 3 ] }
                     =>  XOR([ ]) + XOR([ 1 ]) + XOR([ 3 ]) + XOR([ 1, 3 ])  
                     =>     0      +      1        +       3       +       2       =   6(ans)
```

what is a subset?

Array or element **A** is a subset of a set **B** if all elements of **A** are also elements of **B**

If an array has “n” elements, then the number of subsets of the given set is 2<sup>n</sup>
which means for a given array [1, 3]  of length 2 which means 2<sup>2</sup> => 4

now, we know we have  2<sup>n</sup> subset to count.

## Naive Approach
For the Naive approach or for a brute-force approach, we have to find XOR all possible combinations of the subset in an array and then perform the summation of all XOR values.

#### Explanation

Using Recursive Method

- We have to recursive  including or exclude the current item from xor subset
- Use a global variable to store all sums of xor subset values
- Finally, print the total XOR sum

with this problem, the Time complexity grows exponentially as a result this approach is not good with large numbers

#### code

```python
total_xor_sum = 0


def XORSum(arr, left, right, xor=0):
    global total_xor_sum
    if left > right:
        total_xor_sum += xor
        return
    XORSum(arr, left + 1, right, xor ^ arr[left])
    XORSum(arr, left + 1, right, xor)


def main():
    arr = [1, 5, 6]
    n = len(arr)
    XORSum(arr, 0, n - 1)
    print(total_xor_sum)


if __name__ == '__main__':
    main()

```

#### Input/Output

```TXT
Input :  array => [1, 5, 6]
Output : 28
Total Subsets created 2^3=> 8
- XOR(1) = 1
- XOR(5) = 5
- XOR(6) = 6
- XOR(1, 5)= 4
- XOR(1, 6) = 7
- XOR(5, 6) = 3
- XOR(1, 5, 6) = 2
- XOR() = 0

sum of all these XORs are => 1 + 5 + 6 + 4 + 7 + 3 + 2 + 0
                                            => 28
```

## Using Bit Manipulation Approach
 One of the efficient approaches is to find the bitwise OR.

```TXT
    1 = 001
    5 = 101
    6 = 110
1 ^ 5 = 100
1 ^ 6 = 111
5 ^ 6 = 011
1^5^6 = 010
```

#### Explanation

 if we look at the above binary numbers of the XORs, we can see that the '1' 's or set bit ( set bit is a binary representation of 1 ) occurs in a column is exactly half of 2<sup>n</sup>. From this we can say that If there is any value in an array that has a set bit at i<sup>th</sup>, then exactly 2<sup>n-1</sup> subsets will be of the formed, so they will each set bit will contribute be 2<sup>n-1+i</sup> to the sum and If there is no value in the array with i<sup>th</sup> bit set, then there is no term in all subsets that have i<sup>th</sup> bit set.

**Take a OR of all elements in the array** 
> [1, 5, 6] = 1 | 5 | 6 = 001 | 101 | 110 = 111

here we got **111** as output, Now to we can write it down as :

= 1*2<sup>n-1+2</sup> + 1*2<sup>n-1+1</sup> + 1*2<sup>n-1+0</sup>
as each bit contribute 2<sup>n-1+i</sup> here n is 3 length of array 

On simplify it, we get - bitwise OR of all elements * 2<sup>n-1</sup>


#### code
 
```python
from typing import List


def XORSum(nums: List[int]) -> int:
    ans = 0
    n = len(nums)
    for i in nums:
        ans |= i
    return ans * pow(2, n - 1)


def main():
    arr = [1, 5, 6]
    print(XORSum(arr))


if __name__ == "__main__":
    main()
    
```

#### Input/Output

```
Input :  array => [1, 5, 6]
Output : 28
``` 

practice on : [leetcode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)