import random

def random_num():
    r = random.choices([1,2])
    return int(r[0])
  
random_num()
