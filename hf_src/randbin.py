# Python program for random
# binary string generation
  
  
import random
  
  
# Function to create the
# random binary string
def rand_key(p):
    
    # Variable to store the 
    # string
    key1 = ""
  
    # Loop to find the string
    # of desired length
    for i in range(p):
          
        # randint function to generate
        # 0, 1 randomly and converting 
        # the result into str
        temp = str(random.randint(0, 1))
  
        # Concatenatin the random 0, 1
        # to the final result
        key1 += temp
          
    return(key1)
  
# Driver Code
n = 521
str1 = rand_key(n)
print("Desired length random binary string is: ", str1)

