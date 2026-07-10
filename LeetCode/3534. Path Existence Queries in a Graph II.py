return (1 << j) + minJumps(jump[start][j], end, j)
def minDist(u: int, v: int) -> int:
uIndex = indexMap[u]
vIndex = indexMap[v]
start = min(uIndex, vIndex)
end = max(uIndex, vIndex)
res = minJumps(start, end, maxLevel - 1)
return res if res < math.inf else -1
return [minDist(u, v) for u, v in queries]