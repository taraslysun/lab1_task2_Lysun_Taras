'''Module for functions for task 2 of lab 1'''
import geopy.geocoders
import haversine
def read_dataset(path_to_dataset:str) -> list[str]:
    '''Read dataset from file and return it as a list of lines'''
    data = []
    with open(path_to_dataset, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data[15:]

def get_films_years(data:list) -> dict[str]:
    '''Create a dictionary with years as keys and lists of films as values'''
    film_dict = {}
    year_list = sorted({line[line.find('(')+1: line.find(')')]
                        for line in data if line[line.find('(')+1: line.find(')')].isdigit()})
    for year in year_list:
        film_dict[year] = list({line[2:line.find('" (')]
                                for line in data if year in line})

    return film_dict


def get_locations(data:list, film_dict:dict, year:str) -> dict[str]:
    '''Create a dictionary with films as keys and locations as values'''
    location_dict = {}
    for film in film_dict[year]:
        if not film:
            continue
        location_dict[film] = [line[line.rfind('\t')+1:]
                            for line in data if film in line]
    return location_dict

def get_coordinates(data:list, film_dict:dict, year:str) -> tuple[int, int, str]:
    '''
    Create a dictionary with films as keys and coordinates as values
    >>> get_coordinates(get_films(read_dataset('locations.list')), '2006')['"10th & Wolf"']
    (39.9526, -75.1652)
    '''
    geolocator = geopy.geocoders.Nominatim(user_agent="app")
    coords = []
    films = film_dict[year]
    for film in films:
        if not film:
            continue
        try:
            for loc in get_locations(data, film_dict, year)[film]:
                location = geolocator.geocode(loc)
                coords.append((location.latitude,location.longitude,film))
        except (AttributeError, geopy.exc.GeocoderUnavailable):
            continue
    return coords


def pick_10_closest(coords:list, latitude:str, longitude:str) -> list[tuple[int, int, str]]:
    '''
    Pick 10 closest locations to the user's location, if less than 10, return all of them
    '''
    user = (float(latitude), float(longitude))
    if len(coords) < 11:
        return coords
    closest = sorted(coords, key=lambda x: haversine.haversine(user, (x[0], x[1])))[:11]
    return closest
