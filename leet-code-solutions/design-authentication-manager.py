class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token_time_map={}
        self.timeToLive=timeToLive
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_time_map[tokenId]=currentTime+self.timeToLive
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_time_map:
            if self.token_time_map[tokenId]>currentTime:
                self.token_time_map[tokenId]=currentTime+self.timeToLive
    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter=0
        for token in self.token_time_map:
            if self.token_time_map[token]>currentTime:
                counter+=1
        return counter
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)