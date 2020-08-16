class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColar = image[sr][sc]

        if oldColar==newColor:
            return image
        # 没加这个，导致超时
        
        m = len(image)
        n = len(image[0])
        
        queue = [sr, sc]
        while queue:
            a = queue.pop(0)
            b = queue.pop(0)
            if image[a][b] == oldColar:
                image[a][b] = newColor
                if a != 0:
                    queue.append(a-1)
                    queue.append(b)
                if a != m-1:
                    queue.append(a+1)
                    queue.append(b)
                if b != 0:
                    queue.append(a)
                    queue.append(b-1)
                if b != n-1:
                    queue.append(a)
                    queue.append(b+1)

        return image
