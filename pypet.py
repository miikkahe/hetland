print "Welcome to Pypet!"
print

cat = {
    'name': 'Weiwei',
    'age': 22,
    'weight': 11.6,
    'hungry': True,
    'photo': '(=^o.o^=)__',
    'happiness': 0,
}

mouse = {
    'name': 'Kaikai',
    'age': 26,
    'weight': 20.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
    'happiness': 0,
}

pets = [cat, mouse]

print 'Hello, ' + cat['name']
print
print cat['photo']
print
print cat
print

print 'Hello, ' + mouse['name']
print
print mouse['photo']
print
print mouse
print

def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print 'The Pypet is not hungry!'

if cat['hungry'] == True or mouse['hungry'] == True:
    print "One or more pets are hungry!"

print "Choose an option:"
print "1. Feed cat    2. Feed mouse    3. Feed both"

choice = input("> ")

if choice == 1:
    feed(cat)
    print cat
elif choice == 2:
    feed(mouse)
    print mouse
else:
    for pet in pets:
        feed(pet)
        print pet