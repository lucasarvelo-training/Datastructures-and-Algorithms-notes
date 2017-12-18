# Lecture 1
  
  
## Complexity
  
  
Complexity analysis allows us to calculate mathematically the speed of an algorithm relative to the size of the data.
Theoretical time analysis has the following benefits:
  
* Programmer independent
* Programming language independent
* Hardware independent
* Does not require implementation of the algorithm
  
There are two ( 2 ) types of complexity analysis, time and space and are analysed using big-O notation.
  
Big-O notation allows us to define an upper, a lower and an absolute bound to the algorithm relative to the amount of elements we have.
  
* <img src="https://latex.codecogs.com/gif.latex?&#x5C;Theta"/> is used to define an absolute bound for the algorithm. This means that the best and worst case of the algorithm are the same and the algorithm will never have a lower runtime.
  
* <img src="https://latex.codecogs.com/gif.latex?&#x5C;Omega"/> is used to define a lower bound for the algorithm, such that the algorithm will never run faster than that.
* <img src="https://latex.codecogs.com/gif.latex?{O}"/> is used to define the upper bound for the algorithm, such that the algorithm will never run slower than that.
  
### Examples:
  
  
```python
for x in range(n)
    print(x)
```
  
The loop repeats for  N times thus the loop has time complexity of <img src="https://latex.codecogs.com/gif.latex?O(n)%20&#x5C;times"/> internal time complexity.
  
```python
    print(x)
```
  
This is the internal of the loop. Printing x always takes the same amount of time thus the internal of the loop is <img src="https://latex.codecogs.com/gif.latex?O(1)"/>.
  
Combining the loop and it's internal we find that our small algorithm has <img src="https://latex.codecogs.com/gif.latex?O(n)%20{&#x5C;times}%20O(1)%20=%20O(n)"/> time complexity. 
  
A better way to show this is this:
<img src="https://latex.codecogs.com/gif.latex?T=%20&#x5C;Sigma_{i=1}^n%20IL%20=%20&#x5C;Sigma_{i=1}^n%201%20=%20O(n)"/>
Where <img src="https://latex.codecogs.com/gif.latex?T"/> is the time complexity and <img src="https://latex.codecogs.com/gif.latex?IL"/> is the time complexity of inner loop.
  
This algorithm has total time complexity <img src="https://latex.codecogs.com/gif.latex?O(1)+O(n)%20=%20O(n+1)"/>.
Similarly to finding the limit of a function, big-O notation allows us to ignore constant numbers as they don't alter time complexity relative to the amount of elements. Moreover, multiplication constants are considered irrelevant in the grand scheme of things and are only to be considered when comparing algorithms with the same time complexity and in very time sensitive/critical applications.
  
Thus we can say that this algorithm is <img src="https://latex.codecogs.com/gif.latex?{O(n)}"/>.
This algorithm is also <img src="https://latex.codecogs.com/gif.latex?&#x5C;Omega(n)"/> because it will ***always*** run for n times,thus we can say that the algorithm has <img src="https://latex.codecogs.com/gif.latex?&#x5C;Theta(n)"/> time complexity.
___
  
#### Finding the biggest element in a list
  
  
```python
max_value = l[0]
for i in l:
    if max_value <i:
        max_value = i
```
  
##### Inside the loop
  
  
|operation|time complexity|
|---------|---------------|
|if max < l [i] | <img src="https://latex.codecogs.com/gif.latex?O(1)"/>
|max = l [i]|<img src="https://latex.codecogs.com/gif.latex?O(1)"/>
  
##### All operations
  
  
| operation|Time Complexity |    
|--------|------------------|
|l <- list| <img src="https://latex.codecogs.com/gif.latex?{O(1)}"/>|
|max <- list[0] | <img src="https://latex.codecogs.com/gif.latex?O(1)"/>|
|for ( i = 1, i < size(l), i++ )| <img src="https://latex.codecogs.com/gif.latex?{O(n)%20&#x5C;times%20IL%20=%20&#x5C;Sigma_{i=1}^n%20IL}%20=%20&#x5C;Sigma_{i=1}^n%201%20=%20O(n)"/>
  
Thus the algorithm is <img src="https://latex.codecogs.com/gif.latex?{O(n)}"/> and <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Omega(n)}"/> thus is <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Theta(n)}"/>.
  
Suppose, instead of a randomized loop, we had an ascending sorted list. Instead of iterating over the list in <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Theta(n)}"/> and getting the biggest element we can simply get the last element <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Theta(1)}"/> as such.
  
```python
    max_val = l[len(l)-1] 
```
  
  
Example 2:
```python
for i in range(n):
    for j in range(i*i):
        sum++
```
  
|operation| time complexity|
|-|-|
|Outer loop|<img src="https://latex.codecogs.com/gif.latex?{&#x5C;Sigma_{i=1}^nInnerLoop}"/>|
|InnerLoop|<img src="https://latex.codecogs.com/gif.latex?{&#x5C;Sigma_{j=1}^{i^2}1}"/>|
  
##### Inner Loop
  
  
|i | 0 | 1 | 2 | 3| ...| n-1|
|-|-|-|-|-|-|-|-|
|IL|0|1|4|9| ... | <img src="https://latex.codecogs.com/gif.latex?{(n-1)^2}"/>
  
Thus, this double loop has <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Theta(n*(n^2+2+1))=&#x5C;Theta(N^3)}"/> time complexity.
  
## Summarizing
  
  
When we use big-O notation:
  
* Constants are ignored
* We keep count basic operations and not their runtime.
* Only the function of the highest order is kept and the others are discarded.
* Environmental and other factors are ignored
  
![Big-O-chart](./images/big-O-chart.png )
  
## Non algorithmic examples of Big-O-notation
  
  
* <img src="https://latex.codecogs.com/gif.latex?{7*n*lnn%20+%20n^2}%20=%20O(n^2)"/>
* <img src="https://latex.codecogs.com/gif.latex?{20*n^3%20+%20nlogn%20+%205%20+%2023n^2}%20=%20O(n^3)"/>
  
## Properties of big O
  
  
* <img src="https://latex.codecogs.com/gif.latex?{O(X+Y)%20=%20O(X)+O(Y)}%20&#x5C;in%20max(O(X),O(Y))"/>
* <img src="https://latex.codecogs.com/gif.latex?{O(X*Y)%20=%20O(X)*O(Y)%20&#x5C;in%20O(X*Y)}"/>
* <img src="https://latex.codecogs.com/gif.latex?{O(cX)%20=%20O(X)}"/>
  
Let f(n) = <img src="https://latex.codecogs.com/gif.latex?{16*n+20n^2%20+%203logn%20+%208}%20=%20O(n%20+%20n^2%20+logn%20+8)%20=%20O(n%20+%20n^2%20+%20logn)%20=%20O(n^2)"/>
  
While O defines an upper bound, it's important for our bounds to be as tight as possible in order to have better accuracy.
  
For example, we could say that the previous examples, are <img src="https://latex.codecogs.com/gif.latex?O(n^4)"/>, while that may be true, it doesn't provide us with a clear representation of the algorithm.
  
When designing or analysing an algorithm, we often focus on worst case scenario in order to find the upper bound of the algorithm.
  
## Worst Case
  
  
Let <img src="https://latex.codecogs.com/gif.latex?D_n"/> the possible combinations of all elements, <img src="https://latex.codecogs.com/gif.latex?t(I)"/> the number of basic operations for every <img src="https://latex.codecogs.com/gif.latex?i%20&#x5C;in%20D_n"/>. Thus the runtime of worse case is equal  to <img src="https://latex.codecogs.com/gif.latex?max%20&#x5C;{%20t(I)%20|%20I%20&#x5C;in%20D_n&#x5C;}"/>.
  
## Calculating the average case
  
  
Suppose we have a probability **<img src="https://latex.codecogs.com/gif.latex?{p(I)}"/>** for each case <img src="https://latex.codecogs.com/gif.latex?{I&#x5C;in%20D_n}"/>. The average case for an algorithm equals to <p align="center"><img src="https://latex.codecogs.com/gif.latex?{&#x5C;Sigma_{i&#x5C;in%20D_n}%20p(I)%20&#x5C;times%20t(I)}"/></p>  
  
  