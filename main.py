'''Main file of the project.'''
import argparse

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
    '''Main function of the project.'''

if __name__ == '__main__':
    main()