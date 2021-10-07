class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        stk = [(sx, sy)]
        while (len(stk) > 0):
            pt = stk.pop()
            startX = pt[0]
            startY = pt[1]
            if (startX > tx or startY > ty):
                return False
            elif (startX == tx and startY == ty):
                return True
            else:
                stk.append((sx, sx + sy))
                stk.append((sx + sy, sy))
