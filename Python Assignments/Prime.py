import threading

class PrimeThread(threading.Thread):
    def __init__(self, start, end):
        threading.Thread.__init__(self)
        self.start = start
        self.end = end

    def run(self):
        count = 0
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    count += 1
        print("Count of prime numbers between", self.start, "and", self.end, "is", count)

threads = []
total_count = 0

for i in range(1, 201, 100):
    thread = PrimeThread(i, i + 99)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    total_count += thread.count

    print("Total count of prime numbers is", total_count)
