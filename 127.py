class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = len(beginWord)
        def countDiffChar(target, item):
            ans = 0
            for i in range(l):
                if target[i] != item[i]:
                    ans += 1
                if ans > 1:
                    break
            return ans

        isEnd = False
        visited = [0]*len(wordList)
        optionList = []
        for i,n in enumerate(wordList):
            if n == endWord:
                isEnd = True
            if countDiffChar(beginWord, n)==1:
                optionList.append((n,2))
                visited[i] = 1

        if not isEnd:
            return 0   # endWord 不在字典中，所以无法进行转换。

        lWordList = len(wordList)
        while optionList:
            word, ans = optionList.pop(0)
            if word == endWord:
                return ans
            for i in range(lWordList):
                if visited[i]==0:

                    if countDiffChar(word, wordList[i])==1:
                        optionList.append((wordList[i], ans+1))
                        visited[i] = 1        

        return 0
