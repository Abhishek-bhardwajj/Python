n = int(input('Enter the number'))
temp = n
rev = 0
while(n>0):
    rem = n%10
    rev = (rev*10) + rem
    n = n//10

if(rev == temp):
    print('Palindrome number')
else:
    print('Not a palindrome number')
