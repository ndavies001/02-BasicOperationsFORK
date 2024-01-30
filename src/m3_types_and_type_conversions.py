import math
print (type(3.14))
###############################################################################
# DONE: 1. (3 pts)
#   Every object has a TYPE and a VALUE.  For example,
#   for the object that is computed by  math.sqrt(2):
#      Its TYPE is float  (which is shorthand for "floating point number")
#      Its VALUE is (approximately) 1.4142135623730951.
#
#   The TYPE of an object is important because it determines:
#      -- what the object KNOWS, and
#      -- what the object can DO.
#
#   The   type   function returns the TYPE of its argument.  For example,
#       type(3.14)    returns the CLASS (synonym for TYPE) 'float'
#   and so the code:
#       print(type(3.14))
#   will print     <class 'float'>
#   Try it now!
#   (Just write   print(type(3.14))   below this _TODO_ and run the program.)
#
#   Now go through the BLAH objects listed below.  For each:
#      -- Try to GUESS its TYPE.
#      -- Write code of the form   print(type(BLAH)).
#      -- RUN the code to LEARN its TYPE.
#
#       "hello"
print (type("hello"))
#       'hello'
print (type('hello'))
#       "a b c"
print (type("a b c"))
#       3 + 3
print (type( 3+3))
#       "3" + "3"
print (type("3"+"3"))
#       2 ** 100
print (type(2**100))
#       2.0 ** 100
print (type(2.0**100))
#       math.sin(8)
print (type(math.sin(8)))
#       math.sin
print (type(math.sin))
#       print
print (type(print))
#       math
print (type(math))
#       'math'
print (type('math'))
#
# After you have written and run the code to learn the TYPE
# of each of the above, change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
print (type(round(2.75)))
#   As you can see from the first _TODO_, there is an important difference
#   between a  float  type and an  integer  type. Floats can have decimals 
#   while integer are just that, integers.
#
#   We can actually round a float to get the rounded integer by using the 
#   round   function like so
#       round(2.75)
#
#   Try it below this _TODO_.
#
#   Now, just as you did above, get the type of the result of the round
#   function. Notice how the result is an integer instead of a float like the
#   input that you put into the function.
#
#   Once you have done this, change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# done: 3. (1 pt)
print (26.78)
print (type(26.78))
name1 = (int(26.78))
print (type(name1))
#   We can also manually convert an object from one type to another. This is 
#   also called casting.
#
#   You can cast a float to an integer by specifying the type you are casting
#   to followed by the object that you are trying to convert in parentheses,
#   like so:
#       int(2.75)
#
#   Immediately below this _TODO_, write code that prints each of the following
#     - The value  26.78  stored to a name of your choosing
#     - The type of that value
#     - The result of casting that float into an int
#     - The type of the result
#
#   Notice how this also rounds the number.
#   
#   Once you have done this, change the above _TODO_ to DONE.
###############################################################################