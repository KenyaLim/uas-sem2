def palindromeAsik(s,b):
    #s=s.replace(" "," ").lower()
    s=''.join(filter(str.isalpha,s))
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromeAsik(s[1:-1],b)
print(palindromeAsik("k!@!a#s()u$$rr#%u^s&%a*k",24))#true
print(palindromeAsik("#Al#p@!rO@*)A$sik*(k$is#A$O@r@$pl$!_A",37))#true
print(palindromeAsik("%#@$a$l%p#@rO%@S$u#@s!#a^h",26)) #false
print(palindromeAsik("_*ma$!k@!an%#%n%$@a%k!@an",25)) #false
