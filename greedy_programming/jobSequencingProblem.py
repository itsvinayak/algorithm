class job:
    def __init__(self, job_id, job_deadline, profit):
        self.job_id = job_id
        self.job_deadline = job_deadline
        self.profit = profit

    def __lt__(self, other):
        return self.profit < other.profit


def JobScheduling(job_id, job_deadline, profit):
    jobs = []
    for i in range(len(job_id)):
        jobs.append(job(job_id[i], job_deadline[i], profit[i]))

    jobs.sort(reverse=True)

    ans = [False] * len(job_id)
    for i in jobs:
        if ans[i.job_deadline - 1] is False:
            ans[i.job_deadline - 1] = i.job_id
        else:
            temp = i.job_deadline - 1
            while temp + 1:
                if ans[temp] is False:
                    ans[temp] = i.job_id
                    break
                temp -= 1
    print(" ".join(str(i) for i in ans if i is not False))


def main():
    job_id = ["a", "b", "c", "d", "e"]
    job_deadline = [2, 1, 2, 1, 3]
    profit = [100, 19, 27, 25, 15]
    JobScheduling(job_id, job_deadline, profit)


if __name__ == "__main__":
    main()
