# if then else
a = 33
b = 34
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


is_hot = False
is_cold = False
if is_hot:
  print("It's a hot day")
  print("Dring plenty of water")
elif is_cold:  
  print("it's a cold day")
  print("wear warm clothes")
else:
  print("It's a lovely day")
  print("Enjoy Your Day")


price = 2500000
has_good_credit = False

if has_good_credit:
  down_payment = 0.1 * price
else:
  down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")    

# # while
a = 1
while a < 6:
  print(a)
  a += 1

i = 1
while i <= 5:
  print('*' * i)
  i = i + 1


# # for 
for x in range(1,6):
  print(x)

for x in range(1,11,2):
  print(x)  

for item in 'Python':
  print(item)

for item in ['Mosh','John','Sarah','George']:
  print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
  total += price
print(f"total : {total}")