### [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


**_Example 1:_**  
Input: people = [1,2], limit = 3  
Output: 1  
Explanation: 1 boat (1, 2)

**_Example 2:_**  
Input: people = [3,2,2,1], limit = 3  
Output: 3  
Explanation: 3 boats (1, 2), (2) and (3)  

**_Example 3:_**    
Input: people = [3,5,3,4], limit = 5  
Output: 4  
Explanation: 4 boats (3), (3), (4), (5)

_**Constraints:**_  
1 <= people.length <= 5 * 104  
1 <= people[i] <= limit <= 3 * 104