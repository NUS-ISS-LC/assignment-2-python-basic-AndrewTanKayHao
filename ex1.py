def find(s, n):
# write your implementation here
# assume s is the number list [] and n is the target int 
    for b in range(len(s)):
        for c in range(b+1, len(s)):
            if s[b]+s[c] == n:
                return [b, c]        
    return None
