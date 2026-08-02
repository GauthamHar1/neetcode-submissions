class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use a stack to keep track of the days waiting for a warmer day
        waiting = []
        result = [0] * len(temperatures)
        for day in enumerate(temperatures):
            if not waiting:
                waiting.append(day)
                continue
            else:
                # we want to pop all the days for which this new day is warmer
                if day[1]<=waiting[-1][1]:
                    waiting.append(day)
                else:
                    while waiting and day[1]>waiting[-1][1]:
                        elem = waiting.pop()
                        result[elem[0]] = day[0]-elem[0]
                    else:
                        waiting.append(day)
                # if the new day is actually less than the top of waiting
                # then we just append it
        return result
                    
            

                
            