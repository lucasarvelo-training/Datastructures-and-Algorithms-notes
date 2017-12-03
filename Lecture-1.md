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

* $\Theta$ is used to define an absolute bound for the algorithm. This means that the best and worst case of the algorithm are the same and the algorithm will never have a lower runtime.

* $\Omega$ is used to define a lower bound for the algorithm, such that the algorithm will never run faster than that.
* ${O}$ is used to define the upper bound for the algorithm, such that the algorithm will never run slower than that.

### Examples:

    i <- 0
    while(i < N)
        print i
        i++


This takes constant time, meaning that it always takes the same amount of time regardless of the size of our elements.

    i <- 0

Lets analyse the loop.

    while(i < N)
        print i

The loop repeats for  N times thus the loop has time complexity of $O(n) \times $ internal time complexity.

    print i

This is the internal of the loop. Printing i always takes the same amount of time thus the internal of the loop is $O(1)$.

Combining the loop and it's internal we find that our small algorithm has $O(n) {\times} O(1) = O(n)$ time complexity. 

A better way to show this is this:
$$T= \Sigma_{i=1}^n IL = \Sigma_{i=1}^n 1 = O(n) $$Where $T$ is the time complexity and $IL$ is the time complexity of inner loop.

This algorithm has total time complexity ``$O(1)+O(n) = O(n+1)$.``
Similarly to finding the limit of a function, big-O notation allows us to ignore constant numbers as they don't alter time complexity relative to the amount of elements. Moreover, multiplication constants are considered irrelevant in the grand scheme of things and are only to be considered when comparing algorithms with the same time complexity and in very time sensitive/critical applications.

Thus we can say that this algorithm is ${O(n)}$.
This algorithm is also $\Omega(n)$ because it will ***always*** run for n times,thus we can say that the algorithm has $\Theta(n)$ time complexity.
___

#### Finding the biggest element in a list

    l <- list
    max <- list[0]
    for ( i = 1, i < size(l), i++ )
        if max < l [i]
            max = l [i]

##### Inside the loop

|operation|time complexity|
|---------|---------------|
|if max < l [i] | $O(1)$
|max = l [i]|$O(1)$

##### All operations

| operation|Time Complexity |    
|--------|------------------|
|l <- list| ${O(1)}$|
|max <- list[0] | $O(1)$|
|for ( i = 1, i < size(l), i++ )| ${O(n) \times IL = \Sigma_{i=1}^n IL} = \Sigma_{i=1}^n 1 = O(n) $

Thus the algorithm is ${O(n)}$ and ${\Omega(n)}$ thus is ${\Theta(n)}$.

Suppose, instead of a randomized loop, we had an ascending sorted list. Instead of iterating over the list in ${\Theta(n)}$ and getting the biggest element we can simply get the last element ${\Theta(1)}$ as such.

    max <- last(l)

Or

    max <- l[size(l)-1]

Example 2:

    for( i = 0, i < n, i++ )
        for ( j = 0, j < i*i , j++)
            sum++

|operation| time complexity|
|-|-|
|Outer loop|${\Sigma_{i=1}^nInnerLoop}$|
|InnerLoop|${\Sigma_{j=1}^{i^2}1}$|

##### Inner Loop

|i | 0 | 1 | 2 | 3| ...| n-1|
|-|-|-|-|-|-|-|-|
|IL|0|1|4|9| ... | ${(n-1)^2}$

Thus, this double loop has ${\Theta(n*(n^2+2+1))=\Theta(N^3)}$ time complexity.

## Summarizing

When we use big-O notation:

* Constants are ignored
* We keep count basic operations and not their runtime.
* Only the function of the highest order is kept and the others are discarded.
* Environmental and other factors are ignored

![Big-O-chart](./images/big-O-chart.png)

## Non algorithmic examples of Big-O-notation

* ${7*n*lnn + n^2} = O(n^2)$
* ${20*n^3 + nlogn + 5 + 23n^2} = O(n^3)$

## Properties of big O

* ${O(X+Y) = O(X)+O(Y)} \in max(O(X),O(Y))$
* ${O(X*Y) = O(X)*O(Y) \in O(X*Y)}$
* ${O(cX) = O(X)}$

Let f(n) = ${16*n+20n^2 + 3logn + 8} = O(n + n^2 +logn +8) = O(n + n^2 + logn) = O(n^2) $

While O defines an upper bound, it's important for our bounds to be as tight as possible in order to have better accuracy.

For example, we could say that the previous examples, are $O(n^4)$, while that may be true, it doesn't provide us with a clear representation of the algorithm.

When designing or analysing an algorithm, we often focus on worst case scenario in order to find the upper bound of the algorithm.

## Worst Case

Let $D_n$ the possible combinations of all elements, $t(I)$ the number of basic operations for every $i \in D_n$. Thus the runtime of worse case is equal  to $max \{ t(I) | I \in D_n\}$.

## Calculating the average case

Suppose we have a probability **${p(I)}$** for each case ${I\in D_n}$. The average case for an algorithm equals to $${\Sigma_{i\in D_n} p(I) \times t(I)} $$