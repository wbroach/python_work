def make_album(artist_name, album_title, tracks = ''): 
    """Makes an album that tracks in dictionary"""
    catalog = {'artist': artist_name, 'album name': album_title}
    if tracks:
        catalog['# of tracks'] = tracks
    return catalog
    
while True:
    print("Enter album information as follows (press 'q' to quit at any time)")
    
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
            
    album = input("Album name: ")
    if album.lower() == 'q':
        break    

    if_tracks_known = input("Do you know the number of tracks (y or n)? ")
    if if_tracks_known.lower() == 'y': 
        track_number = input("# of tracks: ")
        if track_number.lower() == 'q':
            break   

    elif if_tracks_known.lower() == 'n':
        track_number = ''
        
    elif if_tracks_known.lower() == 'q':
        break
    
    album_info = make_album(artist, album, track_number)
    print(album_info)
