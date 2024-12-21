#from collections import Counter

class AdventOfCode:
    def AttemptAnswer(self, inputNumbers: list[int]) -> bool:
        diffs = [abs(pos1 - pos2) for pos1, pos2 in zip(inputNumbers, inputNumbers[1:])]

        if not all(1 <= d <= 3 for d in diffs):
            return False
        if all(pos1 < pos2 for pos1, pos2 in zip(inputNumbers, inputNumbers[1:])):
            return True
        if all(pos1 > pos2 for pos1, pos2 in zip(inputNumbers, inputNumbers[1:])):
            return True
        
        return False
    
    def AttemptAnswerAgain(self, line: str) -> bool:
        nums = list(map(int, line.split(' ')))

        return self.AttemptAnswer(nums)

    #dropping single values to numerate, check all sub-lists
    def AttemptAnswerYetAgain(self, line: str) -> bool:
        nums = list(map(int, line.split(' ')))

        if (self.AttemptAnswer(nums)):
            return True
        for i in range(len(nums)):
            if self.AttemptAnswer(nums[:i] + nums[i + 1:]):
                return True
            
        return False

def main():
    attempter = AdventOfCode()
    data = open('input.txt').read().strip()
    inputLines = data.split('\n')

    #print(attempter.AttemptAnswer(inputLines))
    part1Results = [line for line in inputLines if attempter.AttemptAnswerAgain(line)]
    print(len(part1Results))

    part2Results = [line for line in inputLines if attempter.AttemptAnswerYetAgain(line)]
    print(len(part2Results))

if "__main__":
    main()