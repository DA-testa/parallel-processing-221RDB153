# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    heap =[(0, i) for i in range(n)]
    heap.heapify(heap)
    for i in range(m):
        job_time = data[i]
        thread_time, thread_index = heapq.heappop(heap)
        output.append((thread_index, thread_time))
        thread_time += job_time
        heapq.heappush(heap,(thread_time, thread_index))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
