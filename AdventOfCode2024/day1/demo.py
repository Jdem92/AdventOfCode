from collections import Counter

#
class AdventOfCode:
    def AttemptAnswer(self, inputLines):
        leftColValues = []
        rightColValues = []
        rightColIdentifier = Counter()

        for line in inputLines:
            LeftValue, RightValue = line.split()
            
            LeftValue = int(LeftValue)
            RightValue = int(RightValue)

            leftColValues.append(LeftValue)
            rightColValues.append(RightValue)

            rightColIdentifier[RightValue] += 1

        leftColValues = sorted(leftColValues)
        rightColValues = sorted(rightColValues)

        answer1 = 0
        answer2 = 0

        for lVal, rVal in zip(leftColValues, rightColValues):
            answer1 += abs(lVal - rVal)
        print(answer1)

        for lVal in leftColValues:
            answer2 += lVal * rightColIdentifier.get(lVal, 0)
        print(answer2)

def main():
    attempter = AdventOfCode()
    
    data = open('input.txt').read().strip()
    inputLines = data.split('\n')

    attempter.AttemptAnswer(inputLines)

if "__main__":
    main()