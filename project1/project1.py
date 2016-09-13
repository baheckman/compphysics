import math

#################################### NUMBER 1 ####################################
def integrate(a, b):
  if (a == float("-inf")):
    a = -4.0
  if (b == float("inf")):
    b = 4.0

  dx = (b-a)/1000.0
  i = int(abs((b-a)/dx))
  n = 0
  area = 0
  x = a
  while n < i:
      dA = math.exp((-1.0)*(x**2.0)) * dx
      x += dx
      area += dA
      n += 1
  print abs(area)

##################################################################################

#################################### NUMBER 2 ####################################
# find all primes between 2 and n (1 is not a prime)
def print_primes():
  print "Please enter a variable, N"
  n = input()
  prime_count = 0
  for num in range(2, n):	# must be > 1 to be prime
	if is_prime(num):
          prime_count += 1
	  print num
  print "There are ", prime_count, " prime numbers between 1 and ", n

def is_prime(n):
  for i in range(2, int(math.ceil(math.sqrt(n)))+1):	# +1 because 2nd value is exclusive
    if n % i is 0 and n is not i:
      return False
  return True
##################################################################################

print_primes()
integrate(float("-inf"), float("inf"))
