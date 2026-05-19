#Calculating sqrt of a number with the Babylonian Method
#Compatible with any positive real numbers

def babylonian_sqrt():
  #Ensuring number does not have alphabets
  break_fn = False
  while True:
    num = input("Enter a postive real number: ")
    if num.isdigit() == True:
      num = float(num)
      break
    else:
      if num.isalpha() == False and num.isdecimal() == False:
        num = float(num)
        break
  #Initialising values
  sqrt = 0
  smallest_diff = -1
  #Finding values to iterate with (mostly half of number)
  roots = list(range(0,(round(num // 2))))
  roots.append(num//2)
  #making a dictionary of keys as squares and values as roots
  squares = list(map((lambda x:x**2),roots))
  correspond = dict(zip(squares,roots))
  #special case for 0 and 1
  if num == 1 or num == 0:
    sqrt = num
  if num in squares:
    sqrt = correspond[num]
  #finding distance of which square is num closes to in mumber line both ways
  else:
    smallest_diff = squares[-1]
    for i in squares:
      if abs(num-i) <= smallest_diff:
        smallest_diff = abs(num-i)
  #finding which square is num closes to in number line both ways
  if (num - smallest_diff) in squares:
    closest_square = num - smallest_diff
  elif (num + smallest_diff) in squares:
    closest_square = num + smallest_diff
  if num != 1 and num != 0 and sqrt == 0:
    while True:
      #giving choice to rounding accuracy
      global dp
      dp = input("How many decimal places to round to? ")
      if dp.isdigit() == True:
        dp = int(dp)
      break
    #finding highest square smaller than or equal to number
    if closest_square > num:
      highest_lower_square = (correspond[closest_square] - 1)**2
    else:
      highest_lower_square = closest_square
   #babylonian method
    highest_lower_root = correspond[highest_lower_square]
    def artifical_sqrt(num,highest_lower_root):
      sqrt = highest_lower_root + (num - highest_lower_root**2) / (2*highest_lower_root)
      return sqrt
    sqrt = artifical_sqrt(num,highest_lower_root)
    #iterate for more accuracy
    for i in range(3):
      sqrt = artifical_sqrt(num,sqrt)
  #special case for 0 and 1
  if sqrt == 1.0 or sqrt == 0.0:
    sqrt = int(sqrt)
  return round(sqrt,dp)
