import csv
from create_xml import createFile

def formatManDataToColumns(man, columnTitles):
	return {columnTitles[index] : value for index, value in enumerate(man)}


def formatPeopleDataToColumns(people, columnTitles):
	return [formatManDataToColumns(man, columnTitles) for man in people]


def getPeople(listFromCSV):
	people = []
	for index, man in enumerate(listFromCSV):
		if index > 3:
			people.append(man)
	return people


def getColumnNames():
	return (
		"A", 
		"B", 
		"C", 
		"D", 
		"E", 
		"F", 
		"G", 
		"H", 
		"I", 
		"J", 
		"K", 
		"L", 
		"M", 
		"N", 
		"O", 
		"P", 
		"Q", 
		"R"
		)


def getPeopleDataInCorrectFormat(source):
	return formatPeopleDataToColumns(
		getPeople(source), 
		getColumnNames()
	)


def getData():
	with open("data.csv", newline="") as data:
		fileContent = csv.reader(data)
		return getPeopleDataInCorrectFormat(fileContent)


def main():
	data = getData()
	createFile(data)


main()




		
