def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    result = []
    last_finish_time = 0

    for job in jobs:
        if job[0] >= last_finish_time:
            result.append(job)
            last_finish_time = job[1]

    return result

# Example usage:
jobs = [(1, 3), (2, 5), (3, 8), (4, 6)]
scheduled_jobs = job_scheduling(jobs)

print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job {job[0]} starts at {job[1]}")
