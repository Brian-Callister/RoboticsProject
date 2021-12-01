# Methods to work with
	# run(delayTime)
	# back(delayTime)
	# left(delayTime)
	# right(delayTime)
	# spin_left(delayTime)
	# spin_right(delayTime)
	# brake(delayTime)


TIME_INCREMENT = 0.2 # seconds


def findBall():
	regionBall = getRegion()
	while regionBall == -1:
		spin_left(TIME_INCREMENT)



def main():
	while True:
		regionBall = getRegion()

		if regionBall == -1:
			findBall()

		elif regionBall == 1:
			run(TIME_INCREMENT)


		elif regionBall == 2:
			right(TIME_INCREMENT)


		elif regionBall == 0:
			left(TIME_INCREMENT)



main()

