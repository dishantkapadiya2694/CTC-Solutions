"""Given a NxN image where each cell is a pixel, rotate that image by 90 degrees. can you do it inplace?"""
from math import ceil

def rotateImage(image):
    rotatedImage = []
    for i in range(len(image)):
        temp = []
        for j in range(len(image)):
            temp.append(-1)
        rotatedImage.append(temp)

    for i in range(len(image)):
        for j in range(len(image)):
            rotatedImage[len(image)-j-1][i] = image[i][j]

    return rotatedImage

def rotateImageInPlace(image):
    temp = 0
    length = len(image)
    for a in range(len(image)/2):
        first = a
        last = length - a - 1
        for i in range(first, last):
            offset = i - first
            temp = image[first][i]
            image[first][i] = image[i][last]
            image[i][last] = image[last][last - offset]
            image[last][last - offset] = image[last - offset][first]
            image[last - offset][first] = temp
            print image




image = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

rotatedImage = [[3, 6, 9],
                [2, 5, 8],
                [1, 4, 7]]

#rotateImage(image)
rotateImageInPlace(image)