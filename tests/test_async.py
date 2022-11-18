class Taffy(object):
    def __init__(self, index, cnt):
        self.name = f"taffy{index}"
        self.cnt = cnt

    async def rsq(self):
        while self.cnt > 0:
            print(f"{self.cnt}")
            self.cnt -= 1


taffy = Taffy(1, 10)
taffy.rsq()