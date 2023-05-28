
# input 
mode = 17 # use

# Original message
X = 16

message = c(1, 2, 3,
            4, 5, 6,
            7, 8,9,
            0, 1, 2,
            3, 4, 5)

index = c(1:length(message))

sum(message*index)


c = 3


# Lemma 2
message_prime = c(message,c)
index_prime = c(1:length(message_prime))

sum(message_prime*index_prime) 

sum(message_prime*index_prime) %% 11


# Hash function: compute c 
h = function(message, mode){
  sum = 0
  for(i in 1:length(message)){
    sum = sum + message[i]*i
  }
  return(sum %% mode)
}


# Ready message: add c to original message
message_togo = c(message, h(message,mode))


# Check if message is valid
validate_message = function(message, mode){
  sum = 0
  for(i in 1:length(message)){
    sum = sum + message[i] * i
  }
  return((sum %% mode) == 0) # 0 is important 
  
}
validate_message(message_togo, mode)

# proof #

# invalid message 
message_invalid = c(1, 2, 3,
                    4, 5, 6,
                    7, 8, 9,11,
                    h(message,mode))


validate_message(message_invalid, mode)




D_prime = (1:n)
# actual message 
m = c(1, 2, 3,
      4, 5, 6,
      9, 8, 9)



# digit checker
X = sum(m*D) %% mode

# Receieved message
m_prime = c(m,X)


## Compute


# Definition
print("Actual m: should be 0")
(sum(m*D)+ n*X) %% mode

print("Received m")
(sum(m_prime*D_prime)) %% mode


## Note ISBN10

#sum 
m = c(1, 2, 3,
      4, 5, 6,
      7, 8,9)

n = length(m) + 1

mode = 11 

# Hash function: compute c 
sum_all = function(message, mode){
  sum = 0
  for(i in 1:length(message)){
    sum = sum + message[i]*i
  }
  return(sum)
}



((sum_all(m) %% mode)*n + sum_all(m) ) %% mode



## Note ISBN13
m = c(1, 2, 3,
      4, 5, 6,
      7, 8,9,
      9,9,9,
      9)

n = length(m) + 1

mode = 10

# Hash function: compute c 
sum_all = function(message, mode){
  sum = 0
  for(i in 1:length(message)){
    if(i %% 2 == 0){
      sum = sum + message[i]*3
    }else{
      sum = sum + message[i]
    }
    
  }
  return(sum)
}


sum_all(m) %% mode
c = sum_all(m) %% mode
# should always equal to 0 
(sum_all(m) + c*n) %% mode

