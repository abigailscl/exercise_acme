# Exercise ACME
###### The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
## Overview
###### This solution matches two employees who have shared the same office at the same time, for this the data stored in txt file was classified and stored in an Employee object, which contains the name of the employee, a list with the corresponding offices and a list with recorded hours. Then, with loops and conditionals, each employee's office and time are compared to find matches.
## Architecture
###### The exercise consists of a program written in python and a txt file, therefore, there is a data flow between the file and the program, the program is responsible for opening, reading the file, extracting the data it contains, organizing these data and process it.
![Architecture](/architecture.png) 
## Approach and methodology
###### The approach to solve this exercise was to classify the data that is inside the txt file and, once organized, apply algorithms to compare the data that must coincide, which is the office and the hours of all the employees registered in the file.
###### For this exercise, a formal software development methodology was not used, however the first step was to understand the objective of the problem, identify what the input is and how it was organized in the txt file and how the output should be structured. 
###### Then a diagram was made as a table to represent how the information in the file is organized and how to classify and store it, for this a notebook was used where the data classification algorithm was designed through graphics and how to compare them.
###### Finally, each function was programmed based on the graphs of the algorithm made previously and unit tests were carried out to check the efficiency of these algorithms. 
## How to run the program locally
This solution is written in python version 3.9.5, if you already have python installed in this version you can continue from step 2:
###### 1. Install python 3.9.5 : https://www.python.org/downloads/
###### 2. Clone this repository
###### 3. Open the repository in the ide of your choice
###### 4. Open a terminal at the address where the main.py file is located
###### 5. Run the following command
###### 5. Run the following command
<!--sec data-title="Prompt: Windows" data-id="windows_prompt2" data-collapse=true ces-->


    > python main.py
    

<!--endsec-->
