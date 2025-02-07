
num_lst = [1,2,1,3]
# Sum Function
print(f"Built-in sum : {sum(num_lst)} ") # built-in sum function

# our sum function
Sum =0
for i in num_lst:
    Sum += i
print(f"Our sum loop result: {Sum}")
##############################
# Max function
print(f"Built-in max : {max(num_lst)}")

# our max function
Max = 0
for i in num_lst:
    if Max <= i:
        Max = i
print(f"Our sum loop result: {Max}")



