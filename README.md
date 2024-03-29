<h1 align="center">
    <br>
    Austin Animal Shelter Dashboard :dog:	
</h1>

<div align="center">
 
[![License badge](https://img.shields.io/badge/License-MIT-red.svg?style=for-the-badge&logo=github)](LICENSE "GitHub MIT License") [![Generic badge](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/) [![Generic badge](https://img.shields.io/badge/Language-JavaScript-blue.svg)](https://www.javascript.com/) [![Generic badge](https://img.shields.io/badge/Database-MongoDB-yellow.svg)](https://www.mongodb.com/) [![Generic badge](https://img.shields.io/badge/Development_Tool-Jupyter_Notebook-orange.svg)](https://jupyter.org/) [![Generic badge](https://img.shields.io/badge/OS-Linux-pink.svg)](https://www.linux.org/) [![Generic badge](https://img.shields.io/badge/Tools-PyMongo-purple.svg)](https://pymongo.readthedocs.io/en/stable/) [![Generic badge](https://img.shields.io/badge/Tools-Mongo_Shell-purple.svg)](https://www.mongodb.com/docs/v4.4/mongo/) [![Generic badge](https://img.shields.io/badge/Framework-Dash-green.svg)](https://plotly.com/dash/) [![Generic badge](https://img.shields.io/badge/Graphing_Library-Plotly-sage.svg)](https://plotly.com/)

 </div>

## Competency
> Learn how to apply database systems concepts and principles to develop client/server applications that interface client-side code with databases. Develop an application that integrates with current and emerging technologies in an effective and efficient manner. 

## Scenario :memo:
You work for Global Rain, a software engineering company that specializes in custom software design and development. Your team has been assigned to work on a project for an innovative international rescue-animal training company, Grazioso Salvare. You have been made the lead developer on this project.

As part of its work, Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs are able to find and help to rescue humans or other animals, often in life-threatening conditions. To help identify dogs for training, Grazioso Salvare has reached an agreement with a non-profit agency that operates five animal shelters in the region around Austin, Texas. This non-profit agency will provide Grazioso Salvare with data from their shelters.

In meeting with the client, Grazioso Salvare, you have discovered that they look for certain profiles in dogs to train. For instance, search-and-rescue training is generally more effective for dogs that are no more than two years old. Additionally, certain breeds of dogs are proficient at different types of rescue, such as water rescue, mountain or wilderness rescue, locating humans after a disaster, or finding a specific human by tracking their scent.

Grazioso Salvare is seeking a software application that can work with existing data from the animal shelters to identify and categorize available dogs. Global Rain has contracted for a full stack development of this application that will include a database and a client-facing web application dashboard, through which users at Grazioso Salvare will access the database.

Grazioso Salvare has also requested that the code for this project be open source and accessible on GitHub, so that it may be used and adapted by similar organizations.

## Motivation 
The motivation behind the creation and maintenance of the project is to search for good candidates of dog trainers to train to become search-and-rescue companions. With MongoDB, the database from the animal shelters can be quickly and easily setup. Using the CRUD functionality for the animal database, the client, Grazioso Salvare can manage their navigation and records of data.  

## Steps 
To obtain a local copy and get the program up and running, please follow the following example steps: 
1. Create a simple Mongo Database named “AAC”. 
2. Create administrator account with full privileges to the “AAC” database. 
3. Enable user authentication for the database using: 
mongo --port xxxxx  --authenticationDatabase "admin" -u "admin" -p 
4. Import data from the file “aac_shelter_outcomes.csv”. 
5. Develop Python module in a PY file for CRUD operations in Jupyter Notebook. 
6. Create a method for create. 
7. Create a method for read.  
8. Create a method for update.  
9. Create a method for delete.  
10. Create and run Python testing script in Jupyter Notebook. 
  * Make any necessary changes to ensure the code is functional.  
11. Create Dashboard web application. 
  * Include chart of choice, geolocation map, widgets, and interactive data table. 
12. Create callback for database queries and map updates. 
13. Run the ipynb file and ensure the dashboard is fully functional and includes the necessary features, widgets, and tools.  

## Installation 
- MongoDB – This is used for our database. To install, simply go to https://www.mongodb.com/docs/manual/installation/ and select the desired operating system you will be using.  
- Pymongo – To install, simply go to https://pymongo.readthedocs.io/en/stable/installation.html and follow the manual instructions for installation.  
- Python – The programming language we will be using. To install, simply go to https://realpython.com/installing-python/ which has detailed instructions on installing the program.  
- Jupyter Notebooks – THe client-side dashboard will be created in this IDE and web tool. To install, simply go to https://jupyter.org/install and follow the installation instructions.  
- Dash – This framework allows us to build the web-based application. The framework can be installed by simply going to https://plotly.com/python/getting-started/ to get started. 
- Plotly – To create charts such as the pie chart or graph, plotly is a tool that can assist with this need. Simply review the instructions and documents at https://pypi.org/project/dash/ and follow the installation instructions provided on the website.  

## Reflection :pencil2:	
To write programs that are maintainable, readable, and adaptable, I ensure that the code is up to high standards such as in the areas of industry best practices. Additionally, utilizing encapsulation assisted in constructing code that would be readable, repeatable, and adaptable. The advantage of working with CRUD is that the developer can balance the various operations that are needed to take place for the database that was in Project One. To add on, CRUD is essential to implementing a database application. 

As a computer scientist, I believe that approaching a problem needs exceptional attention to detail and critical analysis of the issue at hand. Such as my approach to the database and dashboard requirements that Grazioso Salvare requested, I utilized tools such as Pymongo, Jupyter Notebook, and MongoDB. These tools not only made the process of building the project run smoothly but also helped to ensure that the expected outcome would result in success. My approach for this project differed from previous assignments in past courses because I had to implement the CRUD operation as well as the Mongo module to query the database. Additionally, with this project, it was vital to work on each principle of the CRUD method each week. This helped when it came to unit tests because it provided me with more time to integrate different structures for each CRUD functionality as well as ensuring that the minute details are up to standards. I would most definitely use the CRUD method in the future to create databases to meet other client requests. I also enjoyed how this project gave me a feel for real world scenarios. 

Computer scientists are unique individuals who provide specific expertise in the tech industry. Though this can be a very broad statement, computer scientists are the true brains behind technology. What they do, matters, because their work goes unnoticed especially when it comes to business functions. They play a major role in businesses running and without them business structures can crumble. My work on this type of project can help a company to do their work better because the companies and  team members can efficiently benefit from data being found fast and effectively. 

## Challenges 
While building the Dashboard web application, I encountered a challenge. Though, I was able to come overcome it. The challenge was formatting the chart and geolocation map so that they would be side by side. Additionally, the functionality of my dashboard wasn't up to my standards. Despite, I overcame these challenges by being more attentive to each detail and the CRUD operation to ensure that everything flowed all together. Despite the challenges, I truly enjoyed working on this project to create a successful dashboard using various tools and resources. 

## Screenshots :camera_flash:
### Starting State of the dashboard
![StartingState](https://user-images.githubusercontent.com/88872392/236719473-3be568d7-bbff-4fd8-8b06-d582c03d5413.png)
![Reset2](https://user-images.githubusercontent.com/88872392/236719483-5e8ffd1b-ac82-4e80-ab35-d25963dd7eb5.png)

### Water Rescue execution
![WaterRescue](https://user-images.githubusercontent.com/88872392/236719600-76b74b07-abaf-4057-b05b-e6d3b267d61c.png)
![WaterRescue2](https://user-images.githubusercontent.com/88872392/236719593-105ce524-8c17-4f48-91d5-2af3ab998521.png)

### Mountain or Wilderness Rescue execution
![MountainWildernessRescue](https://user-images.githubusercontent.com/88872392/236719628-c27fdd1c-284c-4148-9a9f-bcbf6e5724a2.png)
![MountainWildernessRescue2](https://user-images.githubusercontent.com/88872392/236719673-7d165afe-8037-400e-98ec-b45d65d567ba.png)

### Disaster or Individual Tracking execution
![DisasterIndividualTracking](https://user-images.githubusercontent.com/88872392/236719754-d90424e4-36ec-456a-984e-4a257e7c1c67.png)
![DisasterIndividualTracking2](https://user-images.githubusercontent.com/88872392/236719760-8a124beb-cb66-4e97-bd38-a24e4093d40f.png)

### Reset (returns all widgets to their original, unfiltered state) execution
![Reset](https://user-images.githubusercontent.com/88872392/236719777-e2dc5be0-a39f-4e4f-bc21-9c4dcf4ddd32.png)
![Reset2](https://user-images.githubusercontent.com/88872392/236719784-76c55d04-f629-4fa6-9e66-12a73cdb2d41.png)

---
*[Updated May 2023 by celinephil]*
