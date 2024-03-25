import time

iterations = 10
total_write_time = 0
total_read_time = 0
for _ in range(iterations):
    start_time = time.time()
    with open("test_file.txt", "w") as file:
        for _ in range(1_000_000):
            file.write("Some sample text.\n")
    write_end_time = time.time()
    total_write_time += (write_end_time - start_time)

    with open("test_file.txt", "r") as file:
        content = file.readlines()
    read_end_time = time.time()
    total_read_time += (read_end_time - write_end_time)

average_write_time = total_write_time / iterations
average_read_time = total_read_time / iterations
print(f"Average time taken to write: {average_write_time} seconds")
print(f"Average time taken to read: {average_read_time} seconds")
