k = 12
a = [1, 2, 3,4,5,6,7,8,9,10]

rotation = k 
ourArray = a

# def rotate(listToRotation)
arrayLength = len(ourArray)

def fixRotationLength(rotations, lengthOfArray):
	if rotations > lengthOfArray:
		rotations = rotations - lengthOfArray

		if rotations > lengthOfArray:
			fixRotationLength(rotations, lengthOfArray)

	return rotations





actualRotations = fixRotationLength(rotation, arrayLength)
print(actualRotations)

rotationCountCheck = rotation
upperArray = arrayLength - rotation

lastElements = [ourArray[-actualRotations:]]
firstElement = ourArray[0:-actualRotations]

# print(lastElements,firstElement)
print(lastElements[0:][0]+firstElement)
solution = lastElements[0:][0]+firstElement

# return solution 
