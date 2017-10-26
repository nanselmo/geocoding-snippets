
#STEP ONE: Creat Educator Object from educator DF
educator_dict = educator_lat_long_sample.to_dict('index')
current_educator = educator_dict[list(educator_dict.keys())[0]]


#STEP TWO: Loop through CCD Edge GeoIDs
lat_long_threshold = 5
meets_threshold = 0
for index, row in edge_geoid_sample.iterrows():
    
    school_lat = row['LATCODE']
    school_long = row['LONGCODE']
    current_ed_lat = current_educator['lat']
    current_ed_long = current_educator['longi']

    #check if it's in the threshold
    if (row['LATCODE'] < (current_educator['lat'] + lat_long_threshold)) and (row['LATCODE'] > (current_educator['lat'] - lat_long_threshold)):
        meets_threshold = meets_threshold + 1
        print meets_threshold
        #calculate the minimum distance away
        the_dist = math.sqrt((school_lat - current_ed_lat)**2 + (school_long - current_ed_long)**2)
        print the_dist
        ##add that min_dist to the object
        if meets_threshold == 1:
                current_educator['min_dist'] = the_dist
                current_educator['closest_school'] = row['NCESSCH']
                current_educator['closest_city'] = row['LCITY']
        else:
            if the_dist < current_educator['min_dist']:
                current_educator['min_dist'] = the_dist
                current_educator['closest_school'] = row['NCESSCH']
                current_educator['closest_city'] = row['LCITY']

                                                                                
