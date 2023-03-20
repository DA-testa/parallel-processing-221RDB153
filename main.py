# python3

def parallel_processing(n, m, data):
    output = []
    jobs =[(data[i], i) for i in range(n)]
    threads = [0]*n
    for job in jobs:
        thread = threads.index(min(threads))
        start_time = threads[thread]
        output.append((thread, start_time))
        threads[thread] += job[0]
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread, time in result:
        print(thread, time)

if __name__ == "__main__":
    main()
