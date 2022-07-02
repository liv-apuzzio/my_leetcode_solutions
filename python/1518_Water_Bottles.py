class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        while numBottles >= numExchange:
            botexch = numBottles - (numBottles % numExchange)
            botgain = botexch / numExchange
            drank += botgain
            numBottles = numBottles - botexch + botgain
        return int(drank)