class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

    def __lt__(self, other):
        return self.end < other.end

    def __str__(self):
        return f"{self.end} - {self.start}"


class maxMeeting:
    def __init__(self, first, last, n):
        self.n = n
        self.meets = self.makeMeeting(first, last)

    def makeMeeting(self, first, last):
        meets = []
        for i in range(self.n):
            meets.append(meeting(first[i], last[i], i + 1))
        return meets

    def solve(self):
        self.meets.sort()
        time_limit = self.meets[0].end
        m = [self.meets[0].pos]
        for i in range(1, self.n):
            if self.meets[i].start >= time_limit:
                m.append(self.meets[i].pos)
                time_limit = self.meets[i].end
        print(*m)


def main():
    s = [1, 3, 0, 5, 8, 5]
    e = [2, 4, 6, 7, 9, 9]
    m = maxMeeting(s, e, len(s))
    m.solve()


if __name__ == "__main__":
    main()
