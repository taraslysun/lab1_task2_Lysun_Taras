'''Main file of the project'''
import argparse
import folium
import haversine
from functions import read_dataset, get_films_years, get_locations, get_coordinates, pick_10_closest

parser = argparse.ArgumentParser(description='Enter info about your location and year')
parser.add_argument('year',
                    help="Year of the film's release")
parser.add_argument('latitude',
                    type=str,
                    help='Latitude of your location')
parser.add_argument('longitude',
                    type=str,
                    help='Longitude of your location')
parser.add_argument('path_to_dataset',
                    type=str,
                    help='Path to dataset of films')
args = parser.parse_args()
year = args.year
latitude = args.latitude
longitude = args.longitude
path_to_dataset = args.path_to_dataset


def main():
    '''Main function'''
    data = read_dataset(path_to_dataset)
    film_dict = get_films_years(data)
    coords = pick_10_closest(get_coordinates(data, film_dict, year), latitude, longitude)
    map = folium.Map(location=[latitude, longitude])
    for coord in coords:
        map.add_child(folium.Marker(location=[coord[0], coord[1]], popup=coord[2]))
    map.save('map.html')

if __name__ == '__main__':
    main()
