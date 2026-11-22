num=int(input("enter a number")
temp=0
rev=0
while num>0
  digit=num%10
  rev=rev*10+digit
  num=num//10
if temp==rev:
  print("palindrome number")
else:
  print("Not a palindrome")
