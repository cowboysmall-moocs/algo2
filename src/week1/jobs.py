import sys


def construct_jobs(file_path):
    with open(file_path) as file:
        total = int(file.readline())
        jobs = []
        for line in file:
            elements = line.split()
            weight   = int(elements[0])
            length   = int(elements[1])
            jobs.append((weight - length, float(weight) / float(length), weight, length))
    return (total, jobs)


def main(argv):
    total, jobs = construct_jobs(argv[0])


    jobs1 = sorted(jobs, key = lambda element: (element[0], element[2]), reverse = True)

    completion = 0
    weighted   = 0
    for job in jobs1:
        completion += job[3]
        weighted   += completion * job[2]

    print
    print 'for w - l'
    print '              Total Jobs: ', total
    print '   Total Completion Time: ', completion
    print 'Weighted Completion Time: ', weighted


    jobs2 = sorted(jobs, key = lambda element: (element[1]), reverse = True)

    completion = 0
    weighted   = 0
    for job in jobs2:
        completion += job[3]
        weighted   += completion * job[2]

    print
    print 'for w / l'
    print '              Total Jobs: ', total
    print '   Total Completion Time: ', completion
    print 'Weighted Completion Time: ', weighted
    print


if __name__ == "__main__":
    main(sys.argv[1:])

