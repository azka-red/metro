# metro.py

This simple script is the conclusion of a homework given to me by a certain recruiter. The homework required me to create a repository for it, and here it is!

 ## Problem proposed
 
Write a program that allows you to calculate the route with the fewest stations between two stations of a metro network. In the metro network some stations may have an associated color (Red or Green) that indicates that a Green express train will pass alone through stations without color or Green, and a Red colored express train will pass only through stations no color or red.

For example, for the image in the figure: 
 
 ![alt text](https://github.com/azka-red/metro/blob/main/problem.PNG?raw=true)
 
 The shortest route between A and F is:
- If it is a red train: A-> B-> C-> H-> F.
- If it is a green train there are two possible routes: A-> B-> C-> D-> E-> F and A-> B-> C-> G-> I-> F
- If it is a train without color: A-> B-> C-> D-> E-> F. 
 
First, you will have to design the file format that the program will receive as input
to represent a subway network.
Your program should receive as parameters:
- The file you designed that describes the network
- A starting station
- A final station
- One train color Red or Green (optional)
And have as a result the smallest route according to the parameters, indicating all the stations
that compose it. In case there is more than one, it is enough to return one
any as a result. 
 
 
 ## Requirements
 
- Python 3.7+
- matplotlib==3.4.2
- networkx==2.5.1

Matplotlib and Networkx are used to display a .png image of the output graphs. The Graphs implementation and path finding routine is done from scratch here.


## Usage

Using metro.py is easy, the command sintaxis is the following

```
python metro.py <graph file> <starting node> <ending node> [color]
```

where:

- graph file : The file with the directed graph data. You can find an example of this file on this repository(example.graph).
- starting node : The name of the node where metro.py will begin to trace a path.
- ending node : The name of the node where metro.py stops (destination).
- color (optional) : The color of the train used to trace the path in the graph. It can be either "red", "green" or "white". It defaults to "white".

## Example

### Input

```
$ python metro.py example.graph A F green
```

### Output

Command prompt :
```
[A]->[B]->[C]->[D]->[E]->[F] [A]->[B]->[C]->[G]->[I]->[F] 
```
Output images :
![alt text](https://github.com/azka-red/metro/blob/main/output1.png?raw=true)

![alt text](https://github.com/azka-red/metro/blob/main/output2.png?raw=true)
