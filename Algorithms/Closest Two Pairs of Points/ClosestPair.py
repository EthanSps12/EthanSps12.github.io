# CS4102 Spring 2022 - Unit A Programming 
#################################
# Sources:
# https://www.programiz.com/python-programming/methods/string/index
# https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
# https://www.cuemath.com/geometry/distance-between-two-points/
# https://www.geeksforgeeks.org/merge-sort/
# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number
#################################

import math

class ClosestPair:
    def __init__(self):
        return

    def mergeSortByX(self, list):  # Initial merge sort by x values
        if len(list) == 1:  # Base case: if 1 item, already sorted
            return list
        elif len(list) == 2:  # Base case: if 2 items, sort then return
            newList = []
            if list[0][2] < list[1][2]:
                newList.append(list[0])
                newList.append(list[1])
            else:
                newList.append(list[1])
                newList.append(list[0])
            return newList
        else:  # If the list has 3+ items
            median = len(list) // 2
            combineA = self.mergeSortByX(list[0:median])  # Recursive step, split list in 2 and merge sort each part
            combineB = self.mergeSortByX(list[median:len(list)])
            toReturn = []
            a = b = 0  # Code from https://www.geeksforgeeks.org/merge-sort/  # Merging the two sorted lists
            while a < len(combineA) and b < len(combineB):  # While each sub-list is not empty
                if combineA[a][2] < combineB[b][2]:
                    # Take the smallest element of each list, compare them, and add the smaller to the new list
                    toReturn.append(combineA[a])
                    a += 1
                else:
                    toReturn.append(combineB[b])
                    b += 1
            while a < len(combineA):  # Once one of the lists are empty, add the rest of the other list
                toReturn.append(combineA[a])
                a += 1
            while b < len(combineB):
                toReturn.append(combineB[b])
                b += 1
            return toReturn

    def closest2Points(self, pointsList):  # Input: a list of points sorted by x value
        # Return format: shortest distance between two points, 2nd shortest distance between two points, and a the given
        # list sorted by y-value
        if len(pointsList) <= 1:  # Verifying more then one point is passed.
            print("Error: closest2Points passed 1 point or less; minimum number of points is 2.")
            exit(-1)
        if len(pointsList) == 2:  # Base case: 2 points. Not ideal since it returns an default second-shortest length.
            # Only used if sublist is too small.
            dist = math.sqrt((pointsList[1][0] - pointsList[0][0]) ** 2 + (pointsList[1][1] - pointsList[0][1]) ** 2)
            return dist, 100001, [min(pointsList), max(pointsList)]
            # 100001 is a dummy value for the nonexistent 2nd pair of points
        elif len(pointsList) == 3:  # Base case: 3 points
            # Computing the distance
            dist01 = math.sqrt((pointsList[1][0] - pointsList[0][0]) ** 2 + (pointsList[1][1] - pointsList[0][1]) ** 2)
            dist02 = math.sqrt((pointsList[2][0] - pointsList[0][0]) ** 2 + (pointsList[2][1] - pointsList[0][1]) ** 2)
            dist12 = math.sqrt((pointsList[2][0] - pointsList[1][0]) ** 2 + (pointsList[2][1] - pointsList[1][1]) ** 2)
            # Finding the smallest two distances
            threePoints = [dist01, dist02, dist12]
            min3Pts = min(threePoints)
            threePoints.remove(min3Pts)
            secondMin3Pts = min(threePoints)
            # Sorting the points by their Y values
            sorted3Pts = []
            if pointsList[0][1] <= pointsList[1][1] and pointsList[0][1] <= pointsList[2][1]:
                sorted3Pts.append(pointsList[0])
            elif pointsList[1][1] <= pointsList[2][1] and pointsList[1][1] <= pointsList[0][1]:
                sorted3Pts.append(pointsList[1])
            else:
                sorted3Pts.append(pointsList[2])
            if pointsList[0] in sorted3Pts:
                if pointsList[1][1] < pointsList[2][1]:
                    sorted3Pts.append(pointsList[1])
                    sorted3Pts.append(pointsList[2])
                else:
                    sorted3Pts.append(pointsList[2])
                    sorted3Pts.append(pointsList[1])
            elif pointsList[1] in sorted3Pts:
                if pointsList[0][1] < pointsList[2][1]:
                    sorted3Pts.append(pointsList[0])
                    sorted3Pts.append(pointsList[2])
                else:
                    sorted3Pts.append(pointsList[2])
                    sorted3Pts.append(pointsList[0])
            else:
                if pointsList[0][1] < pointsList[1][1]:
                    sorted3Pts.append(pointsList[0])
                    sorted3Pts.append(pointsList[1])
                else:
                    sorted3Pts.append(pointsList[1])
                    sorted3Pts.append(pointsList[0])
            return min3Pts, secondMin3Pts, sorted3Pts
        elif len(pointsList) == 4:  # Base case: 4 points.
            # Computing the distances between the points.
            dist01 = math.sqrt((pointsList[1][0] - pointsList[0][0]) ** 2 + (pointsList[1][1] - pointsList[0][1]) ** 2)
            dist02 = math.sqrt((pointsList[2][0] - pointsList[0][0]) ** 2 + (pointsList[2][1] - pointsList[0][1]) ** 2)
            dist12 = math.sqrt((pointsList[2][0] - pointsList[1][0]) ** 2 + (pointsList[2][1] - pointsList[1][1]) ** 2)
            dist03 = math.sqrt((pointsList[3][0] - pointsList[0][0]) ** 2 + (pointsList[3][1] - pointsList[0][1]) ** 2)
            dist13 = math.sqrt((pointsList[3][0] - pointsList[1][0]) ** 2 + (pointsList[3][1] - pointsList[1][1]) ** 2)
            dist23 = math.sqrt((pointsList[3][0] - pointsList[2][0]) ** 2 + (pointsList[3][1] - pointsList[2][1]) ** 2)
            # Finding the smallest two distances.
            sixDistances = [dist01, dist02, dist12, dist03, dist13, dist23]
            min6Dists = min(sixDistances)
            sixDistances.remove(min6Dists)
            secondMin6Dists = min(sixDistances)
            # Sorting the points by their Y values.
            sorted4Pts = []
            fourYVals = [pointsList[0][1], pointsList[1][1], pointsList[2][1], pointsList[3][1]]
            while len(fourYVals) > 0:
                minPoint = min(fourYVals)
                if minPoint == pointsList[0][1]:
                    sorted4Pts.append(pointsList[0])
                    fourYVals.remove(pointsList[0][1])
                elif minPoint == pointsList[1][1]:
                    sorted4Pts.append(pointsList[1])
                    fourYVals.remove(pointsList[1][1])
                elif minPoint == pointsList[2][1]:
                    sorted4Pts.append(pointsList[2])
                    fourYVals.remove(pointsList[2][1])
                else:
                    sorted4Pts.append(pointsList[3])
                    fourYVals.remove(pointsList[3][1])
            return min6Dists, secondMin6Dists, sorted4Pts
        else:  # For lists with more than 4 points
            median = len(pointsList)//2
            # Recursive step: running this method on points left and right of the median
            resultsA = self.closest2Points(pointsList[0:median])
            resultsB = self.closest2Points(pointsList[median:len(pointsList)])
            # Finding the shortest and second-shortest points
            shortestA = resultsA[0]
            shortestB = resultsB[0]
            secondShortestA = resultsA[1]
            secondShortestB = resultsB[1]
            if shortestA < shortestB:
                delta = shortestA  # Delta = shortest distance between 2 points
                secondDelta = min(shortestB, secondShortestA)
            else:
                delta = shortestB
                secondDelta = min(shortestA, secondShortestB)
            # Merging the sub-lists by their Y values
            sublistA = resultsA[2]
            sublistB = resultsB[2]
            sortedByY = []
            a = b = 0  # Code from https://www.geeksforgeeks.org/merge-sort/
            while a < len(sublistA) and b < len(sublistB):
                if sublistA[a][1] < sublistB[b][1]:
                    sortedByY.append(sublistA[a])
                    a += 1
                else:
                    sortedByY.append(sublistB[b])
                    b += 1
            while a < len(sublistA):
                sortedByY.append(sublistA[a])
                a += 1
            while b < len(sublistB):
                sortedByY.append(sublistB[b])
                b += 1
            # Constructing the runway
            # The runway is used to compare distances between points on opposite sides of the median
            runwayL = pointsList[median][0] - secondDelta
            runwayR = pointsList[median][0] + secondDelta
            runwayPoints = []
            for point in sortedByY:
                if runwayL <= point[0] <= runwayR:
                    runwayPoints.append(point)
            # Evaluating runway points
            # If there are 8 or more runway points
            if len(runwayPoints) >= 8:
                # For each runway point (until the last 7 or so)
                for p in range(0, len(runwayPoints) - 7):
                    # Consider the next 7 points
                    for i in range(1, 8):
                        # If they are on opposite sides of the median
                        if not (((runwayPoints[p][0] < pointsList[median][0]) and (
                                runwayPoints[p+i][0] < pointsList[median][0])) or (
                                (runwayPoints[p][0] >= pointsList[median][0]) and (
                                runwayPoints[p+i][0] >= pointsList[median][0]))):
                            # Compute the distance, and update deltas if necessary
                            dist = math.sqrt((runwayPoints[p + i][0] - runwayPoints[p][0]) ** 2 + (
                                    runwayPoints[p + i][1] - runwayPoints[p][1]) ** 2)
                            if dist < delta:
                                secondDelta = delta
                                delta = dist
                            elif dist < secondDelta:
                                secondDelta = dist
                # This handles the last points, when there are fewer than 7 next points
                for i in range(1, 7):
                    if not (((runwayPoints[-7][0] < pointsList[median][0]) and (
                            runwayPoints[i-7][0] < pointsList[median][0])) or (
                            (runwayPoints[-7][0] >= pointsList[median][0]) and (
                            runwayPoints[i-7][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 7][0] - runwayPoints[-7][0]) ** 2 + (
                                runwayPoints[i - 7][1] - runwayPoints[-7][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
                for i in range(1, 6):
                    if not (((runwayPoints[-6][0] < pointsList[median][0]) and (
                            runwayPoints[i-6][0] < pointsList[median][0])) or (
                            (runwayPoints[-6][0] >= pointsList[median][0]) and (
                            runwayPoints[i-6][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 6][0] - runwayPoints[-6][0]) ** 2 + (
                                runwayPoints[i - 6][1] - runwayPoints[-6][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
                for i in range(1, 5):
                    if not (((runwayPoints[-5][0] < pointsList[median][0]) and (
                            runwayPoints[i-5][0] < pointsList[median][0])) or (
                            (runwayPoints[-5][0] >= pointsList[median][0]) and (
                            runwayPoints[i-5][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 5][0] - runwayPoints[-5][0]) ** 2 + (
                                runwayPoints[i - 5][1] - runwayPoints[-5][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
                for i in range(1, 4):
                    if not (((runwayPoints[-4][0] < pointsList[median][0]) and (
                            runwayPoints[i-4][0] < pointsList[median][0])) or (
                            (runwayPoints[-4][0] >= pointsList[median][0]) and (
                            runwayPoints[i-4][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 4][0] - runwayPoints[-4][0]) ** 2 + (
                                runwayPoints[i - 4][1] - runwayPoints[-4][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
                for i in range(1, 3):
                    if not (((runwayPoints[-3][0] < pointsList[median][0]) and (
                            runwayPoints[i-3][0] < pointsList[median][0])) or (
                            (runwayPoints[-3][0] >= pointsList[median][0]) and (
                            runwayPoints[i-3][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 3][0] - runwayPoints[-3][0]) ** 2 + (
                                runwayPoints[i - 3][1] - runwayPoints[-3][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
                for i in range(1, 2):
                    if not (((runwayPoints[-2][0] < pointsList[median][0]) and (
                            runwayPoints[i-2][0] < pointsList[median][0])) or (
                            (runwayPoints[-2][0] >= pointsList[median][0]) and (
                            runwayPoints[i-2][0] >= pointsList[median][0]))):
                        dist = math.sqrt((runwayPoints[i - 2][0] - runwayPoints[-2][0]) ** 2 + (
                                runwayPoints[i - 2][1] - runwayPoints[-2][1]) ** 2)
                        if dist < delta:
                            secondDelta = delta
                            delta = dist
                        elif dist < secondDelta:
                            secondDelta = dist
            else:  # If there are less than 8 runway points
                # For every runway point (except the last, because then we considered every pair)
                for p in range(0, len(runwayPoints) - 1):
                    # For the next points until the end of the runway
                    for i in range(1, len(runwayPoints) - p):
                        # If they are on opposite sides
                        if not (((runwayPoints[p][0] < pointsList[median][0]) and (
                                runwayPoints[p+i][0] < pointsList[median][0])) or (
                                (runwayPoints[p][0] >= pointsList[median][0]) and (
                                runwayPoints[p+i][0] >= pointsList[median][0]))):
                            # Compute the distance and update the deltas if necessary
                            dist = math.sqrt((runwayPoints[p + i][0] - runwayPoints[p][0]) ** 2 + (
                                    runwayPoints[p + i][1] - runwayPoints[p][1]) ** 2)
                            if dist < delta:
                                secondDelta = delta
                                delta = dist
                            elif dist < secondDelta:
                                secondDelta = dist
            return delta, secondDelta, sortedByY

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
    def compute(self, file_data):

        # Converting from a list of strings to a list of list of x and y values. O(n).
        for i in range(0,len(file_data)):
            file_data[i] = file_data[i].split()
            file_data[i][0] = float(file_data[i][0])
            file_data[i][1] = float(file_data[i][1])

        # Sorting by x. O(n log n).
        pointsByX = self.mergeSortByX(file_data)

        # Preparation done, calling the main recursive function.
        results = self.closest2Points(pointsByX)
        closest = results[0]
        secondClosest = results[1]
        return [closest, secondClosest]  # Returning the two closest pairs of points
