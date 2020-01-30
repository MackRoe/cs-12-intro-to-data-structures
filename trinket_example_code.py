# reference only
# TA plz do not evaluate

list_of_lists_histogram = [["bird", 3], ["cat", 5], ["dog", 5]]

# TODO: write a loop that prints out the animal word and the count in
# list_of_lists_histogram
# update the count for "cat" by adding 1

for list in list_of_lists_histogram:
    print(list)
    critter = list[0]
    count = list[1]
    print(f"The critter is {critter} and its count is {count}")  # √

list_of_lists_histogram[1][1] += 1  # √

dictionary_histogram = {"cupcake": 33, "donut": 4, "cake": 50}

# TODO: write a loop that prints out the food word and the count in
# dictionary_histogram
# update the count for "cupcake" by adding 1

for key, value in dictionary_histogram.items():
    print(f"Food item is {key} and count is {value}")

dictionary_histogram["cupcake"] += 1
print(dictionary_histogram)

list_of_tuples_histogram = [("snowboarding", 4), ("basketball", 8), ("football", 9)]
# update the count for "football" by adding 1

for inner_tuple in list_of_tuples_histogram:
    sport = inner_tuple[0]
    count = inner_tuple[1]
    print(f"Sport: {sport}, Count: {count}")

list_of_tuples_histogram[2] = (list_of_tuples_histogram[2][0], list_of_tuples_histogram[2][1] + 1)
print(list_of_tuples_histogram[2])
