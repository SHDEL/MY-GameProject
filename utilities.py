class Utilities:

    @staticmethod
    def getPoint(card: str) -> int:
        # case 10
        if len(card) == 3:
            return 0

        # get only first char
        val: str = card[:-1]
        if val == "A":
            return 1
        if val == "J" or val == "Q" or val == "K":
            return 0
        return int(val)

    @staticmethod
    def getTotalPointInPokdeng(prevTotalPoint: int) -> int:
        if prevTotalPoint >= 10:
            return prevTotalPoint - 10
        return prevTotalPoint
