#!/usr/bin/env python

__author__ = "Giulia Dnt"

"""
This script generates an empty xml template to fill with your test cases
structure will be: 

<TestCases>
	<Test description="" id="1">
		<step>[noInput]</step>
		<step>[noInput]</step>
		<step> </step>
	</Test>
</TestCases>

with default 3 steps per each test (first two are no inputs)

Python 2.7.13 :: Anaconda 4.3.1 (x86_64)

"""
import xml.etree.cElementTree as ET
import xml.dom.minidom

#TestCases = ET.Element("TestCases")

def main():
	TestCases = ET.Element("TestCases")

	while True:
		try:
			num = raw_input("How many tests do you want for this file? ")
			for i in range(1, int(num)+1):
				Test = ET.SubElement(TestCases, "Test", id=str(i), description="")
				step1 = ET.SubElement(Test, "step").text="[noInput]"
				step2 = ET.SubElement(Test, "step").text="[noInput]"
				step3 = ET.SubElement(Test, "step").text=" "
			break

		except Exception as e:
			pass
			print "Please input the number of tests you want in digits" 	

	name = raw_input("How do you want to name this file? ")
	xml_p = xml.dom.minidom.parseString(ET.tostring(TestCases)).toprettyxml(indent="	")
	with open(name + ".xml", "w") as f:
	    f.write(xml_p)

if __name__ == "__main__":
	main()