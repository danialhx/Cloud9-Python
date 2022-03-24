list = [1]

#loop prime
minimum = int(input("Please Enter the Minimum Value: "))
maximum = int(input("Please Enter the Maximum Value: "))

for Number in range (minimum, maximum + 1):
  count = 0
  for i in range(2, (Number//2+1)):
    if (Number % i ==0):
      count = count + 1
      break
      
  if (count == 0 and Number != 1):
    list.append(Number)
#will loop until maximum
#create list

#create file,write, join, string, list
with open('result.txt','w') as f:
  f.write(''.join(str(list)))
