import random as rand
import string
import math

class Ch:
    speed: int
    helth: int
    damage: int
    pts: int
    name: str
    fightes: list

    def __init__(self):
        self.speed = rand.randint(1, 10)
        self.helth = rand.randint(1, 10)
        self.damage = rand.randint(1, 10)
        self.pts = 100
        self.name = ''.join(rand.choices(string.ascii_uppercase, k = 3))
        self.fightes = []

    def getStrengs(self):
        strengs = int(self.speed * 5
                      * self.damage * 4
                      * self.helth * 3/60
                      * (rand.uniform(0.85, 1.15)))
        return strengs

    def setPts(self, pts: int):
        self.pts = pts
        self.fightes.append(pts)

    def getPts(self):
        return self.pts

    def stats(self):
        return f"{self.name} fights: {self.fightes}\n" \
               f"speed {self.speed} helth {self.helth} damage {self.damage} - [{self.getStrengs()}]"

    def __str__(self):
        return f"{self.name}[{self.getPts()}] speed {self.speed} helth {self.helth} damage {self.damage}"

def findNearestCh(arr: list):
    firstindex = rand.randint(0,len(arr)-1)
    first = arr[firstindex]
    firstPts = first.getPts()
    dist = 1000000
    for i in range(len(arr)):
        if i != firstindex:
            if (abs(arr[i].getPts()-firstPts)<dist):
                second = arr[i]
                dist = abs(firstPts-second.getPts())
    return first, second

def calculate_new_ratings(strengsA,strengsB,R_A, R_B, K=40):
    if (strengsA > strengsB):
        print("A win")
        result = 1
    elif (strengsA < strengsB):
        print("B win")
        result = 0
    else:
        print("draw")
        result = 0.5
    E_A = 1 / (1 + 10**((R_B - R_A) / 400))
    E_B = 1 / (1 + 10**((R_A - R_B) / 400))
    S_A = result  # 1 for win, 0.5 for draw, 0 for loss
    S_B = 1 - result  # S_B is complementary to S_A

    R_A_new = R_A + K * (S_A - E_A)
    R_B_new = R_B + K * (S_B - E_B)

    if R_A_new < 10:
        R_A_new = 10
    if R_B_new < 10:
        R_B_new = 10

    return R_A_new, R_B_new
def main():
    arr = []
    for i in range(10):
        arr.append(Ch())

    for i in range(260):
        a, b = findNearestCh(arr)
        print(f"Fight {i}")
        print(a)
        print(b)
        strengsA = a.getStrengs()
        strengsB = b.getStrengs()
        print(strengsA,strengsB)
        ptsA = a.getPts()
        ptsB = b.getPts()
        R_A_new, R_B_new = calculate_new_ratings(strengsA, strengsB,ptsA,ptsB)

        print(R_A_new,R_B_new, "\n")
        a.setPts(int(R_A_new))
        b.setPts(int(R_B_new))

    for c in arr:
        print(c.stats())

if __name__ == '__main__':
    main()