Generate Report
Process the client provided data which carries Customer Id, Contract Id, Geo Zone, Team Code, Project Code, Build Duration from the data set (either by csv, xml or flat file) and print the final result in the report

Given a string with the following data (it includes multiple lines): 
2343225,2345,us_east,RedTeam,ProjectApple,3445s 
1223456,2345,us_west,BlueTeam,ProjectBanana,2211s 
3244332,2346,eu_west,YellowTeam3,ProjectCarrot,4322s 
1233456,2345,us_west,BlueTeam,ProjectDate,2221s 
3244132,2346,eu_west,YellowTeam3,ProjectEgg,4122s

The data is organized into columns delimited by a comma (,) in the following order: 
customerId,contractId,geozone,teamcode,projectcode,buildduration 

The first line of data would then be interpreted as 
2343225 is the customerId 
2345 is the contractId 
us_east is the geozone 
RedTeam is the teamcode 
ProjectApple is the projectcode 
3445s is the buildduration
 
Write an application using Java that would consume the entire multiline string as the input 
and produce the following report as the output 
The number of unique customerId for each contractId 
The number of unique customerId for each geozone 
The average buildduration for each geozone 
The list of unique customerId for each geozone

Approach:
Python Program along with Pytest Automation Framework to get the desired output data/result

Software Required:
- PyCharm 2022.3.2 (Community Edition)
- PyCharm Runtime version: 17.0.5+1-b653.25 amd64
- VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
- Python: Version 3.11.2 - v.1934 64 bit
- Python Library:  pytest 8.3.3, pytest-html
	- pytest 8.3.3 installation:
		- pip install -U pytest
	- pytest-html instllation:
		- pip install pytest-html

Environment Varialble:
- E:\PyCharm\bin
- Path Variable: %PyCharm%
- Path Variable: %PyCharm Community Edition%
- Path Variable: D:\Python\Scripts\
- Path Variable: D:\Python\
- User Variable: D:\PyCharm Community Edition 2022.3.2\bin



Venv (Virtual Environment) Executable Command:

Open the Terminal window and execute below command

pytest test_process_data.py  --html=report.html --self-contained-html -vv

HTML Output Report:

file:///C:/Users/anupr/PycharmProjects/pythonProject2/report.html 


