import platform
import statistics
import time

ITERATIONS = 200_000

def workload():
    # Deterministic CPU workload used only to verify that the benchmark
    # executes consistently across architectures.
    value = 0
    for i in range(100):
        value = (value + i * 17) % 1_000_003
    return value

def main():
    samples = []

    print("=" * 64)
    print("EdgeVoice Arm64 Benchmark")
    print("=" * 64)
    print("Platform:", platform.platform())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor() or "unknown")
    print("Python:", platform.python_version())
    print("Iterations:", ITERATIONS)
    print()

    for _ in range(10):
        start = time.perf_counter()
        for _ in range(ITERATIONS // 10):
            workload()
        elapsed = time.perf_counter() - start
        samples.append(elapsed)

    median_seconds = statistics.median(samples)
    operations_per_second = ITERATIONS / median_seconds

    print(f"Median benchmark time: {median_seconds:.6f} s")
    print(f"Workload throughput:   {operations_per_second:,.0f} ops/s")
    print()
    print("NOTE:")
    print("These are CPU workload measurements, not LLM inference results.")
    print("Use a real quantized model benchmark for the final hackathon claim.")

if __name__ == "__main__":
    main()
