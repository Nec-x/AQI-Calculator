*Introduction*

Hello and welcome to the Air Quality Index Calculator(AQIC)! This calculator is able to solve the problem of 
"Where are some places where the air quality is unhealthy within 30 miles of where I am now?".
Using the data collected from PurpleAir sensors around the globe, we can identify the different level of air quality 
in specific areas.

This project uses the PurpleAir API (https://api.purpleair.com/) and the Nominatim API (https://nominatim.org/release-docs/latest/api/Overview/)

The GUI generated is built using TKinter, a Python library.


*How To Use*

Location:
	Location is a interactive box that allows input. Here, you will specify the location that you wish to be
	the center point of where you want your AQI search to be conducted. The more specific the better. 
	Addresses work such as "34452 Laurie Lane", and less specific ones such as "Florida".

Minimum AQI:
	Minimum AQI is a interactive box that allows input. The number entered here will be the mimimum
	AQI level that will be shown at the end of the completed search. Entering in "40" will, for example,
	lead to showing areas who AQI levels are 40 and above. It will not show those that are below 40.

Range(In Miles):
	Range(In Miles) is a interactive box that allows input. The number entered will be how far from your previously entered center point
	that the search will be conducted. If for example "30" is entered, then the search will be conducted as far as 30 miles
	from the center point. It will not look at PurpleAir sensors outside of that mile range.
Max Outputs:
	Max Outputs is a interactive box that allows input. The number entered will be the amount of outputs that will be shown to you
	on the right side of the "Options" menu. A input of "5" will show 5 locations and their API. If not enough sensors are found with
	the desired information, as much as was found will be displayed.
Clear:
	Clear is a button that can be pressed at the bottom of the "Options" menu. It will clear all the entries made in the "Options" menu.

Instructions:
	Instructions is a button that can be pressed at the bottom of the "Options" menu. It will display a pop up containing this information.

*Upon Pressing Start*
	
	Pressing Start(A button located at the bottom of the "Options" menu) will display a new pop up window displaying a input box
	to the user. Alongside this, the "Options" menu will not be editable until the current search is completed.

	Leaving the newly displayed input box blank will do a "call" to the PurpleAir API, and will gather the data to be used in the search through their server.
	Pressing enter will commence the search.
	
	If instead the user does not wish to use the PurpleAir API, they can input a file path to a file containing the data from a previous call
	to the PurpleAir API. This file must contain the same data, structured in the same way as a call to the PurpleAir API would return.
	If it is not, an error message will appear to inform you.
	After inputting the file name, entering will commence the search.

*Reading Results*
	After the search, a varying amount of information may be displayed.
	If no areas match the criteria you are searching for, "No areas matched your criteria, please try again" will be displayed.
	If some areas match the criteria, you will be shown (up to your maximum output) all the areas in descending order from the highest AQI level.

	An example of a result looks as follows:

	AQI Value: 88
	Lat/Lon: (34.08064,-118.63482)
	Location: Sadie Road, Los Angeles County, California, 90290, United States
	
	This data means:
	AQI Value: This is the AQI Value of this area.
	Lat/Lon: This is the coordinates of the location of the sensor
	Location: This is the location name as taken from the Nominatim API when the coordinates above are entered.