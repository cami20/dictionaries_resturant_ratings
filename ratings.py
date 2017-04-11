"""Restaurant rating lister."""

# put your code here
import sys

def sort_ratings(ratings_file):
    """ Takes ratings from a file and prints alphabetically sorted statements """
    ratings_file = open(ratings_file)

    ratings = {}
    for line in ratings_file:
        line = line.rstrip()
        line = line.split(":")
        ratings[line[0]] = line[1]

    ratings_file.close()
    return ratings


def ratings_options(ratings_dict):
    while True:
        user_choice = str(raw_input("Type 'a' to view ratings in alphabetical order \n \
            Type 'b' to add a new resturant \n Type 'q' to quit: \n \n")).lower()

        if user_choice == "a":
            ratings_list = sorted(ratings_dict.items())

            for rating in ratings_list:
                print "%s is rated at %s." % (rating[0], rating[1])
            continue
        elif user_choice == "b":
            new_rest = str(raw_input("Type the name of a restaurant you would \
                like to add a rating for: ")).title()
            new_rating = str(raw_input("Great! On a scale of 1 to 5, how would \
                you rate this restaurant: "))

            if new_rating in ["1", "2", "3", "4", "5"]:
                ratings_dict[new_rest] = new_rating
            else:
                print "Ratings must be a whole number between 1 and 5! Your input was not added!"
        elif user_choice == "q":
            break
        else:
            print "Invalid input!"
            continue


# inputs second file argument in command line into
# function of first file argument
ratings = sort_ratings("scores.txt")
ratings_options(ratings)
