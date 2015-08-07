summa = input("Give a number (will stop when we hit over 100): ")

while summa < 100:
    more = input("Give more: ")
    summa = summa + more

print "Done", "(The sum is", summa, ")"