class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people

        people.sort()
        l = len(people)
        max = people[-1][0]

        equ = [0]*l
        tmp = people[0][0]
        tmp_count = 0
        for i,p in enumerate(people):
            if p[0] == tmp:
                tmp_count += 1
            else:
                tmp = p[0]
                tmp_count = 1
            equ[i] = tmp_count - 1

        for i in range(l-2,-1,-1):
            if people[i][0] == max:
                continue
            elif people[i][1] == 0:
                continue
            else:
                b = people[i][1] - equ[i]

                people.insert(i+b, people.pop(i))

        return people
