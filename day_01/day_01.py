location_ids_1 = []
location_ids_2 = []

# read all location id into 2 lists
with open('day_01/day_01_input.txt', mode='rt', encoding='utf-8') as f:
	for line in f:
		line_items = line.strip("\n").split()
		location_ids_1.append(int(line_items[0]))
		location_ids_2.append(int(line_items[1]))

# sort lists in place containing location ids
location_ids_1.sort()
location_ids_2.sort()

# get the list of distances
distances = [abs(a - b) for a, b in zip(location_ids_1, location_ids_2)]

# print(distances)
print("Answer to part 1")
print(f"Total of distances is : {sum(distances)}")

# get similarity scores by
# multiplying each location id from list 1 by number of occuence in the list 2
similarity_scores = [a * location_ids_2.count(a) for a in location_ids_1]

# print(similarity_scores)
print("Answer to part 2")
print(f"Total of similarity scores is : {sum(similarity_scores)}")

