# Creating-map-for-stating-machine

## General info
This software was created to create a map for implementing a state machine in graphical implementation  
Repositiry consists of four files:
* main
* robot
* map
* support

<a href = 'https://github.com/ksen322/Creating-map-for-stating-machine/blob/main/main.py'>*main*</a> implements the main code that runs the main loop of the programm and icnludes map and robot files    

## Control
S - starting point selection  
G - ending point selection 
O - points of obstacles selection  
Space - fixed the changes  
W - running robots

# Description of programms

## Main
The programm is constructor for launching the graphical window of the pygame library   
Также в программе создаются экзмепляр класса Map и 3 экземпляра класса Robot  
Thanks to the simplest state machine mechanism the programm is initialized in the __Creating map__ state    
FAfter finishing editing the map using W button the programm goes into the __Simulating work__ state   
In this state instances of the Robot class are initialized and subsequently rendered  

## Map
This code perfoms the following graphical functions:
* drawing a background in the form of chess grid  
* drawing a start point  
* drawing an end point  
* drawing an obstacles

Inside class Map, firstly, an empty map is created as a two-dimensional array   
Next, using the state machine we can switch to different editing modes   
The first mode is launched using S button and allows select the starting position using LMB   
The second mode - select end point using G button  
The third mode selected using O button and allows to set obstacles using LMB and delete them using RMB   
It is important to understand that whtn adding any of the above points logical checks are made to see if it is impossible to place one point in another (you can't put the starting position in the place of an obstacle or end point and etc.)

## Robot
This code is template  
There is a constructor inside the class for changing the states of the robot  
Only the rendering function is practically implemented    

## Support
This code is auxiliary  
It emplements 2 functions:  
* drawing cell at given coordinates  
* drawing text at given coordinates  
