#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  i =0
  newlist=[]
  if not nums :
    return newlist
  length = len(nums)-1
  #print length
  while i < length:
    if nums[i] == nums[i+1]:
      #newlist.append(nums[i])
      #i+=1
      #print ''
      pass
    else:
      newlist.append(nums[i])
      #i+=1
    i+=1
  newlist.append(nums[i])
  return newlist


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  len1=len(list1)
  len2=len(list2)
  newlist=[]
  if not list1 or not list2 :
    return newlist
  if len1 < len2 :
    #print 'enter 1'
    i=0
    while i < len1 :
      if list1[i] < list2[i]:
        newlist.append(list1[i])
        newlist.append(list2[i])
      else:
        newlist.append(list2[i])
        newlist.append(list1[i])
      i+=1
    while i< len2 :
      newlist.append(list2[i])
      i+=1
    # index with len1
    #then add all the elements of len2
  else :
    #index with len2
    #then add all elements of len1
    i=0
    while i < len2 :
      if list1[i] < list2[i] :
        newlist.append(list1[i])
        newlist.append(list2[i])
      else:
        newlist.append(list2[i])
        newlist.append(list1[i])
      i+=1
    while i< len1 :
      newlist.append(list1[i])
      i+=1
    
  return newlist

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
