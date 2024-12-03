def read_input(file_path):
	"""
	"""
	all_reports = {}

	with open(file_path, mode='rt', encoding='utf-8') as f:
		line_id = 1
		for line in f:
			line_items = [int(i) for i in line.strip("\n").split()]
			all_reports[line_id] = line_items
			line_id += 1

	return all_reports


def report_is_safe(report):
	"""
	"""
	report_diffs = [report[i-1] - report[i] for i, _ in enumerate(report) if i > 0]

	return (
		all( 1 <= diff <=  3 for diff in report_diffs) or
		all(-3 <= diff <= -1 for diff in report_diffs)
	)


def part1(all_reports):
	"""
	"""
	counter_safe_reports = 0 
	for line_id, report in all_reports.items():
		if report_is_safe(report):
			counter_safe_reports += 1

	print("Answer part 1:")
	print(f"Number of safe reports is : {counter_safe_reports}")

	return None


def part2(all_reports):
	"""
	"""
	counter_safe_reports = 0 
	for line_id, report in all_reports.items():
		# remove 1 element from report and check
		# no need to check full report, because removing first element keeps safe report safe
		for counter, _ in enumerate(report):
			report_with_removed_element = report[:counter] + report[counter+1:]
			if report_is_safe(report_with_removed_element):
				counter_safe_reports += 1
				break

	print("Answer part 2:")
	print(f"Number of safe reports is : {counter_safe_reports}")

	return None


if __name__ == "__main__":

	all_reports = read_input("day_02/day_02_input.txt")

	part1(all_reports)
	part2(all_reports)
