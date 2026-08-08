class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # car will join a fleet if it has less time than the one in front
        # time of each fleet only increases

        fleets = deque()

        # sort positions decending: closest to target first
        cars = sorted(zip(position, speed), reverse=True)

        # calculate time
        #   time = (target - position)/speed
        # for each car join fleet if fleet time on stack is greater than cars time
        
        for pos, spd in cars:
            time = (target - pos)/spd # after we sort position[i] and speed[i] are not the same car
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        # return len stack
        return len(fleets)
