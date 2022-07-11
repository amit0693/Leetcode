class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = collections.defaultdict(str)
        for path in paths:
            src = path[0]
            dst = path[1]
            d[src] = dst
        for k, v in d.items():
            if v not in d:
                return v       
        