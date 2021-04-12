class Permutations:
    def __init__(self, string):
        self._in = string
        self._out = ""
        self.used = [False] * len(string)

    def permute(self):
        if len(self._out) == len(self._in):
            print(self._out)
            return

        for i in range(len(self._in)):
            if self.used[i]:
                continue

            self._out += self._in[i]
            self.used[i] = True
            self.permute()
            self.used[i] = False
            self._out = self._out[:-1]


Permutations("abcde").permute()
