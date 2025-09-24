# Create a simple countdown timer using a while loop.

'''
Write a code to create a simple countdown timer of 5 seconds using a while loop.

Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
'''

import time

def contador(segundos):
    while segundos > 0:
        print('Time remaining: ', segundos, ' seconds')
        time.sleep(1)
        segundos -= 1

    print("Time's up!")

contador(10)