# Hashmap LEFT JOIN

We were assigned the task to implement a simplified LEFT JOIN for two hashmaps. One of examples that we were given were certain words with their accompanied synonym and antonym.

## Challenge

- First we were challenged to write a function called left join that takes two hash maps

- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.

- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

- The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

And some other things to remember:

- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.

- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.

- If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Approach & Efficiency

The approach that I took was to create an empty list and append the key with the left value pairs. With a for loop, I created a conditional. If the key of the left hashmap matched the key of the right hashmap, it would append the right value. Otherwise return None, or null.

Big(O):
time: O(n) (time efficiency can be infinite because we can set how many key value pairs)
space: O(1)

## Solution

![White Board](./images/whiteboard.png)
