__author__ = "Daniel J. Lewis"
__credits__ = "Drew Dara-Abrams, Francesco de Virgilio"
__license__ = "unknown"


# The following code has been published on GitHub Gists by Drew Dara-Abrams:
# http://gist.github.com/drewda/1299198 and it comes from Daniel J. Lewis:
# http://danieljlewis.org/files/2010/06/Jenks.pdf described at
# http://danieljlewis.org/2010/06/07/jenks-natural-breaks-algorithm-in-python/

def get_jenks_breaks(datalist, numclass):
    datalist.sort()
    mat1 = []
    for i in range(0, len(datalist)+1):
        temp = []
        for j in range(0, numclass+1):
            temp.append(0)
        mat1.append(temp)
    mat2 = []
    for i in range(0, len(datalist)+1):
        temp = []
        for j in range(0, numclass+1):
            temp.append(0)
        mat2.append(temp)
    for i in range(1, numclass+1):
        mat1[1][i] = 1
        mat2[1][i] = 0
        for j in range(2, len(datalist)+1):
            mat2[j][i] = float('inf')
    v = 0.0
    for l in range(2, len(datalist)+1):
        s1 = 0.0
        s2 = 0.0
        w = 0.0
        for m in range(1, l + 1):
            i3 = l - m + 1
            val = float(datalist[i3-1])
            s2 += val * val
            s1 += val
            w += 1
            v = s2 - (s1 * s1) / w
            i4 = i3 - 1
            if i4 != 0:
                for j in range(2, numclass+1):
                    if mat2[l][j] >= (v + mat2[i4][j - 1]):
                        mat1[l][j] = i3
                        mat2[l][j] = v + mat2[i4][j - 1]
        mat1[l][1] = 1
        mat2[l][1] = v
    k = len(datalist)
    kclass = []
    for i in range(0, numclass+1):
        kclass.append(0)
    kclass[numclass] = float(datalist[len(datalist) - 1])
    countnum = numclass
    while countnum >= 2:  # print "rank = " + str(mat1[k][countNum])
        nid = int((mat1[k][countnum]) - 2)
        #print "val = " + str(dataList[id])
        kclass[countnum - 1] = datalist[nid]
        k = int((mat1[k][countnum] - 1))
        countnum -= 1
    return kclass


# written by Drew Dara-Abrams:
# used after running getJenksBreaks()
def classify(value, breaks):
    for i in range(1, len(breaks)):
        if value < breaks[i]:
            return i
    return len(breaks)
    # Francesco de Virgilio: the original functions had `return len(breaks)-1`,
    # but it returned the same class for the last two values in the list, even
    # if they were _really_ different (e.g. 306 and 4008).