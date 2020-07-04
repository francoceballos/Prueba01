irises = []

with open("casv_clubs.csv", "r") as iris_file:
	headers = next(iris_file).strip().split(",")

	for row in iris_file:
		iris = row.strip().split(",")
		iris_dict = dict(zip(headers, iris))

		irises.append(iris_dict)


print(irises)