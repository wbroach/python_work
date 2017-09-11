allData = {
 'WY': {'Albany': {'pop': 36299, 'tracts': 10},
        'Big Horn': {'pop': 11668, 'tracts': 3},
        'Campbell': {'pop': 46133, 'tracts': 7},
        'Carbon': {'pop': 15885, 'tracts': 5},
        'Converse': {'pop': 13833, 'tracts': 4},
        'Crook': {'pop': 7083, 'tracts': 2},
        'Fremont': {'pop': 40123, 'tracts': 10},
        'Goshen': {'pop': 13249, 'tracts': 4},
        'Hot Springs': {'pop': 4812, 'tracts': 2},
        'Johnson': {'pop': 8569, 'tracts': 2},
        'Laramie': {'pop': 91738, 'tracts': 21},
        'Lincoln': {'pop': 18106, 'tracts': 4},
        'Natrona': {'pop': 75450, 'tracts': 18},
        'Niobrara': {'pop': 2484, 'tracts': 1},
        'Park': {'pop': 28205, 'tracts': 5},
        'Platte': {'pop': 8667, 'tracts': 2},
        'Sheridan': {'pop': 29116, 'tracts': 6},
        'Sublette': {'pop': 10247, 'tracts': 2},
        'Sweetwater': {'pop': 43806, 'tracts': 12},
        'Teton': {'pop': 21294, 'tracts': 4},
        'Uinta': {'pop': 21118, 'tracts': 3},
        'Washakie': {'pop': 8533, 'tracts': 3},
        'Weston': {'pop': 7208, 'tracts': 2}}
        }
        
for state, state_dict in allData.items():
    counties = [(county['pop'], county_name) for county_name, county in state_dict.items()]
    min_pop, min_name = min(counties)
    print(min_name, min_pop)



