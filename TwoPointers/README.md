# Two Pointers 

### Tags
#linkedlist #linked #list #twopointers #two #pointer
# Cycle Detection using Fast and Slow Pointer

## Detect if cycle exists

1. Initialize two pointers at the head ( slow pointer and fast pointer) and perform the following operations
2. Repeat while fast pointer is not null and next node of fast pointer is not null
    1. Move the slow pointer by one node.
    2. Move the fast pointer by two nodes.
    3. If the fast pointer and slow pointer are same, then there exists a cycle
3. If the fast pointer is null, there is no cycle and the pointer has reached the end of the list. 
   
### Example image to demonstrate the actions



## Node where cycle exists

1. Initialize two pointers at the head ( slow pointer and fast pointer) and perform the following operations
2. Repeat while fast pointer is not null and next node of fast pointer is not null
    1. Move the slow pointer by one node.
    2. Move the fast pointer by two nodes.
    3. if the fast pointer and slow pointer are same, then there exists a cycle. break at this point. 
3. If the fast pointer is null, there is no cycle and the pointer has reached the end of the list. no cycle exists
4. Else we need initialize the fast pointer to head.
5. While fast pointer is not equal to slow pointer
   1. Move fast pointer and slow pointer by 1 node.
6. Return the slow/fast pointer.

### Example image to demonstrate the actions