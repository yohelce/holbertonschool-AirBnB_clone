### Airbnb Clone

#### Description
> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: Amenity, City, State, Place,
> Review), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances.

After a few months, we will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![steps](https://i.imgur.com/9WkM9nn.png)

And the final data diagram looks like this:

![data_diagram](https://i.imgur.com/I7VURNR.jpg)

## What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Resources
Read or watch:

* cmd module
* packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Installation
```
git clone https://github.com/yohelce/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone.git
```

### Start using the console
start the console with
```./console```
you will see:
```(hbnb)```
and can start to use the hbnb console
## How to use the HBNB console
### Syntax:
``` <command> <classname> <id>```
Warming! <id> don't apply to create command

##|Commands|how to use it in the command interpreter|Instance form|Description
---|---|---|---|---
0.0|quit|```quit```||Exit the program
0.1|EOF|```EOF```||Exit the program
0.2|empty line|``` ```||not do nothing
0.3|create|```create <class name>```|| create an instance of the class
0.4|show|```show <class name> <id number>```|```<class name>.show(<id>)```|Prints the string representation of an instance based on the class name and id
0.5|destroy|```destroy <class name> <id number>```|```<class name>.destroy(<id>)```|Deletes an instance based on the class name and id (save the change into the JSON file)
0.6|all|```all``` or ```all <class name>```|```<class name>.all()```|Prints all string representation of all instances based or not on the class name
0.7|update|```update <class name> <id number> <attribute to update> "<new value of attribute>"```|simple form:```<class name>.update(<id>, <attribute name>, <attribute value>)``` update more than 1 attribute(using dictionaries): ```<class name>.update(<id>, <dictionary representation>)```|Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). If there are more commands, the command interpreter will only count the first attribute with its value
0.8|count|```count <class name>```|```<class name>.count()```|retrieve the number of instances of a class

### Examples:
#### For Help:
```
(hbnb)help create
create a new instace of a class
(hbnb)
```
#### For standard commands:
```
(hbnb)create User
993e570d-9b4e-449c-84b3-085ab454d3ce
(hbnb)
```
It will create a new <User> and returns its <id>

``` 
(hbnb)create BaseModel
a871be23-73d9-4fbd-92f5-fe9ec7054m2n
(hbnb)show BaseModel a871be23-73d9-4fbd-92f5-fe9ec7054m2n
[BaseModel] (a871be23-73d9-4fbd-92f5-fe9ec7054m2n) {'id': 'a871be23-73d9-4fbd-92f5-fe9ec7054m2n', 'created_at': '2022-07-04T02:20:53.149558', 'updated_at': '2022-07-04T02:20:53.149791'}
(hbnb)
```

It will create a new BaseModel and shows the objects of the instance
 
```
(hbnb)destroy BaseModel a871be23-73d9-4fbd-92f5-fe9ce7054m2n
['BaseModel', 'a871be23-73d9-4fbd-92f5-fe9ce7054m2n']
(hbnb)
```

It will destroy the BaseModel with <'id': 'a871be23-73d9-4fbd-92f5-fe9ce7054m2n'>

## Authors:
* Christian Varas |   <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> [GitHub](https://github.com/ChristianVaras) | [Medium](https://medium.com/@christianvaras-2020)
* Yohel Cruz | <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" />[GitHub](https://github.com/yohelce) | [Medium](https://medium.com/@yohel.cruz.espinoza)
