# SplitBFriends

**SplitBFriends** is a simple Python program to make balance between friends expenses !

## How to use

To launch the program simply run the command line :
`python SplitBFriends.py`

You may use option `-v` (or `--visualization`) for data visualization :
`python SplitBFriends.py -v`

Here is the help menu :
```
>python SplitBFriends.py -h
usage: SplitBFriends.py [-h] [-v] [-f]

Split expenses between friends, let's Split and Be Friends !

optional arguments:
  -h, --help           show this help message and exit
  -v, --visualization  Generate visualization of balances
  -f, --french         Use SlipBFriends in french
```

## Program output

Here is an example of the program output :

```
>python SplitBFriends.py

############
## Event : 
############

	● Number of friends ? > 4
	
############
## Friend n° : 1
############

	● Name ? > Harry
	● Paid amount ? > 54.87
	
############
## Friend n° : 2
############

	● Name ? > Ron
	● Paid amount ? > 23.98
	
############
## Friend n° : 3
############

	● Name ? > Hermione
	● Paid amount ? > 87.12
	
############
## Friend n° : 4
############

	● Name ? > Voldemort
	● Paid amount ? > 125.50
	
############
## Balance summary : 
############

	● Total amount > 291.47€
	● Amount by friend > 72.87€
	● Friend [Harry] should pay 14.25€ to [Hermione]
	● Friend [Harry] should pay 3.75€ to [Voldemort]
	● Friend [Ron] should pay 48.89€ to [Voldemort]
```

## Visualization

Here is an example of output visualization :

![Output visualization](/resources/data_visualization.png)

## Requirements

SplitBFriends requires _matplotlib_ Python library for generating data visualization.
Please see the official [matplotlib documentation](https://matplotlib.org) to know how to install it.