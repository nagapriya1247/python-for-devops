# Simple DevOps examples using assignment operators

# 1) Retry counter (+=)
retries = 0
retries += 1      # schedule another retry -> retries = 1
print("retries:", retries)

# 2) Decrease available worker slots (-=)
slots = 10
slots -= 2        # two workers started -> slots = 8
print("slots left:", slots)

# 3) Accumulate bytes downloaded (+=)
total_bytes = 0
chunk = 4096
total_bytes += chunk   # add downloaded chunk
print("total_bytes:", total_bytes)

# 4) Running average of CPU samples (+= and /=)
count = 0
cpu_total = 0.0
cpu_sample = 30.0
cpu_total += cpu_sample   # add new sample
count += 1
avg_cpu = cpu_total / count
print("avg_cpu:", avg_cpu)

# 5) Compute number of chunks (// and math-free ceil trick)
filesize = 10245
chunk_size = 1000
chunks = (filesize + chunk_size - 1) // chunk_size
print("chunks needed:", chunks)

# 6) Exponential backoff doubling (*=)
backoff = 1
backoff *= 2     # double delay -> backoff = 2
backoff *= 2     # double again -> backoff = 4
print("backoff seconds:", backoff)

# 7) Round-robin index using modulus (%=)
index = 0
index += 1
index %= 3       # keep index in range 0..2 for 3 servers -> DevOps use: assign tasks in round-robin to servers/workers without exceeding the server count.
print("round-robin index:", index)

if __name__ == "__main__":
    pass
