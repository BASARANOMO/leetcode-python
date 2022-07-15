class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stk and stk[-1] > 0:
                alive = stk[-1] < -asteroid
                if stk[-1] <= -asteroid:
                    stk.pop()
            if alive:
                stk.append(asteroid)
        return stk
