import asyncio.events as ae
import datetime
import os
from pathlib import *
from tkinter import (ACTIVE, BASELINE, HORIZONTAL, BaseWidget, CallWrapper,
                     Frame, Grid)
from typing import Any


def myFunction   (input1,input2, )   :
	result   =   input1+input2
	if result>10:
		print('The result is greater than 10')
	else   :
		print   (   "The result is less than or equal to 10"   )
	return result


def anotherFunction   (x, y,z  )   :
	if x>10   :
		y   = y   *   z

	return y


def main()   :
	input1= 5
	input2=   7
	output= myFunction(input1,input2)
	print   (   'The final output is:' , output   )

	anotherFunction(12,3,4)
if   __name__  ==  '__main__':
  main()