import threading

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Arithematics():
    def worker(self, lb, ub):
        print(list[lb:ub + 1])

    def arithematics(self):

        l = len(list)
        t = 3

        c = int(l / t)

        threads = []
        for i in range(t + 1):
            lb = i * c + 1
            ub = (i + 1) * c
            th = threading.Thread(target=self.worker, args=(lb, ub))
            threads.append(th)
            th.start()

    # if __name__ == "__main__":
    #     self.arithematics()


test = Arithematics()
test.arithematics()