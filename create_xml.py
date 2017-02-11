import xml.etree.ElementTree as ET
import copy
from payer_data import getPayerDataForFields

def getWrapperTemplate():
	tree = ET.parse("wrapper.xml")
	return tree


def getItemTemplate():
	tree = ET.parse("item.xml")
	return tree;


def getItemsRoots(items):
	return [getItemRootWithData(item) for item in items]


def getItemRootWithData(itemData):
	itemRoot = getItemTemplate().getroot()
	for column, value in itemData.items():
		fillInItemWithManData(itemRoot, column, value)
	fillInItemWithPayerData(itemRoot)
	fillInItemTitle(itemRoot, itemData.get("B"))
	return itemRoot


def fillInItemWithManData(rootToFillIn, column, value):
	elementName = getRootElementNameBasedOnColumnName(column)
	
	if elementName != None:
		rootToFillIn.find("forms").find("item").find(elementName).text = value

	return rootToFillIn;


def fillInItemWithPayerData(rootToFillIn):
	payerData = getPayerDataForFields()
	rootWithPayerData = rootToFillIn.find("forms").find("item")
	for fieldName, value in payerData.items():
		rootWithPayerData.find(fieldName).text = value
	return rootToFillIn


def fillInItemTitle(itemRoot, itemTitle):
	itemRoot.find("title").text = itemTitle
	return itemRoot
	

def getRootElementNameBasedOnColumnName(column):
	columnToElementName = {
		"B": "p10_3_subfield_2",
		"C": "p11",
		"D": "p12",
		"F": "p15",
		"G": "p16",
		"H": "p17",
		"I": "p21",
		"J": "p18",
		"K": "p19",
		"L": "p20",
		"M": "p23",
		"N": "p22",
		"P": "p13",
		"Q": "p5_subfield_0",
		"R": "p25"
	}
	return columnToElementName.get(column)


def appendItems(wrapperRoot, itemsRoots):
	for item in itemsRoots:
		wrapperRoot.find("Profiles").find("item").find("FormsList").append(item)


def createFile(items):
	wrapperTree = getWrapperTemplate()
	wrapperRoot = wrapperTree.getroot()
	itemsRoots = getItemsRoots(items)
	appendItems(wrapperRoot, itemsRoots)
	wrapperTree.write("result.xml")
	
