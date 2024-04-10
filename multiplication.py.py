def sum_mul(number, cap):
   if number <= 0 or cap <= 0:
     return "INVALID"
  multiples = 0
  sum_of_multiples =0
 while multiples < cap:
   multiples += number
   if multiples >= cap:
     break
    sum_of_multiples += multiples
reture sum_of_multiples
   #print(multiples, multiples >= cap)

print(sum_mul(1,10))