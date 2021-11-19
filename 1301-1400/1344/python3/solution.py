class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(11*minutes/2-30*(hour%12))
        
        #The minute hand moves 6 degrees every minute, while the hour hand moves 1/2 degrees.

        #11/2 is the rate of separation of the hour hand and minute hand per minute.
        
        if (angle < 180.0):
            return angle
        else:
            return 360-angle