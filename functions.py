'''Module for functions for task 2 of lab 1'''
def read_dataset(path_to_dataset):
    '''Read dataset from file and return it as a list of lines'''
    data = []
    with open(path_to_dataset, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('"#'):
                data.append(line)
    return data


def get_films(data):
    '''Create a dictionary with years as keys and lists of films as values'''
    film_dict = {}
    for line in data:
        year = line[line.find('(')+1: line.find(')')]
        film_dict[year] = list({line[2: line.find('" (')]
                               for line in data if line[line.find('(')+1: line.find(')')] in line})
    return film_dict
