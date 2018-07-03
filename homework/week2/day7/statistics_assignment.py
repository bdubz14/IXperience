# -*- coding: utf-8 -*-
"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data 
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a script
with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information
- Given a neighbourhood, the tool will provide the following information to the user
  - Total number of available listings in the neighbourhood
  - Number of rooms broken down per listing type
  - Average Room Price
  - Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belém"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.
This functionality will help the user to find an appropriate listing. It will ask
the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesnt specifiy any of the requirements (pressing enter without typing anything)
We will consider that the user is indiferent

It will also ask the user if he/she prefers the results sorted by price, by average score
or by number of reviews.

Finally the script will print out the top 10 results matching the desired requirements and sorted
by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user that no
listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the data source.
"""

import pandas as pd
import sys

def load_data():
    data = pd.read_csv('data/airbnb.csv', encoding='Latin-1')
    return data

def information(neighborhood):
    data = load_data()
    neigh_data = data[data.neighborhood == neighborhood]
    room_type_count = neigh_data['room_type'].value_counts()
    neigh_info = neigh_data['price'].describe()
    return('Information for {}:\nTotal number of available listings: {}\nBy type\nEntire home/apt: {}\nPrivate room: {}\nShared room: {}\nAverage room price: {}\nPrice Quartiles\n25%: {}\n50%: {}\n75%: {}'.format(
        neighborhood, neigh_info['count'], room_type_count[0], room_type_count[1], room_type_count[2], round(neigh_info['mean'], 2), neigh_info['25%'], neigh_info['50%'], neigh_info['75%']))

def search():
    data = load_data()
    price_input = input('Enter price range (ex:40,50) To skip, just press Enter: ')
    if not price_input == '':
        price_range = price_input.split(',')
        price_range[0] = int(price_range[0])
        price_range[1] = int(price_range[1])
        data = data[(data.price >= price_range[0]) & (data.price <= price_range[1])]
    room_input = input('Enter room # range (ex:1,3) To skip, just press Enter: ')
    if not room_input == '':
        room_range = room_input.split(',')
        room_range[0] = int(room_range[0])
        room_range[1] = int(room_range[1])
        data = data[(data.bedrooms >= room_range[0]) & (data.bedrooms <= room_range[1])]
    region_input = input('Enter regions you would like to search (ex:Alvalade,Santa Maria Maior,Estrela) To skip, just press Enter: ')
    if not region_input == '':
        region_list = region_input.split(',')
        data = data.set_index('neighborhood', drop=False).loc[region_list]
    order = input('How would you like the results to be sorted by? Price, Rating, or # of reviews(Reviews): ')
    if order == 'Price':
        data = data.sort_values('price', ascending=True)
    elif order == 'Rating':
        data = data.sort_values('overall_satisfaction', ascending=False)
    elif order == 'Reviews':
        data = data.sort_values('reviews', ascending=False)
    print(data.head(10).to_string())
    

def parse_arguments():
    arguments = sys.argv[1:]
    region = ''
    if arguments[0] == 'information':
        for name in arguments[1:-1]:
            region += name + ' '
        region += arguments[-1]
        arguments[1] = region
    return arguments

def main(arguments):
    if arguments[0] == 'information':
        print(information(arguments[1]))
    elif arguments[0] == 'search':
        search()

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
