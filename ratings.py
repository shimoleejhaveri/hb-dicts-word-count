"""Restaurant rating lister."""


# put your code here

new_file = open("scores.txt")

def restaurant_list(new_file):

    list_of_restaurants = {}

    for line in new_file:
        line = line.rstrip()
        restaurant_line = line.split(':')
        # print(restaurant_line)

        restaurant = restaurant_line[0]
        rating = restaurant_line[1]

        list_of_restaurants[restaurant] = rating

    for restaurant, rating in sorted(list_of_restaurants.items()):
        print(f"{restaurant} is rated at {rating}")
               


restaurant_list(new_file)