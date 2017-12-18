# Readme

___

## About this repo

This repo consists of my notes of algorithms and datastructures classes taught in University of Cyprus.

The repo contains most, if not all content as taught in the classes along with accompanied code. For educational purposes, the code is written in python and/or C. Special cases and optimisations that are either not available in python or, are, to my knowledge impossible to implement, will be implemented only in C.

Example of this, is a double link linked list with only one (1) field for neighbouring elements.

## Content

0. [Lecture 0 - What are algorithms and their importance.](./Lectures/Compiled/Lecture-0.md)
1. [Lecture 1 - Big-O notation](./Lectures/Compiled/Lecture-1.md)
2. [Lecture 2 - Runtime analysis Examples](./Lectures/Compiled/Lecture-2.md)
3. [Lecture 3 - Abstract datatypes](./Lectures/Compiled/Lecture-3.md)

**Note :** The content and lectures above, are only those I have completed thus far. For a complete list of the content I am working on, checkout the [roadmap](#roadmap).

## Notes style

### Code

All code will be marked \`\`\`Language ...code... \`\`\` when the lecture is read in raw format. When viewed through Github and Pandoc, it will be color coded based on the language as such:

* Python
    ```Python
        class foo:
            def __init__(self):
                print("bar")
    ```
  * All Python code is written with Python 3.6
* C
    ```c
    #include <stdio.h>
    int main(void){
        char * foo = "bar";
        printf("%s",foo);
        return 0;
    }
    ```
  * All C code is Compiled with ```gcc 7.2.0``` and flags ```-Wall -pedantic``` on ```Manjaro Linux```.

### Roadmap

- [x] Write Lectures 0 - 3:

* [Lecture 0 - What are algorithms and their importance.](./Lectures/Compiled/Lecture-0.md)
* [Lecture 1 - Big-O notation](./Lectures/Compiled/Lecture-1.md)
* [Lecture 2 - Runtime analysis Examples](./Lectures/Compiled/Lecture-2.md)
* [Lecture 3 - Abstract datatypes](./Lectures/Compiled/Lecture-3.md)

- [x] Rewrite Readme.md
- [x] Move [Raw](./Lectures/Raw) and [Compiled](./Lectures/Compiled) lectures to their own folders.
- [ ] Fix some grammar/spelling mistakes as well as some formula visibility issues in Lectures 0-3.

__Write the following Lecture notes:__

- [ ] Lecture 4 - Stacks and Queues.
- [ ] Lecture 5 - Singly Linked Lists.
- [ ] Lecture 6 - Cyclical Lists, Space optimisations.
- [ ] Lecture 7 - Basic sorting algorithms.
- [ ] Lecture 8 - Advanced Sorting algorithms.
- [ ] Lecture 9 - Trees, definitions and operations.
- [ ] Lecture 10 - Binary Search Trees.
- [ ] Lecture 11 - Balanced Trees.
- [ ] Lecture 12 - AVL Trees, B-trees.
- [ ] Lecture 13 - 2-3 Trees, R-trees.
- [ ] Lecture 14 - Other trees.
- [ ] Lecture 15 - Recursion.
- [ ] Lecture 16 - Heaps.
- [ ] Lecture 17 - Heap sort.
- [ ] Lecture 18 - Heap operations.
- [ ] Lecture 19 - Graphs I.
- [ ] Lecture 20 - Graphs II - Prim's, Kruskal's.
- [ ] Lecture 21 - Graphs III - Minimum spanning Trees.
- [ ] Lecture 22 - Graphs IV - Dijkstra's algorithm , Euler graphs.
- [ ] Lecture 23 - Hashing I.
- [ ] Lecture 24 - Hashing II.
- [ ] Lecture 25 - Hashing Other hashing methods.
- [ ] Lecture 26 - Probabilistic datastructures.