a='radar'
b='madhu'

print(type(a),type(b))

#Check - palindrome 
if a==a[::-1]:
    print(a + ' is a palindrome')
else:
    print(a + ' is not palindrome')
    if b==b[::-1]:
        print(b + ' is a palindrome')
    else:
        print(b + ' is not palindrome')