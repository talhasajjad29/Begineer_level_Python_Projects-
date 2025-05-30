def is_prime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
print("prime numbers:")   
for number in range(1,101):
     if is_prime(number):
          print(number,end=" ")
print("\nThe number reaches to 100")
         
