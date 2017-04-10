"""Restaurant rating lister."""

# put your code here
import sys

def sort_ratings(ratings_file):
    """Takes ratings from a file and prints an alphabetically sorted statement"""
    ratings_file = open(ratings_file)
    ratings = {}
    for line in ratings_file:
        line = line.rstrip()
        line = line.split(":")
        ratings[line[0]] = line[1]

    ratings_list = sorted(ratings.items())

    for rating in ratings_list:
        print "%s is rated at %s." % (rating[0], rating[1])

    ratings_file.close()

# inputs second file argument in command line into
# function of first file argument
sort_ratings(sys.argv[1])
