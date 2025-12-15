# CS4102 Spring 2022 -- Unit C Programming
#################################
# Sources: Introduction to Algorithms, Cormen,
# https://stackoverflow.com/questions/11902458/i-want-to-exception-handle-list-index-out-of-range,
# https://www.i2tutorials.com/what-are-negative-indexes-and-why-are-they-used,
# https://www.w3schools.com/python/ref_list_append.asp
#################################
import math

class SeamCarving:
    def __init__(self):
        return

    def weightOf(self, x, y):
        # My strategy is to find the average difference in color between this pixel and each of its surrounding pixels.
        if x == 0 and y == 0:
            # If the pixel is the top left corner, look at the pixels below it, to the right, and to the lower right
            return (self.diffBtwnPixels(imageStuff[0][0], imageStuff[0][1]) + self.diffBtwnPixels(imageStuff[0][0], imageStuff[1][0]) +
                    self.diffBtwnPixels(imageStuff[0][0], imageStuff[1][1])) / 3
        elif x == 0 and y == len(imageStuff) - 1:
            # If the pixel is the bottom left corner, look at the pixels above it, to the right, and to the upper right
            return (self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][0], imageStuff[len(imageStuff) - 1][1]) +
                    self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][0], imageStuff[len(imageStuff) - 2][0]) +
                    self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][0], imageStuff[len(imageStuff) - 2][1])) / 3
        elif x == len(imageStuff[0]) - 1 and y == 0:
            # If the pixel is the top right corner, look at the pixels below it, to the left, and to the lower left
            return (self.diffBtwnPixels(imageStuff[0][len(imageStuff[0]) - 1], imageStuff[0][len(imageStuff[0]) - 2])
                    + self.diffBtwnPixels(imageStuff[0][len(imageStuff[0]) - 1], imageStuff[1][len(imageStuff[0]) - 1])
                    + self.diffBtwnPixels(imageStuff[0][len(imageStuff[0]) - 1],
                                          imageStuff[1][len(imageStuff[0]) - 2])) / 3
        elif x == len(imageStuff[0]) - 1 and y == len(imageStuff) - 1:
            # If the pixel is the bottom right corner, look at the pixels above it, to the left, and to the upper left
            return (self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][len(imageStuff[0]) - 1], imageStuff[len(imageStuff) - 1]
            [len(imageStuff[0]) - 2]) + self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][len(imageStuff[0]) - 1],
                                                            imageStuff[len(imageStuff) - 2][len(imageStuff[0]) - 1]) +
                    self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][len(imageStuff[0]) - 1], imageStuff[len(imageStuff) - 2]
                    [len(imageStuff[0]) - 2])) / 3
        elif x == 0 and y != 0 and y != len(imageStuff) - 1:
            # If the pixel is on the left edge, look at the pixels above and below it, to its right, and to its upper
            # and lower right
            return (self.diffBtwnPixels(imageStuff[y][0], imageStuff[y - 1][0]) +
                             self.diffBtwnPixels(imageStuff[y][0], imageStuff[y + 1][0]) +
                             self.diffBtwnPixels(imageStuff[y][0], imageStuff[y - 1][1]) +
                             self.diffBtwnPixels(imageStuff[y][0], imageStuff[y][1]) +
                             self.diffBtwnPixels(imageStuff[y][0], imageStuff[y + 1][1])) / 5
        elif x == len(imageStuff[0]) - 1 and y != 0 and y != len(imageStuff) - 1:
            # If the pixel is on the right edge, look at the pixels above and below it, to its left, and to its upper
            # and lower left
            return (self.diffBtwnPixels(imageStuff[y][len(imageStuff[0]) - 1], imageStuff[y + 1][len(imageStuff[0]) - 1]) +
                                          self.diffBtwnPixels(imageStuff[y][len(imageStuff[0]) - 1], imageStuff[y - 1][len(imageStuff[0]) - 1]) +
                                          self.diffBtwnPixels(imageStuff[y][len(imageStuff[0]) - 1], imageStuff[y + 1][len(imageStuff[0]) - 2]) +
                                          self.diffBtwnPixels(imageStuff[y][len(imageStuff[0]) - 1], imageStuff[y][len(imageStuff[0]) - 2]) +
                                          self.diffBtwnPixels(imageStuff[y][len(imageStuff[0]) - 1], imageStuff[y - 1][len(imageStuff[0]) - 2])) \
                                             / 5
        elif y == 0 and x != 0 and x != len(imageStuff[0]) - 1:
            # If the pixel is on the top edge, look at the pixels below it, to its left and right, and to its lower left
            # and lower right
            return (self.diffBtwnPixels(imageStuff[0][x], imageStuff[0][x - 1]) +
                             self.diffBtwnPixels(imageStuff[0][x], imageStuff[0][x + 1]) +
                             self.diffBtwnPixels(imageStuff[0][x], imageStuff[1][x - 1]) +
                             self.diffBtwnPixels(imageStuff[0][x], imageStuff[1][x]) +
                             self.diffBtwnPixels(imageStuff[0][x], imageStuff[1][x + 1])) / 5
        elif y == len(imageStuff) - 1 and x != 0 and x != len(imageStuff[0]) - 1:
            # If the pixel is on the bottom edge, look at the pixels above it, to its left and right, and to its upper
            # left and upper right
            return (self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][x], imageStuff[len(imageStuff) - 1][x - 1]) +
                                          self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][x], imageStuff[len(imageStuff) - 1][x + 1]) +
                                          self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][x], imageStuff[len(imageStuff) - 2][x - 1]) +
                                          self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][x], imageStuff[len(imageStuff) - 2][x]) +
                                          self.diffBtwnPixels(imageStuff[len(imageStuff) - 1][x], imageStuff[len(imageStuff) - 2][x + 1])) \
                                         / 5
        else:  # If the pixel has 8 other pixels surrounding it, look at all of those
            return (self.diffBtwnPixels(imageStuff[y][x], imageStuff[y - 1][x - 1]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y - 1][x]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y - 1][x + 1]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y][x - 1]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y][x + 1]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y + 1][x - 1]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y + 1][x]) +
                                 self.diffBtwnPixels(imageStuff[y][x], imageStuff[y + 1][x + 1])) / 8

    def diffBtwnPixels(self, A, B):  # Find the difference in color between pixels A and B
        redPart = (B[0] - A[0])**2
        bluePart = (B[1] - A[1])**2
        greenPart = (B[2] - A[2])**2
        return math.sqrt(redPart + bluePart + greenPart)

    def traceMinSeam(self, x, y):
        if y == lenWeightsY - 1:  # If this is the lowest pixel, return that pixel
            return [x]
        if x == 0:  # If this is the leftmost pixel
            goToVal = min(weights[y+1][x], weights[y+1][x+1])  # Go down or to the right, whichever has less weight
            if goToVal == weights[y+1][x]:
                chosen = "down"
            else:
                chosen = "right"
        elif x == lenWeightsX - 1:  # If this is the rightmost pixel
            goToVal = min(weights[y+1][x-1], weights[y+1][x])  # Got down or to the left, whichever has less weight
            if goToVal == weights[y+1][x-1]:
                chosen = "left"
            else:
                chosen = "down"
        else:  # Otherwise, go down, left, or right, whichever has less weight
            goToVal = min(weights[y+1][x-1], weights[y+1][x], weights[y+1][x+1])
            if goToVal == weights[y+1][x-1]:
                chosen = "left"
            elif goToVal == weights[y+1][x]:
                chosen = "down"
            else:
                chosen = "right"
        if chosen == "down":
            goToIndex = x
        elif chosen == "left":
            goToIndex = x-1
        else:
            goToIndex = x+1
        listSoFar = self.traceMinSeam(goToIndex, y+1)  # Recurse on the next lower pixel chosen
        listSoFar.append(x)  # Add this pixel to the list
        return listSoFar  # Return list of x values of the min weight seam

    def findMinSeam(self):
        minSeam = self.s3(0, 0)  # Find the min weight seam starting from the top left
        # Go through the top row, and see if the min weight seam starting from any of those pixels has less weight
        for topX in range(1, len(weights[0])):
            current = self.s3(topX, 0)
            if current < minSeam:
                minSeam = current
        minX = weights[0].index(minSeam)  # The x-value of the top row that results in the overall min weight seam
        global bestSeam
        bestSeam = self.traceMinSeam(minX, 0)  # Getting the x-values that make up the min seam
        bestSeam.reverse()
        return minSeam

    def s3(self, x, y):  # Returns the weight of the min weight seam starting from x, y
        if y >= lenWeightsY:  # If this function considers pixels below the bottom of the image
            return 0
        if x < 0 or x >= lenWeightsX:  # If this function considers pixels outside the image to the left or right
            return 9999999999999999999
        storedVal = weights[y][x]  # Weights is used to store the weight of the min weight seam starting from that pixel
        if storedVal != -1:  # If we already calculated the weight of that pixel, use that value
            return storedVal
        downL = self.s3(x - 1, y + 1)  # Find the weights of the pixels below, to the below left, and to the below right
        downM = self.s3(x, y + 1)
        downR = self.s3(x + 1, y + 1)
        vals = [downL, downM, downR]
        best = vals.index(min(vals))  # Finding which of the three lower pixels has the least weight
        myWeight = self.weightOf(x, y)  # Calculating the weight of the current pixel
        if best == 0:  # Depending on which lower pixel had the least weight
            # Store the weight of that pixel and the weight of this pixel as the weight of the min weight seam from the
            # current pixel
            weights[y][x] = downL + myWeight
            return downL + myWeight
        elif best == 1:
            weights[y][x] = downM + myWeight
            return downM + myWeight
        else:
            weights[y][x] = downR + myWeight
            return downR + myWeight

    def seamVerifier(self, listOfXs):  # Used in testing this program
        for i in range(len(listOfXs)):
            correct = True
            if i != 0:
                thisVal = listOfXs[i]
                lastVal = listOfXs[i-1]
                # Making sure the seam does not move more than 1 pixel in the x direction
                if not((thisVal == lastVal) or (thisVal == lastVal - 1) or (thisVal == lastVal + 1)):
                    correct = False
        return correct

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        # Image consists of the RBG values of each pixel, stored inside a list of lists that represents the x (inner
        # list) y (outer list) coordinates of each pixel
        global imageStuff
        imageStuff = image

        # Make weights a list of lists the same size as the picture, with -1 in the place of every pixel
        global weights
        weights = [[]]*len(image)
        for y in range(0, len(image)):
            weights[y] = [-1]*len(image[0])

        global lenWeightsX
        global lenWeightsY
        lenWeightsX = len(weights[0])
        lenWeightsY = len(weights)
        return self.findMinSeam()

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return bestSeam
