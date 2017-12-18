# Lecture 1
  
  
___
Contents:
* [Complexity Analysis](#complexity-analysis )
  * [Examples](#examples )
* [Summary](#summarizing )
* [Non algorithmic examples of Big-O-notation](#non-algorithmic-examples-of-big-o-notation )
* [Properties of big O](#properties-of-big-o )
* [Worst case](#worst-case )
  * [Data Permutations](#data-permutations-and-worst-case-scenario )
___
  
## Complexity Analysis
  
  
Complexity analysis allows us to calculate mathematically properties of an algorithm relative to the volume of the data.
Theoretical time analysis has the following benefits:
  
* Programmer independent
* Programming language independent
* Hardware independent
* Does not require implementation of the algorithm
  
There are two ( 2 ) types of complexity analysis, time and space. They are analysed using big-O notation.
  
Big-O notation allows us to define an upper, a lower and an absolute bound to the algorithm relative to the volume of elements.
  
* <img src="https://latex.codecogs.com/gif.latex?&#x5C;Theta"/> is used to define an absolute bound for the algorithm. This means that the best and worst case of the algorithm are the same and the algorithm will never have a lower runtime.
  
* <img src="https://latex.codecogs.com/gif.latex?&#x5C;Omega"/> is used to define a lower bound for the algorithm, such that the algorithm will never run faster than that.
* <img src="https://latex.codecogs.com/gif.latex?{O}"/> is used to define the upper bound for the algorithm, such that the algorithm will never run slower than that.
  
__Important:__ Big O notation isn't a function that gives us the number of operations the algorithm has to execute but instead gives us the order of the total operations. This will be covered later.
  
### Examples
  
  
```C
int n = 10;
for (int i = 0; i <n;i++)
    print(i);
```
  
The loop repeats for  N times thus the loop has time complexity of <img src="https://latex.codecogs.com/gif.latex?O(n)%20&#x5C;times"/> _internal complexity_.
  
```C
print(i);
```
  
This is the internal of the loop.
  
Printing(x) always takes the same amount of time. For this reason, we can say that it requires __constant time__.
  
Using Big-O we denote __constant time complexity__ as <img src="https://latex.codecogs.com/gif.latex?&#x5C;Theta%20(1)"/>.
  
Combining the loop and it's internal, the algorithm has <img src="https://latex.codecogs.com/gif.latex?O(n)%20{&#x5C;times}%20O(1)%20=%20O(n)"/> time complexity.
  
A better way to show this is this:
<img src="https://latex.codecogs.com/gif.latex?T=%20&#x5C;Sigma_{i=1}^n%20IL"/>
Where <img src="https://latex.codecogs.com/gif.latex?T"/> is the total time complexity, <img src="https://latex.codecogs.com/gif.latex?IL"/> is the time complexity of inner loop.
  
```C
int n = 10;
```
  
Also takes Constant time.
  
This algorithm has total time complexity <img src="https://latex.codecogs.com/gif.latex?O(n)+O(1)%20=%20O(n)"/>.
  
Similarly to finding the limit of a function, big-O notation allows us to ignore constant numbers as they don't alter time complexity relative to the amount of elements.
  
Moreover, multiplications of constants are considered irrelevant in the grand scheme of things and are only to be considered when comparing algorithms with the same time complexity and in __very__ time sensitive / critical applications.
  
Thus we can say that this algorithm is <img src="https://latex.codecogs.com/gif.latex?{O(n)}"/>.
  
This algorithm is also <img src="https://latex.codecogs.com/gif.latex?&#x5C;Omega(n)"/> because it will ***always*** run for <img src="https://latex.codecogs.com/gif.latex?n"/> times. As a result, we say that the algorithm has <img src="https://latex.codecogs.com/gif.latex?&#x5C;Theta(n)"/> time complexity.
___
  
#### Finding the biggest element in an array
  
  
```C
int max = array[0];
for (int index = 0;index < n; index++)
    if (max < array[index])
        max = array[index];
```
  
##### Inside the loop
  
  
|operation|time complexity|
|---------|---------------|
|if (max < array[index]) | <img src="https://latex.codecogs.com/gif.latex?O(1)"/> |
|max = array[index] |<img src="https://latex.codecogs.com/gif.latex?O(1)"/> |
  
##### All operations
  
  
| operation|Time Complexity |
|--------|------------------|
|```for (int index = 0; index < n; index++)```| $\Sigma_{i=1}^n 1 = O(n) $|
  
Thus the algorithm is $O(n)$ and $\Omega(n)$ therefor, is also $\Theta(n)$.
  
Suppose, instead of a randomized loop, we had an ascending sorted list. Instead of iterating over the list in ${\Theta(n)}$ and getting the biggest element we can simply get the last element in ${\Theta(1)}$ as such.
  
```C
    int max_val = array[n-1]
```
  
Example 2:
  
```python
sum = 0
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
|-|-|-|-|-|-|-|
|IL|0|1|4|9| ... | <img src="https://latex.codecogs.com/gif.latex?{(n-1)^2}"/>|
  
Thus, this double loop has <img src="https://latex.codecogs.com/gif.latex?{&#x5C;Theta(n*n^2)=&#x5C;Theta(n^3)}"/> time complexity.
  
## Summarizing
  
  
When we use big-O notation:
  
* Constants are ignored
* We keep count basic operations and not their runtime.
* Only the function of the highest order is kept and the others are discarded.
* Environmental and other factors are ignored
  
![Big-O-chart](../../images/big-O-chart.png )
  
## Non algorithmic examples of Big O notation
  
  
* <img src="https://latex.codecogs.com/gif.latex?{7*n*lnn%20+%20n^2}%20=%20O(n^2)"/>
* <img src="https://latex.codecogs.com/gif.latex?{20*n^3%20+%20nlogn%20+%205%20+%2023n^2}%20=%20O(n^3)"/>
  
## Properties of big O
  
  
* <img src="https://latex.codecogs.com/gif.latex?{O(X+Y)%20=%20O(X)+O(Y)}%20&#x5C;in%20max(O(X),O(Y))"/>
* <img src="https://latex.codecogs.com/gif.latex?{O(X*Y)%20=%20O(X)*O(Y)%20&#x5C;in%20O(X*Y)}"/>
* <img src="https://latex.codecogs.com/gif.latex?{O(cX)%20=%20O(X)}"/>
  
Let <img src="https://latex.codecogs.com/gif.latex?f(n)%20=%2016*n+20n^2%20+%203logn%20+%208"/> <img src="https://latex.codecogs.com/gif.latex?=%20O(n%20+%20n^2%20+logn%20+8)"/> <img src="https://latex.codecogs.com/gif.latex?=%20O(n%20+%20n^2%20+%20logn)%20=%20O(n^2)"/>
  
While O defines an upper bound, it's important for our bounds to be as tight as possible in order to have better accuracy.
  
For example, we could say that the previous examples, are <img src="https://latex.codecogs.com/gif.latex?O(n^4)"/>, while that may be true, it doesn't provide us with a clear representation of the algorithm.
  
When designing or analysing an algorithm, we often focus on worst case scenario in order to find the upper bound of the algorithm.
  
## Worst Case
  
  
Suppose the following algorithm:
  
```C
    //The define below is there for the sake of completeness only.
  
    #define print(x) printf("%d\n",x)
  
    for (int i = 1; i <=n; i+=1)
        if (i%2) // the same as i%2==1
            for (int j = 0;j < i; j++)
                print(j);
        else
            print(i);
```
  
Common sense is to say that half the time, the algorithm runs in <img src="https://latex.codecogs.com/gif.latex?O(n)"/> and the other half in <img src="https://latex.codecogs.com/gif.latex?O(n^2)"/>. While that may be true, it doesn't properly describe the order of operations.
  
The above algorithm is in the order of <img src="https://latex.codecogs.com/gif.latex?O(n^2)"/>, when we evaluate a pair or a set of functions in the same block, we keep the operation of highest order, in this case, our 2 operations in the block are of order <img src="https://latex.codecogs.com/gif.latex?O(1)"/> and <img src="https://latex.codecogs.com/gif.latex?O(n)"/>, thus,  time complexity of the block is equal to <img src="https://latex.codecogs.com/gif.latex?max&#x5C;{O(1),O(n)&#x5C;}"/> <img src="https://latex.codecogs.com/gif.latex?=O(n)"/>.
  
### Data permutations and worst case scenario
  
  
Let <img src="https://latex.codecogs.com/gif.latex?D_n"/> the possible combinations of all elements, <img src="https://latex.codecogs.com/gif.latex?t(I)"/> the number of basic operations for every <img src="https://latex.codecogs.com/gif.latex?i%20&#x5C;in%20D_n"/>. Thus the runtime of worse case is equal  to <img src="https://latex.codecogs.com/gif.latex?max%20&#x5C;{%20t(I)%20|%20I%20&#x5C;in%20D_n&#x5C;}"/>.
  
When we evaluate an algorithm for it's worst case performance, we also have to consider the possible permutations of the data.
  
For example, when an array is sorted, bubblesort runs in <img src="https://latex.codecogs.com/gif.latex?O(n)"/>, when it's sorted in __reverse__, it runs in <img src="https://latex.codecogs.com/gif.latex?O(n^2)"/>. Because we only consider the worst case, we see that time complexity of bubble sort is equal to <p align="center"><img src="https://latex.codecogs.com/gif.latex?max&#x5C;{t_{sorted},t_{reverse}&#x5C;}=%20t_{reverse}%20=%20O(n^2)"/></p>  
  
  