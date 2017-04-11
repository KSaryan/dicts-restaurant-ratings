def print_ratings(ratings_dict):
    """Prints a sorted lists restaurants and their scores"""

    for restaurant, rating in sorted(ratings_dict.items()):
        print "{} is rated at {}".format(restaurant, rating)

    print '\n'


def add_ratings(score_file):
    """Adding new items to dictionary of restaurants and ratings"""

    result = {}

    scores = open(score_file)

    for line in scores:
        restaurant, rating = line.rstrip().split(':')
        result[restaurant] = rating

    print_ratings(result)

    while True:
        new_restaurant = raw_input("Enter a new restaurant: ")

        while True:
            new_rating = raw_input("Enter a rating for that restaurant: ")
       
            try:
                if int(new_rating) >= 1 and int(new_rating) <= 5:
                    break
                else:
                    print ("That is not a valid rating, please enter a rating "
                          "between 1 and 5")
            except ValueError:
                print ("That is not a valid rating, please enter a number in"
                       "between 1 and 5!!!!!")

        result[new_restaurant] = new_rating

        print_ratings(result)

        add_another = raw_input("Do you want to add another? y/n: ")

        if add_another.lower() == "n" or add_another.lower() == "no":
            break

    scores.close()

add_ratings('scores.txt')
