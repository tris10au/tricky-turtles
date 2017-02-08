import uuid


class Tile:
    numbers = []
    tile_id = 0

    def __init__(self, numbers, tile_id=None):
        self.numbers = numbers
        if tile_id is None:
            self.tile_id = str(uuid.uuid4())
        else:
            self.tile_id = tile_id

    def __repr__(self):
        return "Tile (" + self.tile_id + "): " + repr(self.numbers)

    def all_forms(self):
        x = []
        for i in range(4):
            j = self.numbers.pop(0)
            self.numbers.append(j)
            x.append(Tile(list(self.numbers), str(self.tile_id)))
        return x


class Board:
    def __init__(self, tiles=[], valid_tiles=[], v=True):
        self.tiles = tiles
        self.valid_tiles = set(valid_tiles)
        if v and len(self.valid_tiles) + len(self.tiles) != 36:
            raise Exception("Not enough tiles")

    def add(self, tile):
        self.tiles.append(tile)

    def options(self):
        opt = []
        for t in self.valid_tiles:
            x = set(self.valid_tiles)
            x.remove(t)
            opt.append(Board(self.tiles + [t], x))
        return opt

    def validate(self):
        s = set([t.tile_id for t in self.tiles])
        l = len(self.tiles)
        if len(s) < l or l > 9:
            # print "non unique tiles"
            return False

        for i in range(l):
            if i in (0, 1, 3, 4, 6, 7) and i + 1 < l and self.tiles[i].numbers[2] + self.tiles[i + 1].numbers[0] != 7:
                # print "left validate fail"
                # print "\t", self.tiles[i], self.tiles[i + 1]
                return False
            if i < 6 and i + 3 < l and self.tiles[i].numbers[3] + self.tiles[i + 3].numbers[1] != 7:
                # print "down validate fail"
                # print "\t", self.tiles[i], self.tiles[i + 3]
                return False
        return True

    def __repr__(self):
        return "Board (" + str(len(self.tiles)) + "): " + repr(self.tiles)