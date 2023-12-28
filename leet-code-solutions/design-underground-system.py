
class UndergroundSystem:
  def __init__(self):
      self.checkIns={}
      self.checkOuts={}
  def checkIn(self, id: int, stationName: str, t: int) -> None:

      self.checkIns[id]=(stationName,t)
  def checkOut(self, id: int, stationName: str, t: int) -> None:

      if id not in self.checkIns:return 
      (starting_station,starting_time)=self.checkIns.pop(id)
      if (starting_station,stationName) not in self.checkOuts:
          self.checkOuts[(starting_station,stationName)]=[0,0]
      self.checkOuts[(starting_station,stationName)][0]+=1
      self.checkOuts[(starting_station,stationName)][1]+=t-starting_time

  def getAverageTime(self, startStation: str, endStation: str) -> float:

      [moving,time]=self.checkOuts[(startStation,endStation)]
      return time/moving


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)