class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i, j in zip(range(0, len(s)), range(0, len(t))):
            if i not in smap:
                pair1 = {s[i] : i}
                smap.update(pair1)
            if j not in tmap:
                pair2 = {t[j] : j}
                tmap.update(pair2)
        svals = list(smap.values())
        tvals = list(tmap.values())
        return svals == tvals