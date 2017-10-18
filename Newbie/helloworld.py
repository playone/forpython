
import os
# import library 'os'
def main():
    print 'Hello World'
#Basic print command
    print "This is safe speaking"
    print 'I want to be\'s a tester'
#Single quote or double quote is good for print strings
    foo(5, 10)
#call function 'foo'
    print '=' *10
#string replicatio. *10 will print 10 times
    print 'Current working directory is ' + os.getcwd()
#Concatnation string with function os.getcwd() from os.py

    counter = 0
    counter += 1

    food = ['apple','meet','egg']
    print food
#varible can be array and assign value
    for i in food: # for loop. use : to end the description. for loop will print the array 'food'
        print 'I like to eat ' + i #for loop with a concatnation string

    print 'count to ten'
    for i in range(10): #for loop and in the range. it will count from 0 to 9
        print i


def foo(param1, secondparam): #define function 'foo', don't forget : in the end
  res = param1 + secondparam #use '=' to assign value

  print '%s plus %s is equal to %s' % (param1, secondparam, res)
#String interpolation % works basically the same as it does in C
  if res < 50:
    print 'foo'
#The compairison operators are same as C
  elif (res >= 50) and ((param1 == 42) or (secondparam == 24)):
    print 'bar'
# Boolean operators are words, not && ||, etc.
  else:
    print 'moo'

  return res
# THIS IS THE COMMENT FOR COMMENT BY USING #
'''THIS IS COMMENT FOR MULTIPLE LINE, 
YOU CAN USE 3 SINGLE QUOTE TO DEFINE IT'''
if __name__ == '__main__':
    main()

# DEMO CODE COME FROM http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute