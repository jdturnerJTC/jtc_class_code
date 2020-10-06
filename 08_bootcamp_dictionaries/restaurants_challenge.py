print("Challenge: Favourite Restaurants")

print()

print("Question 1")

print("Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. Go through the dictionary and print out the following 3 pieces of information about the restaurant: \n1. The latitude and longitude of Four Barrel Coffee \n2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. \n3. The website of Four Barrel Coffee.")

restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print(restaurant['latitude'], "&", restaurant['longitude']) 

# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(restaurant['address1'], restaurant['city'], restaurant['state'], restaurant['zip_code'])

# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(restaurant['url'])

# print()

# print("Question 2")

# # TODO: Create a new empty dictionary called fav_restaurants.
fav_restaurants = {'Balthazar': ['80 Spring St, New York, NY 10012', 'Sausage & Meatballs', '10a-10p'], 
'Sylvia\'s': ['328 Malcolm X Blvd, New York, NY 10027', 'Chicken & Grits', '12-8p'], 
'Famous Sammy\'s': ['157 Chrystie St, New York, NY 10002', 'Subs', '10a-8p']}
# # TODO: Choose 3 of your most favourite restaurants in NYC and add the following information for those restaurants inside fav_restaurants:
# #         1. Name of the restaurant - Should be the key of the dictionary
# #         2. Address of the restaurant - 1st value of the list
# #         3. Favourite dish in that restaurant - 2nd value of the list
# #         4. Opening and closing hours of that restaurant - 3rd value of the list
# # TODO: Print the dictionary.
print(fav_restaurants)
# # The dictionary should look like this

# '''
# fav_restaurants =
# {
#     "Subway": ["116th & Broadway, NY 10016", "Pizza Sub", "12 PM - 12 AM"]
#     "Dominoes": []
#     and so on....
# }
# '''

# print()

print("Question 3")
print("Imagine that any 1 of your most favourite restaurants closed down during the Covid. Remove the details of that restaurant from the dictionary fav_restaurants.")

# # TODO: Remove 1 restaurant from the dictionary fav_restaurants.
fav_restaurants.pop('Balthazar')
# # TODO: Print the new dictionary. The new dictionary should contain only 2 restaurants.
print(fav_restaurants)

print("Question 4")
print("Imagine that another one of your most favourite restaurants modified its opening and closing hours during Covid. Update just the hours field (3rd value of the list) for 1 restaurant in the dictionary fav_restaurants.")

# # TODO: Update the hours field of 1 restaurant in the dictionary fav_restaurants.
old_hours = fav_restaurants['Sylvia\'s'][2] 
fav_restaurants['Sylvia\'s'][2] = '3-11p'
new_hours = fav_restaurants['Sylvia\'s'][2] 
print(old_hours, new_hours)

# # TODO: Print the old and new open hours of the restaurant by accessing those fields from the dictionary.
print(f"Sylvia's old hours were {old_hours} and the new hours are {new_hours}")

# # TODO: Print the updated dictionary.
print(fav_restaurants) 


