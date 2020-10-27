class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def tileset(tiles:str)-> set:
            if len(tiles) == 0:
                return set([""])
            t = set([])
            s = tileset(tiles[1:])
            for item in s:   
                for i in range(len(item) + 1):
                    t.add(item[:i] + tiles[0] + item[i:])
            t.update(s)
            return t
        
        return len(tileset(tiles)) - 1