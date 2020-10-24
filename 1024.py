class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # dp 返回【0-T】所需的最少片段
        # 0,2  4,6 这种咋办？
        #先处理？ 排序
        clips.sort()
        reco = [102]*T
        for clip in clips:
            if clip[1] > T:
                clip[1] = T
            if clip[0] == 0:
                for i in range(clip[1]):
                    reco[i] = 1
            else:
                head = clip[0]-1
                for i in range(clip[0], clip[1]):

                    minpre = min(reco[head:i])
                    reco[i] = min(minpre+1, reco[i])
        
        if reco[-1] == 102:
            reco[-1] = -1
        return reco[-1]
