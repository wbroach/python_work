def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
        
def make_great(things):
    for i in range(len(things)):
        things[i] += " the Great!"
    return things
    
magicians = ['tom', 'dick', 'harry', 'steve']
magicians_plus_the_great = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_plus_the_great)

