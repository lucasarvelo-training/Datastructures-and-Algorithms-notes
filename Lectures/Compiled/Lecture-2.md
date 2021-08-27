# Lecture 2
  
  
---
  
## Nested Loops
  
  
### Example 1
  
  
    sum <- 0
    for ( i <- 0, i < n, i++)
        for ( j <- 0, j < n, j++)
            sum++
  
IL =  <img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{j=0}^{n-1}%201%20=%20n"/>
OL = <img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i=0}^{n-1}%20IL%20=%20n&#x5C;times%20IL%20=%20n&#x5C;times%20n%20=%20n^2"/>
  
<img src="https://latex.codecogs.com/gif.latex?n^2%20&#x5C;in%20O(n^2),&#x5C;Omega(n^2)%20&#x5C;to%20&#x5C;Theta(n^2)"/>
  
### Example 2
  
  
    sum <- 0
    for ( i <- 0, i < n, i++)
        for ( j <- 0, j < i*i , j++)
            sum++
  
IL = <img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{j=0}^{i^2-1}%201%20=%20i^2"/>
OL = <img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i=0}^{n-1}%20IL%20=%20&#x5C;Sigma_{i=0}^{n-1}%20i^2%20=%20n%20&#x5C;times%20&#x5C;frac{(n+1)&#x5C;times(2n+1)}{6}"/>
<img src="https://latex.codecogs.com/gif.latex?=%20&#x5C;frac{1}{6}(2n^3+n^2+2n^2+n)%20&#x5C;in%20&#x5C;Theta(n^3)"/>
  
### Example 3
  
  
    for(i=0, i<n,i++)
        for(j=0, j<n, j++)
            for(k=0, k<n, k++)
                sum++
  
  
<img src="https://latex.codecogs.com/gif.latex?IL_A%20=%20&#x5C;Sigma_{k&#x5C;in%20n}%201%20=%20n"/>
<img src="https://latex.codecogs.com/gif.latex?IL_B%20=%20&#x5C;Sigma_{j&#x5C;in%20n}%20IL_A%20=%20n&#x5C;times%20n%20=%20n^2"/>
<img src="https://latex.codecogs.com/gif.latex?OL%20=%20&#x5C;Sigma_{i&#x5C;in%20n}%20IL_B%20=%20n&#x5C;times%20n^2%20=%20n^3"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;to%20&#x5C;Theta(n^3)"/>
  
### Example 4
  
  
    for ( i = 1 ; i <= n ; i*=2 )
        for (j = 0 ; j< n ; j++ )
            sum++
<img src="https://latex.codecogs.com/gif.latex?IL%20=%20&#x5C;Sigma_{j&#x5C;in%20n}1%20=%20n"/>  
<img src="https://latex.codecogs.com/gif.latex?OL%20=%20&#x5C;Sigma_{i%20=%201}^{log_{2}n}%20IL%20=%20n%20*%20log_2n"/> <img src="https://latex.codecogs.com/gif.latex?&#x5C;to%20&#x5C;Theta(nlogn)"/>  
  
### Example 5
  
  
    for ( i = 1; i < n; i++ )
        if ( n%2 == 0 )
            for ( j = 0; j < n; j++ )
                sum++
        else
            sum--
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i%20&#x5C;in%20n}%20max&#x5C;{if_a,if_b&#x5C;}"/>
  
<img src="https://latex.codecogs.com/gif.latex?max&#x5C;{if_a,if_b&#x5C;}%20=%20max&#x5C;{&#x5C;Sigma_{j&#x5C;in%20n}1,1&#x5C;}%20=%20&#x5C;Sigma_{j&#x5C;in%20n}1%20=%20n"/>
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i%20&#x5C;in%20n}%20max&#x5C;{if_a,if_b&#x5C;}%20=%20&#x5C;Sigma_{i%20&#x5C;in%20n}n%20=%20n^2"/>
  
### Example 6
  
  
    ## x <- array
    ## n <- size
    ## k <- number we are searching for
    ## pos <- current index
    int rlinear( x:int[], n:int , k:int , pos: int):
        if pos == n : return -1
  
        if X[pos] == k : return pos
        if X[pos] > k : return -1
  
        return rlinear( X, n, k, pos+1)
  
Iterates over an array looking for the index of k. If k is found, the index is returned.
  
Worst case: K not found in the array thus n iterations over the array.
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i%20&#x5C;in%20n}1%20=%20n%20&#x5C;in%20O(n)"/>
  
### Example 7 - Binary search
  
  
Suppose a sorted array 'A' where we search for element with value 'k'. We can:
  
1. Iterate over the list as in previous example
2. *Recursively* search the array for the element and reducing the size of the array each time in half. This is called binary search.
  
    ```python
    def py_bs(l,key):
        if len (l) == 1: return l[0] == key
        pivot = len(l)//2
        if  l[:pivot][0] <= key:
            return py_bs(l[pivot:],key)
        return py_bs(l[:pivot],key)
  
    ##More standard binary search
    def bs(l, x, low, high):
        if high-low == 1:
            return l[high] == x
        mid = (low+high)//2
        if l[mid] == x:
            return True
        if l[mid]>= x:
            return bs(l,x,low,mid)
        else:
            return bs(l,x,mid,high)
  
![binary_search](./images/binary-search1.png)
  
Size | Operations
|-|-|
10|4|
100|7
1000|10|
1,000,000|20|
1,000,000,000|30|
  
In essence, binary search makes 1 operation, the comparison, then lessens the size of available array by half each time until there is only 1 element left. So if we were to start with 1024 elements, after 1 recursion, we would have 512 elements, then 256, 128, 64, 32, 16, 8, 4, 2, 1.
  
Since we are diving by 2 each time, we have $log_2$. As a result, with 1024 elements, we would have $log_21024$ or 10 operations.
  
So we conclude that quicksort $\in O(log_2n)$
  
## Analysing divide and conquer recursive algorithms
  
  
```python
    def py_bs(l,key):
        if len (l) == 1: return l[0] == key
        pivot = len(l)//2
        if  l[:pivot][0] <= key:
            return py_bs(l[pivot:],key)
        else:
            return py_bs(l[:pivot],key)
```
The function has 3 operations:
  
* ```if len (l) == 1```
* ```pivot = len(l)//2```
* ```if  l[:pivot][0] <= key```
  
The recursive function is:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?f(n)%20=%20f(n&#x2F;2)+3"/></p>  
  
The recursive condition is:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?f(1)%20=%201"/></p>  
  
  
Using substitution:
<img src="https://latex.codecogs.com/gif.latex?T(n)%20=%20T(n&#x2F;2)+3"/>
    <img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;4)+3%20+3"/>
    <img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;8)+3+3+3"/>
    <img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;16)+3+3+3+3"/>
    <img src="https://latex.codecogs.com/gif.latex?=1+3+.....+3%20=%201+%203*log_2n"/>
    <img src="https://latex.codecogs.com/gif.latex?&#x5C;to%201+3*log_2n%20&#x5C;in%20O(log_2n)"/>
  
In similar fashion, depending on the size of the segments we reduce our problem to, we have the equivalent logarithmic base.
  
