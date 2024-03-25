import tracemalloc

tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

my_list = [x for x in range(1_000_000)]
snapshot2 = tracemalloc.take_snapshot()

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)