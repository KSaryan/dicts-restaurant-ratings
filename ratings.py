def print_ratings(ratings_dict):
    """Prints a sorted lists restaurants and their scores"""

    for restaurant, rating in sorted(ratings_dict.items()):
        print "{} is rated at {}".format(restaurant, rating)

    print '\n'


def add_ratings(input_dict):
    """Adds/updates restaurants and ratings"""

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

    input_dict[new_restaurant] = new_rating
    print '\n'
    
    return input_dict


def view_ratings(score_file):
    """Adding new items to dictionary of restaurants and ratings"""

    result = {}

    scores = open(score_file)

    for line in scores:
        restaurant, rating = line.rstrip().split(':')
        result[restaurant] = rating

    while True:
        print ("Enter 1 to print restaurant list\nEnter 2 to add a new "
               "restaurant or update its rating\nEnter 3 to quit")
        user_choice = raw_input("Enter choice: ")

        if user_choice == '1':
            print "\n"
            print_ratings(result)
        elif user_choice == '2':
            add_ratings(result)
        elif user_choice == '3':
            print "Thank you for visiting!"
            break
        else:
            print "Not a valid input. Choose 1, 2, or 3."

    scores.close()

view_ratings('scores.txt')
