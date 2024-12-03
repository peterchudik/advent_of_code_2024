location_ids_1 = []
location_ids_2 = []
# len = 0

# read all location id into 2 lists and remember length
with open('day_01/day_01_input_test.txt', mode='rt', encoding='utf-8') as f:
	for line in f:
		line_items = line.strip("\n").split()
		location_ids_1.append(int(line_items[0]))
		location_ids_2.append(int(line_items[1]))
		# len += 1

# sort lists in place containing location ids
location_ids_1.sort()
location_ids_2.sort()

# get the list of distances
# for i in range(len):
# 	distance = abs(location_ids_1[i] - location_ids_2[i])
# 	distances.append(distance)
distances = [abs(a - b) for a, b in zip(location_ids_1, location_ids_2)]

# print(distances)
print("Answer to part 1")
print(f"Total of distances is : {sum(distances)}")

# get occurenc count of each element in list 2
# from collections import Counter

# counter_location_ids_2 = Counter(location_ids_2)
# print(counter_location_ids_2)

# get similarity scores list by
# multiplying each location id from list 1 by number of occuence in the list 2

# similarity_scores = []

# for location_id in location_ids_1:
#     similarity_score = location_id * counter_location_ids_2.get(location_id, 0)
#     similarity_scores.append(similarity_score)
similarity_scores = [a * location_ids_2.count(a) for a in location_ids_1]

# print(similarity_scores)
print("Answer to part 2")
print(f"Total of similarity scores is : {sum(similarity_scores)}")

