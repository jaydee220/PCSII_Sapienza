from collections import namedtuple
if __name__ == "__main__":
    num_stdnts = int(input())
    stdnts = namedtuple("stdnts", input())
    gradelst= []
    for _ in range(num_stdnts):
        gradelst += (float(stdnt.MARKS) for stdnt in [stdnts(*input().split())])
    print ("{0:.2f}".format(sum(gradelst)/float(num_stdnts)))