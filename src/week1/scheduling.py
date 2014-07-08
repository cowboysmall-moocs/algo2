import sys


def main(argv):
    with open(argv[0]) as file:
        total = int(file.readline())
        jobs1 = []
        jobs2 = []
        for line in file:
            elements = line.split()
            weight   = int(elements[0])
            length   = int(elements[1])
            jobs1.append((weight - length, weight, length))
            jobs2.append((float(weight) / float(length), weight, length))


    jobs1 = sorted(jobs1, key = lambda element: (element[0], element[1]), reverse = True)

    completion = 0
    weighted   = 0
    for job in jobs1:
        completion += job[2]
        weighted   += completion * job[1]

    print 'for w - l'
    print '              Total Jobs: ', total
    print '   Total Completion Time: ', completion
    print 'Weighted Completion Time: ', weighted


    jobs2 = sorted(jobs2, key = lambda element: (element[0]), reverse = True)

    completion = 0
    weighted   = 0
    for job in jobs2:
        completion += job[2]
        weighted   += completion * job[1]

    print 'for w / l'
    print '              Total Jobs: ', total
    print '   Total Completion Time: ', completion
    print 'Weighted Completion Time: ', weighted


if __name__ == "__main__":
    main(sys.argv[1:])

