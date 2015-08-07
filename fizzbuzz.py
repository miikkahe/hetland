""" for x in range(1,101):
        s = ""
        if x % 3 == 0:
            s += "Fizz"
        if x % 5 == 0:
           s += "Buzz"
        if s == "":
            s = x
        print s


# toinen

for i in range(0,101):
    if i % 3 == 0 and not i % 5 == 0:
        print "fizz: %d" % i
    elif i % 5 == 0 and not i % 3 == 0:
        print "buzz: %d" % i
    elif i % 3 == 0 and i % 5 == 0:
        print "FIZZBUZZ: %d" % i
    else:
        print i
"""

# kolmas

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i
