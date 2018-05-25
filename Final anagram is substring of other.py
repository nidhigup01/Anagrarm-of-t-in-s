# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:30:21 2018
https://codereview.stackexchange.com/questions/160127/checking-whether-any-anagram-of-a-string-appears-within-another-string
@author: nidhi
"""

#Given two strings s and t, determine whether some anagram of t is a substring of s. 
#For example: if s = "udacity" and t = "ad", then the function returns True. 
#Your function definition should look like: question1(s, t) and return a boolean True or False.



def question1(s, t):

  if len(s) < len(t) or len(t)<=1:
    return False
  
   #Intersection s&t : average O(min(len(s), len(t), worst O(len(s) * len(t))
  #print (set(t) & set(s))
  #print(set(t))
  if set(t)!= (set(t) & set(s)):    
      return False
  else:
      return True

# Test case with a space character.
print ('s= over fifty, t= forty/ Anagram of t is in s:', question1( "over fifty","forty"))
# True

# Test case with numbers.
print ('s= 36579, t= 37/ Anagram of t is in s:',question1("36579", "37"))
# True

# Test case where s is smaller than t.
print ('s= du, t= udacity/ Anagram of t is in s:',question1("du", "udacity"))
# False

# Test case where t is same alphabet twice.
print('s= stopped, t= pp/ Anagram of t is in s:',question1("stopped", "pp"))
# True
# Test case where t is single alphabet.
print('s= stopped, t= p/ Anagram of t is in s:',question1("stopped", "p"))
# False