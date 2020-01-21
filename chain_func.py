def add(num):
    class sum(int):
        def __call__(self, num):
            return sum(self + num)

    return sum(num)


print(add(1)(2)(3))
