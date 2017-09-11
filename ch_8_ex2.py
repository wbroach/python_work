def show_magicians(things):
    for thing in things:
        print(thing.title())

def make_great(things):
    for i in range(len(things)):
        things[i] += " the Great!"
    return things
    
magicians = ['tom', 'dick', 'harry', 'steve']

new_list = make_great(magicians[:])
show_magicians(new_list)
show_magicians(magicians)


