# MEB With Multiple Components, single unit system, w/o tests for multiple unknowns for a single component
# Cameron Wood
# 05/13/2020

# Degree of Freedom Analysis
print("Degree of Freedom Analysis Initiating ...\n")
componentsNumber = int(input("How many components are there?  \n"))
unknowns = -int(input("How many unknowns are there?\n"))
DOFAnalysis = componentsNumber + unknowns
if DOFAnalysis < 0:
    print("System is underdetermined, please readjust your values, or take a basis: \n")

else:
    print("System fully determined, please proceed: \n")

    # Begin Collecting Information on Components
    print("We will now assign each component in the system a variable: \n")

    componentAssignmentList = []

    for componentAssignmentNumber in range(componentsNumber):
        componentAssignmentActual = input("Assign a variable to component " + str(componentAssignmentNumber) + " :\n")
        componentAssignmentList.append(componentAssignmentActual)

    # Start Collecting Data on Streams
    streamsInData = int(input("How many streams are entering the system?\n"))

    streamsList = []
    overallStreamsList = []

    for streamsInNumber in range(streamsInData):
        newStreamsList = []
        overallStream = int(input("What is the overall flow rate of Stream " + str(streamsInNumber) + " ?\n"))
        newStreamsList.append(overallStream)

        for streamsInComponentNumber in range(componentsNumber):
            newComponentValue = input("What is the value for component " +
                                      str(componentAssignmentList[streamsInComponentNumber]) + " in Stream " +
                                      str(streamsInNumber) + " ?\n")
            newStreamsList.append(newComponentValue)
        streamsList.append(newStreamsList)


    streamsOutData = int(input("How many streams are exiting the system?\n"))

    for streamsOutNumber in range(streamsOutData):
        newStreamsList = []
        overallStream = int(input("What is the overall flow rate of Stream " + str(streamsOutNumber) + " ?\n"))
        newStreamsList.append(overallStream)

        for streamsOutComponentNumber in range(componentsNumber):
            newComponentValue = input("What is the value for component " +
                                      str(componentAssignmentList[streamsOutComponentNumber]) + " in Stream " +
                                      str(streamsOutNumber) + " ?\n")
            newStreamsList.append(newComponentValue)
        streamsList.append(newStreamsList)

    # Begin going through Lists and setting ? = 0 or some other number

    for streamsAllNumber in range(len(streamsList)):
        for streamsAllComponentNumber in range(componentsNumber):
            b = streamsList[streamsAllNumber][streamsAllComponentNumber]
            if b == '?':
                b = 0
                streamsList[streamsAllNumber][streamsAllComponentNumber] = b
            else:
                b = int(b)
                streamsList[streamsAllNumber][streamsAllComponentNumber] = b

    # Now we can balance each equation respectively
    print("Calculating for unknowns ... \n")

    for streamsAllComponentNumber in range(componentsNumber):
        solvingListIn = []
        solvingListOut = []
        streamsInDataFixed = streamsInData - 1

        for streamsAllNumber in range(len(streamsList)):
            if streamsAllNumber <= streamsInDataFixed:
                i = streamsList[streamsAllNumber][streamsAllComponentNumber]
                solvingListIn.append(i)

            if streamsAllNumber > streamsInDataFixed:
                o = streamsList[streamsAllNumber][streamsAllComponentNumber]
                solvingListOut.append(o)

        x = sum(solvingListIn) - sum(solvingListOut)

        if x < 0:
            x = -x
        print("Unknown for component " +
              str(componentAssignmentList[streamsAllComponentNumber]) + " is equal to: " + str(x) + " \n")
