class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        openroom = [False] * len(rooms)
        keys = [0]
        while keys:
            key = keys.pop()
            if not openroom[key]: 
                openroom[key] = True
                keys = keys + rooms[key]
        
        if openroom == [True] * len(rooms):
            return True
        else:
            return False
