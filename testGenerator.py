#!/usr/bin/python                                                                       
# -*- coding: utf-8 -*- 

__author__ = "Giulia Dnt"

"""
This script generates an xml template to fill with your test cases

The xml structure will be: 

<TestCases>
	<Test description="" id="1">
		<step>[noInput]</step>
		<step>[noInput]</step>
		<step> utterance </step>
	</Test>
</TestCases>

the phrases are extracted from a 2 columns table

software:
Python 2.7.13 :: Anaconda 4.3.1 (x86_64)

TODO:

categories xls file should be added as path (argument parser) not hardcoded

"""
import xml.etree.cElementTree as ET
import xml.dom.minidom
import pandas as pd 


def main():
	TestCases = ET.Element("TestCases")
	
	categories = create_categories_dict()
	phrases = split_values_list(categories)
	
	fill_xml(TestCases, categories, phrases)
	write_xml(TestCases)


def fill_xml(xml_head, categories_dict, phrases_dict_generator):
	#TestCases = ET.Element("TestCases")
	count = 1

	while count < len(categories_dict):
		for categories, utterance in utterances_dict_generator:
			Test = ET.SubElement(xml_head, "Test", id=str(count), description=intent)
			step1 = ET.SubElement(Test, "step").text="[noInput]"
			step2 = ET.SubElement(Test, "step").text="[noInput]"
			step3 = ET.SubElement(Test, "step").text= utterance
			count +=1
	

def write_xml(xml_head):
	name = raw_input("How do you want to name this file? ")
	xml_p = xml.dom.minidom.parseString(ET.tostring(xml_head)).toprettyxml(indent="	")
	
	with open(name + ".xml", "w") as f:
	    f.write(xml_p.encode('utf8'))


def split_values_list(mydict):	
	"""
	param mydict: key is the category, value is a list of phrases
				  {category1 : [phrase1, phrase2, ...], category2 : [phrase1, phrase2, ...]}
	return values: generator (iterable), each value-list is split so
				   dict is {category1: phrase1, category1: phrase2 ...}
	"""
	values = ((key, val.strip().lower()) 
				for key in mydict.keys() 
				for val in mydict[key].split(','))

	return values


def create_categories_dict():
	df1 = pd.read_excel('TABLE.xlsx').dropna() 
	dict1 = pd.Series(df1.Phrases.values, index=df1.Category).to_dict()
	
	return dict1


if __name__ == "__main__":
 	main()
