import time
import random
Today=time.strftime("%A, %B %d")
RandomNumbers= random.choices(range(50,80),k=6)
print(f"The lucky numbers for {Today} are ---> {RandomNumbers}")
