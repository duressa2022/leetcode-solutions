class FrequencyTracker:

    def __init__(self):
        self.number_freq={}
        self.freq_freq={}


    def add(self, number: int) -> None:
        if number not in self.number_freq:
            self.number_freq[number]=1
            if self.number_freq[number] not in  self.freq_freq:
                self.freq_freq[self.number_freq[number]]=1
            else:
                self.freq_freq[self.number_freq[number]]+=1
        else:
            prev_freq=self.number_freq[number]
            self.number_freq[number]+=1
            self.freq_freq[prev_freq]-=1
            if self.freq_freq[prev_freq]==0:
                del self.freq_freq[prev_freq]
            if prev_freq+1 not in  self.freq_freq:
                self.freq_freq[prev_freq+1]=1
            else:
                self.freq_freq[prev_freq+1]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.number_freq:
            prev_freq=self.number_freq[number]
            self.number_freq[number]-=1
            if self.number_freq[number]==0:
                del self.number_freq[number]
            if prev_freq in self.freq_freq:
                self.freq_freq[prev_freq]-=1
                if self.freq_freq[prev_freq]==0:
                    del self.freq_freq[prev_freq]
                if number in self.number_freq and self.number_freq[number] not in self.freq_freq:
                    self.freq_freq[self.number_freq[number]]=1
                else:
                    if number in self.number_freq:
                        self.freq_freq[self.number_freq[number]]+=1
    def hasFrequency(self, frequency: int) -> bool:
        return True if frequency in self.freq_freq else False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)