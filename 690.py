"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        
        d = dict()
        for n,em in enumerate(employees):
            d[em.id] = n
        queue = [id]

        while queue:
            a = d[queue.pop()]
            ans += employees[a].importance
            queue += employees[a].subordinates

        return ans
