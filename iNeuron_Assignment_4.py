# 1. What exactly is []?
# Ans 1. [] are the square brackets use for list.

# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# Ans 2.
spam = [2, 4, 6, 8, 10]
# spam[2]="hello"
# print(spam)


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# spam = [2, 4, 6, 8, 10,['a', 'b', 'c', 'd']]
# 3. What is the value of spam[int(int('3' * 2) / 11)]?
# Ans 3.
print(spam[int(int('3'*2)/11)]) # we are concatenating 3 with another 3 and then dividing it with 11 and then using the
# outcome of it (3) as the index in the list spam which gives us the value 8(which is at the 3rd index).

# 4. What is the value of spam[-1]?
# Ans 4.
# spam = [2, 4, 6, 8, 10,['a', 'b', 'c', 'd']]
# spam[-1] would be ['a', 'b', 'c', 'd']

# 5. What is the value of spam[:2]?
# Ans 5 print(spam[:2]) value is [2,4]

# Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.

# 6. What is the value of bacon.index('cat')?
bacon = [3.14, 'cat',11, 'cat',True]
# Ans 6. the index for cat is 1.

# 7. How does bacon.append(99) change the look of the list value in bacon?
# Ans 7).
#     bacon.append(99)
    # print(bacon)
    # 99 would be added in the end of the bacon list and would like this [3.14, 'cat', 11, 'cat', True, 99].

# 8. How does bacon.remove('cat') change the look of the list in bacon?
# Ans 8).bacon.remove('cat')
# print(bacon)
# the first cat will be removed but the second 'cat' in the list will still be there.
# this would be the outcome. [3.14, 11, 'cat', True].

# 9. What are the list concatenation and list replication operators?
# Ans9). The operator for list concatenation is +, while the operator for replication is *
# l = [1,2,3,4]
# l2 = [5,6,7,8]
# concat = l + l2
# replic = l *3

# 10. What is difference between the list methods append() and insert()?
# Ans 10)
# with append we can add any element at the end of the list, however with insert we can add any element at whichever index
# we want.

# 11. What are the two methods for removing items from a list?
# Ans 11) remove() and pop()
# 12. Describe how list values and string values are identical.
# Ans 12)They both are sequence.they both can be sliced
# 13. What's the difference between tuples and lists?
# Ans 13) tuples are immutable lists are mutable, we use () for tuple for list we have to use [].
# 14. How do you type a tuple value that only contains the integer 42?
# Ans 14) (42,) (comma is mandatory
# t = (42,)
# print(type(t))
# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# Ans 15) by passing the tuple in list() and list in tuple() functions.
# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# Ans 16) They contain references to the list.
# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
# Ans 17 copy.copy() will do a shallow copy of the function while in copy.deepcopy() it's doing deep copy, which means
# any changes in one 1item's element will not be done in the other item2 which was assigned to item 1.


