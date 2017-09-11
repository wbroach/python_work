#~ def city_country(city, country):
    #~ formal_name = city + ", " + country
    #~ return formal_name.title()
    
#~ listing = city_country('santiago', 'chile')
#~ print(listing)
#~ listing = city_country('atlanta', 'georgia')
#~ print(listing)
#~ listing = city_country('mexico city', 'mexico')
#~ print(listing)

#~ def make_album(artist_name, album_title, tracks = ''):
    #~ catalog = {'artist': artist_name, 'album name': album_title}
    #~ if tracks:
        #~ catalog['# of tracks'] = tracks
    #~ return catalog
    
#~ album_listing = make_album('prince','purple rain')
#~ print(album_listing)
#~ album_listing = make_album('GNR','chinese democracy')
#~ print(album_listing)
#~ album_listing = make_album('nin','the fragile', tracks = 9)
#~ print(album_listing)

def make_album(artist_name, album_title, tracks = ''):
    catalog = {'artist': artist_name, 'album name': album_title}
    if tracks:
        catalog['# of tracks'] = tracks
    return catalog
    
while True: 
    print("\nPlease provide album detail as necessary (press 'q' at any time to quit)")
    
    group = input("Artist name: ")
    if group.lower() == 'q':
        break
    
    lp_name = input("Album name: ")
    if lp_name.lower() == 'q':
        break
        
    tracks_numba = input("Number of tracks: ")
    if tracks_numba.lower() == 'q':
        break
        
    dict_of_results = make_album(group.lower(), lp_name.lower(), tracks_numba.lower())
    print(dict_of_results)
        
    
    
    
    
    
    
    
    
        
    













