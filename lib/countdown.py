# your code goes here!
import time

def countdown (num):
    while num >= 1:
        print(f'{num} seconds to midnight!')
        num -= 1
    print('HAPPY NEW YEAR!')

def coundown_with_sleep( num ):
    while num >= 1:
        print(f"{num} seconds to midnight!")
        num -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')

coundown_with_sleep(10)