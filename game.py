from pyspark import SparkContext, SparkConf, StorageLevel
from turtles import Tile, Board


MAX_PARALLEL = 24 * 2


if __name__ == "__main__":
    conf = SparkConf().setAppName("game")
    sc = SparkContext(conf=conf)
    tiles = []
    tiles.append(Tile([0, 1, 5, 4]))
    tiles.append(Tile([0, 4, 6, 2]))
    tiles.append(Tile([0, 5, 6, 2]))

    tiles.append(Tile([0, 2, 4, 6]))
    tiles.append(Tile([0, 5, 6, 3]))
    tiles.append(Tile([0, 5, 6, 3]))

    tiles.append(Tile([1, 3, 5, 7]))
    tiles.append(Tile([1, 4, 7, 2]))
    tiles.append(Tile([1, 4, 7, 3]))

    tiles = sc.parallelize(tiles, MAX_PARALLEL).flatMap(lambda t: t.all_forms()).collect()
    boards = []
    for i in range(len(tiles)):
        j = tiles[:i] + tiles[i + 1:]
        boards.append(Board([tiles[i]], j))
    boards = sc.parallelize(boards, MAX_PARALLEL)

    for i in range(8):
        boards = boards.flatMap(lambda b: b.options()).filter(lambda b: b.validate()).repartition(MAX_PARALLEL)
        boards.persist(StorageLevel.MEMORY_AND_DISK)

        c = boards.count()
        f = boards.first()
        print "At stage", i, "have", c, "valid boards"
        print "Example: ", f
    print "!! ANSWERS"
    print "=========="
    answers = boards.collect()
    for answer in answers:
        print answer
    print "Answers: ", len(answers)
