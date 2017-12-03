# Lecture 0
  
  
## Algorithms
  
  
### Defining algorithms
  
  
An algorithm is a series of actions such that they yield a result or an effect.
  
### What defines a good algorithm?
  
  
First and foremost, for an algorithm to be good, it first has to complete some criteria, ex:
  
* Sort an array in ascending or descending order
* Navigate a datastructure in a specific way
* Find pair of values in an array
* Print a message
  
If an algorithm does not fill the criteria for which it was written then it is of no use.
  
**What makes it a good algorithm, is it's efficiency in space and time.**
  
Depending on a situation, a slower algorithm may be preferred over a faster algorithm that consumes more space. Moreover in some cases, where the dataset cannot be contained in the memory and disk operations are required, an algorithm that is slower but has less disk operations is preferred over a faster with a lot more operations.
  
### The basis of a good algorithm is the underline structure of the data and their relationships
  
  
>…git actually has a simple design, with stable and reasonably well-documented data structures. In fact, I'm a huge proponent of designing your code around the data, rather than the other way around, and I think it's one of the reasons git has been fairly successful […] I will, in fact, claim that the difference between a bad programmer and a good one is whether he considers his code or his data structures more important. Bad programmers worry about the code. Good programmers worry about data structures and their relationships.
>
>Torvalds, Linus (2006-06-27). Message to Git mailing list. Retrieved on 2006-08-28.
  
Suppose you have 1 million numbers where: <img src="https://latex.codecogs.com/gif.latex?x&#x5C;epsilon[0,100]"/>. And you are tasked to sort them.
  
The most simple but naive way is to start from the end and go towards the start, picking the smallest number and putting them to the front each time. This is the bubble sort algorithm. Bubblesort has <img src="https://latex.codecogs.com/gif.latex?{O(n^2)}"/> time complexity. This means that in the worse case - when the array is sorted in reverse - in this scenario, we have to do <img src="https://latex.codecogs.com/gif.latex?1,000,000%20^%202%20=%201,000,000,000,000%20=%2010^{12}%20=%201"/> trillion comparisons.
  
A more efficient algorithm is the mergesort. Where the array is split into smaller and smaller arrays each time until only 1 number remains, then the arrays are merged together. Mergesort has <img src="https://latex.codecogs.com/gif.latex?{O(n%20&#x5C;times%20log_2n)}"/> time complexity, thus, the worst case of mergesort in this scenario requires:<img src="https://latex.codecogs.com/gif.latex?{1,000,000%20&#x5C;times%20log_21,000,000%20=%2010^6*19.931569%20=%2010^7*2}"/> comparisons.
  
An even faster way is using bucket sort. Bucketsort counts how many times each value is found within the array and then recreates the array sorted. Bucketsort has <img src="https://latex.codecogs.com/gif.latex?{O(n)}"/> time complexity, meaning that in this scenario,it will have to do: <img src="https://latex.codecogs.com/gif.latex?{1,000,000%20=%2010^6}"/> operations.
  