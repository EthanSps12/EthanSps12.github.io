#################################
# Sources: Introduction to Algorithms, Cormen, https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/,
# https://www.geeksforgeeks.org/merge-sort/
#################################

class Supply:
    def __init__(self):
        return

    def sortEdges(self, list):  # Using merge sort to sort the list of edges
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
            combineA = self.sortEdges(list[0:median])  # Recursive step, split list in 2 and merge sort each part
            combineB = self.sortEdges(list[median:len(list)])
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

    def findRoot(self, nodeNum, nodeTreeDict):  # Gets the root of the tree the given node is part of
        if nodeNum == nodeTreeDict[nodeNum][1]:  # If the parent of the node matches the node
            return nodeNum  # You are at the root, return that node
        return self.findRoot(nodeTreeDict[nodeNum][1], nodeTreeDict)  # Otherwise, recurse on the parent of this node

    def meetsConditions(self, edge, nodeDict, distCentersStoresList):
        nodeOneID = edge[0]
        nodeTwoID = edge[1]
        nodeOneType = nodeDict[nodeOneID][0]
        nodeTwoType = nodeDict[nodeTwoID][0]
        distCentersList = []
        for i in range(0, len(distCentersStoresList)):  # Creating a list of dist centers by node id
            distCentersList.append(distCentersStoresList[i][0])
        if (nodeOneType == "port" and nodeTwoType == "store") or (nodeOneType == "store" and nodeTwoType == "port"):
            return False  # Ports cant be connected to stores
        if (nodeOneType == "rail-hub" and nodeTwoType == "store") or \
                (nodeOneType == "store" and nodeTwoType == "rail-hub"):
            return False  # Rail hubs cant be connected to stores
        if nodeOneType == "dist-center" and nodeTwoType == "dist-center":
            return False  # Distribution centers cant be connected to another distribution center
        if nodeOneType == "dist-center" and nodeTwoType == "store":
            dCSListIndex = distCentersList.index(nodeOneID)
            if nodeTwoID not in distCentersStoresList[dCSListIndex][1]:
                return False  # Stores can only be connected to specific distribution centers
        if nodeOneType == "store" and nodeTwoType == "dist-center":
            dCSListIndex = distCentersList.index(nodeTwoID)
            if nodeOneID not in distCentersStoresList[dCSListIndex][1]:
                return False
        return True

    def KruskalsModded(self, disjointsets, edgeList, dist_stores):
        MST = []
        MSTSum = 0
        for i in range(0, len(edgeList)):  # Go through the sorted list of edges from smallest to largest
            if self.meetsConditions(edgeList[i], disjointsets, dist_stores):  # If adding the edge follows the rules
                # See if the edge connects two previously unconnected trees
                endOneRoot = self.findRoot(edgeList[i][0], disjointsets)
                endTwoRoot = self.findRoot(edgeList[i][1], disjointsets)
                if endOneRoot != endTwoRoot:
                    # Connect the nodes by setting the parent of one node equal to the other
                    disjointsets[endOneRoot][1] = endTwoRoot
                    MST.append(edgeList[i])  # Add edge to MST
        for j in range(0, len(MST)):  # Go through the MST and sum up the edge weights
            MSTSum += MST[j][2]
        return MSTSum

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        lineOne = file_data[0].split()  # Line 1 of the input tells you the number of nodes and edges in the input
        numNodes = int(lineOne[0])
        numEdges = int(lineOne[1])
        disjointsets = {}  # The dictionary that will hold the nodes and their parents
        edgeList = []
        nodeList_temp = []
        dist_stores_temp = []
        dist_stores = []
        for i in range(1, numNodes + 1):  # Storing the nodes from input in a list
            nodeData = file_data[i].split()
            nodeName = nodeData[0]
            nodeType = nodeData[1]
            nodeList_temp.append(nodeName)
            dist_stores_temp.append(nodeType)
            # Store each node and the root of the nodes tree, which here is itself
            disjointsets[i - 1] = [nodeType, i-1]
        for j in range(numNodes + 1, numNodes + 1 + numEdges):  # Storing the edges from input in a list
            edgeData = file_data[j].split()
            endOne = edgeData[0]
            endTwo = edgeData[1]
            edgeWeight = int(edgeData[2])
            indexOfOne = nodeList_temp.index(endOne)
            indexOfTwo = nodeList_temp.index(endTwo)
            edgeList.append([indexOfOne, indexOfTwo, edgeWeight])
        numDistCenters = -1
        for k in range(0, len(dist_stores_temp)):  # Seeing which distribution centers are associated with which stores
            if dist_stores_temp[k] == "dist-center":
                numDistCenters += 1
                dist_stores.append([k, []])
            if dist_stores_temp[k] == "store":
                dist_stores[numDistCenters][1].append(k)
        edgeList = self.sortEdges(edgeList)  # Sort the list of edges by length
        MSTWeight = self.KruskalsModded(disjointsets, edgeList, dist_stores)  # Get the minimum spanning tree weight
        return MSTWeight
