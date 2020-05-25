import random
n = random.randint(1, 100)
print('See how if you can guess my number in as few guesses as possible')
while True:
    ans = int(input('Enter your guess:'))
    if ans == n:
        print('Success! You Win.')
        continue                               # I want this to grab a new number
    elif ans > n:
        print('Too High.')
    else:
        print('too Low.')





