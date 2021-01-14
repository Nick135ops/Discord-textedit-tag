import sys
import clipboard
print('Your text', end=''); message = str(input(': '))

MAGIC_CHAR = '\u202b'

res = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'

clipboard.copy(res)
print("\nSuccessfully Copied Text To Clipboard\nEnter Any Key To Exit...", end = "")

input()
print()
