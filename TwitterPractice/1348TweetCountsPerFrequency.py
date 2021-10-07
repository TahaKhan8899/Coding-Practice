from typing import DefaultDict, List, final


class TweetCounts:

    def __init__(self):
        # maps time (seconds) to a list of tweets
        self.tweetTimeMap = DefaultDict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:

        if (tweetName in self.tweetTimeMap):
            self.tweetTimeMap[tweetName].append(time)
        else:
            self.tweetTimeMap[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:

        # 1 - partition the start -> end times into time chunks

        if (freq == "minute"):
            inc = 59
        elif (freq == "hour"):
            inc = 3599
        if (freq == "day"):
            inc = 86399

        allChunks = []

        chunkStart = startTime
        chunkEnd = chunkStart + inc

        while(chunkStart <= endTime and chunkEnd <= endTime):
            print(allChunks)
            chunk = [chunkStart, chunkEnd]
            allChunks.append(chunk)
            chunkStart = chunkEnd + 1
            chunkEnd = chunkStart + inc

        if (chunkStart <= endTime):
            finalChunk = [chunkStart, endTime]
            allChunks.append(finalChunk)

        print(allChunks)

        res = []

        for chunk in allChunks:
            chunkStart = chunk[0]
            chunkEnd = chunk[1]

            wordCount = 0

            for time in self.tweetTimeMap[tweetName]:
                if time >= chunkStart and time <= chunkEnd:
                    wordCount += 1

            res.append(wordCount)
        return res

        # Your TweetCounts object will be instantiated and called as such:
        # obj = TweetCounts()
        # obj.recordTweet(tweetName,time)
        # param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
