import random

# we need to get a random item from the following list
friends_list = ["Ahmed", "Mohamed", "Ali"]

# Option1: random.choice() which take a list as input
print(random.choice(friends_list))

# Option2: get random int then use it as index
random_index = random.randint(0, len(friends_list)-1)
print(friends_list[random_index])