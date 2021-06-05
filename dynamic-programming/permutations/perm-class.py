class Permutation:
    def __init__(self):
        self.perms = []

    def permute(self, arr):
        self.backtrack(arr, [])
        return self.perms

    def backtrack(self, arr, path):
        # Base case.
        if not arr:
            self.perms.append(path)

        for n in range(len(arr)):
            self.backtrack(arr[:n] + arr[n + 1:], path + [arr[n]])


p = Permutation()
print(p.permute(["a", "b", "c"]))
