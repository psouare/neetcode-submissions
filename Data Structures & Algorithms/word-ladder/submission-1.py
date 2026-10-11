class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L=len(beginWord)
        word=set(wordList)
        bucket=defaultdict(list)

        for w in word:
            for i in range(L):
                pattern=w[:i] +"*"+w[i+1:]
                bucket[pattern].append(w)
        

        q=deque([(beginWord,1)])
        visit=set([beginWord])

        while q:
            word,steps=q.popleft()
            for i in range(L):
                patt=word[:i] +"*"+word[i+1:]
                for nxt in bucket[patt]:
                    
                    if nxt==endWord:
                        return steps+1
                    if nxt in visit:
                        continue
                    q.append((nxt,steps+1))
                    visit.add(nxt)
                bucket[patt]=[]

        return 0

        

            

