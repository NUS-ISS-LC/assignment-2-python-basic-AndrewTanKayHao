def find(s, n):
# write your implementation here
# O(n) assume s is the number list [] and n is the target int 
    seenNumbersDictionary = {}
    for i, num in enumerate(s):
        complementNumber = n - num
        if complementNumber in seenNumbersDictionary:
            return [complementNumber, seenNumbersDictionary[complementNumber]]
        seenNumbersDictionary[num] = i        
    return None

# O(n2) assume s is the number list [] and n is the target int, returns indices
#    for b in range(len(s)):
#        for c in range(b+1, len(s)):
#            if s[b]+s[c] == n:
#                return [b, c]        
#    return None