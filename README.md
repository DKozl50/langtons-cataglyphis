# Langton's Cataglyphis 

> *Cataglyphis bombycina* is the fastest of the world’s known ant species, clocking a velocity of 855 millimetres per second

## Introdiction

I think it has been over 7 years scince I have first learned about Langton's Ant from [Numberphile's video](https://www.youtube.com/watch?v=NWBToaXK5T0). 

After trying out a couple of configurations I found out configuration `RRRLL` which did not seem to repeat.   
Well, after my experiment ran for a trillion-or-so steps over more than a month and did not lead to any results, I stopped my VM and abandoned any hopes of reaching this configuration's "end".

Now, after so many years of occasionally remembering about this challenge and after getting a bit more experience in programming, I guess it is time to simulate Langton's Ant once again.

## Goal

In this ambitiously named repository I will document my attempts at wrighting fast Python code for simulating Langton's Ant. 

Every implementation should be able to work with any correct Langton's Ant configuration on a square grid. Currently I am only considering Left and Right moves but I guess it will be easy to generalize to other moves (Forward, U-turn...).

Implementations will be measured on how fast can they emulate a given configuration until the ant leaves a grid.
