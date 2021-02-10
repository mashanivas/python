#!/usr/bin/python

def ask_ok(prompt, retries=9, reminder='Please try again!'):
   while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop'):
            return False
        retries = retries - 1
        if retries < 5:
             raise ValueError('invalid user response')
        print(reminder)
ask_ok("Enter input: ", retries=9, reminder='Please try again!')
