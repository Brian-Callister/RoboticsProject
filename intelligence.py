# Methods to work with
	# run(delayTime)
	# back(delayTime)
	# left(delayTime)
	# right(delayTime)
	# spin_left(delayTime)
	# spin_right(delayTime)
	# brake(delayTime)

from movement import run, back, left, right, spin_left, spin_right, brake
from random import randint

TIME_INCREMENT = 0.2 # seconds


def findBall():
	regionBall = getRegion()
	while regionBall == -1:
		spin_left(TIME_INCREMENT)

def findGoal():
	regionGoal = getRegionGoal()
	while regionGoal == -1:
		spin_left(TIME_INCREMENT)


def centerBall():
	
	regionBall = randint(-1, 2)

	if regionBall == -1:
		findBall()

	elif regionBall == 1:
		run(TIME_INCREMENT)
		break


	elif regionBall == 2:
		right(TIME_INCREMENT)


	elif regionBall == 0:
		left(TIME_INCREMENT)


def centerGoal():
	
	regionGoal = randint(0, 2)

	if regionGoal == -1:
		findGoal()

	elif regionGoal == 1:
		run(TIME_INCREMENT)
		break


	elif regionGoal == 2:
		right(TIME_INCREMENT)


	elif regionGoal == 0:
		left(TIME_INCREMENT)

def main():
	centerBall()
	# centerGoal()


