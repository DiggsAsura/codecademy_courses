import time
start_time = time.time()

j = 5
for i in range(5000000):
    print(f"Python:", i * j)
    j += 1

print("--- %s seconds ---" % (time.time() - start_time))
