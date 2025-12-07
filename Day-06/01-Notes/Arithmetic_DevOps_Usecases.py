# Arithmetic operations for DevOps use cases
import math
import time

def disk_percent(total_gb, used_gb):
    """Return used percent (safe if total_gb is 0)."""
    if total_gb == 0:
        return 0.0
    return (used_gb / total_gb) * 100.0

def replicas_needed(load, capacity):
    """Return how many replicas are needed (integer)."""
    if capacity <= 0:
        raise ValueError("capacity must be > 0")
    return math.ceil(load / capacity)

def backoff(base_seconds, attempt, cap_seconds=60):
    """Exponential backoff: base * 2^attempt, capped."""
    return min(cap_seconds, base_seconds * (2 ** attempt))

def run_on_interval(epoch_seconds, interval_minutes=15):
    """Return True if epoch_seconds falls on the interval (e.g., every 15 min)."""
    minute = int(epoch_seconds // 60)  # total minutes since epoch
    return (minute % interval_minutes) == 0

def chunks_needed(total_items, chunk_size):
    """Return number of chunks required to hold total_items."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    return math.ceil(total_items / chunk_size)

def to_hms(seconds):
    """Convert seconds -> (hours, minutes, seconds)."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

# Example usage (print outputs when run)
if __name__ == "__main__":
    now = time.time()
    print("Disk %:", disk_percent(500, 123))
    print("Replicas:", replicas_needed(1234, 200))
    print("Backoff (attempt 3):", backoff(1, 3))
    print("Run now (15m):", run_on_interval(now, 15))
    print("Chunks:", chunks_needed(10245, 1000))
    print("H:M:S:", to_hms(98765))
