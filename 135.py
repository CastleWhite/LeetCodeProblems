class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 思路1：遍历max（ans）次，每次加一，直到满足条件
        # 思路2：每次访问一部分，即评分最小的
        l = len(ratings)
        ans = [0]
        anss = 0
        # c = Counter(ratings)
        # c = sorted(c.keys())
        # for i in c:
        #     for j in range(l):
        #         if ratings[j] == i:
        #             tmp = []
        #             if j-1>=0 and ratings[j-1]<i:
        #                 tmp.append(ans[j-1])
        #             if j+1<l and ratings[j+1]<i:
        #                 tmp.append(ans[j+1])
        #             if tmp:
        #                 ans[j] = max(tmp)+1
        
        # return sum(ans)
        # 都是O（n^2) ，都会超时------------------------------------------------------
        flag = 0
        top = [[0]]
        for i in range(1,l):
            if ratings[i]==ratings[i-1]:
                top[-1].append(i-1)
                top.append([i])
                flag = 0
            elif ratings[i]>ratings[i-1] and flag<0:
                top[-1].append(i-1)
                flag = 1
            elif ratings[i]<ratings[i-1] and flag>0:
                top[-1].append(i-1)
                flag = -1
            elif flag == 0:
                flag = ratings[i]-ratings[i-1]
        if l-1 not in top[-1]:
            top[-1].append(l-1)

        for stage in top:
            # print(stage)
            if len(stage) == 1:
                ans.append(1)
                continue
            begin = ratings[stage[0]+1] - ratings[stage[0]]
            ll = len(stage)
            if begin > 0:
                anss += 1
                for i in range(1,ll,2):
                    anss -= 1

                    a = stage[i]-stage[i-1]
                    if i+1 < ll:
                        b = stage[i+1]-stage[i]
                        if a < b:
                            ans.append(a)
                            ans.append(b+1)
                        else:
                            ans.append(a+1)
                            ans.append(b)
                    else:
                        ans.append(a+1)
            else:
                ans.append(stage[1]-stage[0]+1)
                for i in range(2,ll,2):
                    anss -= 1
                    a = stage[i]-stage[i-1]
                    if i+1 < ll:
                        b = stage[i+1]-stage[i]
                        if a < b:
                            ans.append(a)
                            ans.append(b+1)
                        else:
                            ans.append(a+1)
                            ans.append(b)
                    else:
                        ans.append(a+1)

        # print(ans)
        for i in ans:
            anss += (1+i)*i//2
        return anss


