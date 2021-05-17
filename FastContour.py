import cv2
# 1-^ 2-> 3-. 4-<

#   00  01  02
#   10  11  12
#   20  21  22
def getCurrentDirection(currentPoint, previousPoint):
    i, j = currentPoint
    i1, j1 = previousPoint
    if (i - i1 == 1) and (j - j1 == 0):
        return 3
    elif (i - i1 == 0) and (j - j1 == -1):
        return 4
    elif (i - i1 == -1) and (j - j1 == 0):
        return 1
    elif (i - i1 == 0) and (j - j1 == 1):
        return 2

def caseDirection1(img, currentPoint, stage):
    i, j = currentPoint
    if stage == 1:
        i1 = i+1
        j1 = j-1
        n1 = img[i1][j1]
        if (n1 != 0):
            return (i1, j1), 3, 0

        i2 = i
        j2 = j-1
        n2 = img[i2][j2]
        if (n2 != 0):
            return (i2, j2), 4, 0

    i3 = i-1
    j3 = j-1
    n3 = img[i3][j3]
    if (n3 != 0):
        return (i3, j3), 1, 1

    i4 = i-1
    j4 = j
    n4 = img[i4][j4]
    if (n4 != 0):
        return (i4, j4), 2, 1

    return (i,j), 3, 1

#test case 1
# img = [[0,0,0,0,0],
#        [0,1,1,0,0],
#        [0,0,1,0,0],
#        [0,1,0,0,0],
#        [0,0,0,0,0]]
#
# print(caseDirection1(img, (1,2), 1))

#   00  01  02
#   10  11  12
#   20  21  22
def caseDirection2(img, currentPoint, stage):
    i, j = currentPoint
    if stage == 1:
        i1 = i - 1
        j1 = j - 1
        n1 = img[i1][j1]
        if (n1 != 0):
            return (i1, j1), 4, 0

        i2 = i-1
        j2 = j
        n2 = img[i2][j2]
        if (n2 != 0):
            return (i2, j2), 1, 0

    i3 = i - 1
    j3 = j + 1
    n3 = img[i3][j3]
    if (n3 != 0):
        return (i3, j3), 2, 1

    i4 = i
    j4 = j + 1
    n4 = img[i4][j4]
    if (n4 != 0):
        return (i4, j4), 3, 1

    return (i, j), 4, 1

# img = [[0,0,0,0,0],
#        [0,0,1,0,0],
#        [0,0,1,0,0],
#        [0,1,0,0,0],
#        [0,0,0,0,0]]
#
# print(caseDirection2(img, (2,2), 1))

#   00  01  02
#   10  11  12
#   20  21  22
def caseDirection3(img, currentPoint, stage):
    i, j = currentPoint
    if stage == 1:
        i1 = i - 1
        j1 = j + 1
        n1 = img[i1][j1]
        if (n1 != 0):
            return (i1, j1), 1, 0

        i2 = i
        j2 = j+1
        n2 = img[i2][j2]
        if (n2 != 0):
            return (i2, j2), 2, 0

    i3 = i + 1
    j3 = j + 1
    n3 = img[i3][j3]
    if (n3 != 0):
        return (i3, j3), 3, 1

    i4 = i+1
    j4 = j
    n4 = img[i4][j4]
    if (n4 != 0):
        return (i4, j4), 4, 1

    return (i, j), 1, 1

#   00  01  02
#   10  11  12
#   20  21  22
def caseDirection4(img, currentPoint, stage):
    i, j = currentPoint
    if stage == 1:
        i1 = i + 1
        j1 = j + 1
        n1 = img[i1][j1]
        if (n1 != 0):
            return (i1, j1), 2, 0

        i2 = i+1
        j2 = j
        n2 = img[i2][j2]
        if (n2 != 0):
            return (i2, j2), 3, 0

    i3 = i + 1
    j3 = j - 1
    n3 = img[i3][j3]
    if (n3 != 0):
        return (i3, j3), 4, 1

    i4 = i
    j4 = j - 1
    n4 = img[i4][j4]
    if (n4 != 0):
        return (i4, j4), 1, 1

    return (i, j), 2, 1

# 1-^ 2-> 3-. 4-<
def traceContour(img, initialCurrentPoint, initialPreviousPoint, NBD):
    initalDirection = getCurrentDirection(initialCurrentPoint, initialPreviousPoint)
    contour = []
    if(initalDirection == 1):
        currentPoint, direction, stage = caseDirection1(img, initialCurrentPoint, 1)
    elif(initalDirection == 2):
        currentPoint, direction, stage = caseDirection2(img, initialCurrentPoint, 1)
    elif (initalDirection == 3):
        currentPoint, direction, stage = caseDirection3(img, initialCurrentPoint, 1)
    elif (initalDirection == 4):
        currentPoint, direction, stage = caseDirection4(img, initialCurrentPoint, 1)

    while(not (currentPoint == initialCurrentPoint and direction == initalDirection)):
        contour.append(currentPoint)
        i, j = currentPoint
        if img[i][j + 1] == 0:
            img[i][j] = -NBD
        if img[i][j + 1] != 0 and img[i][j] == 1:
            img[i][j] = NBD
        if (direction == 1):
            currentPoint, direction, stage = caseDirection1(img, currentPoint, stage)
        elif (direction == 2):
            currentPoint, direction, stage = caseDirection2(img, currentPoint, stage)
        elif (direction == 3):
            currentPoint, direction, stage = caseDirection3(img, currentPoint, stage)
        elif (direction == 4):
            currentPoint, direction, stage = caseDirection4(img, currentPoint, stage)

    return (img, contour)

def travelClockwise(currentPoint, turnPoint):
    i, j = currentPoint
    i1, j1 = turnPoint
    if (i - i1 == 1) and (j - j1 == 1):
        return (i1, j1 + 1)
    elif (i - i1 == 1) and (j - j1 == 0):
        return (i1, j1 + 1)
    elif (i - i1 == 1) and (j - j1 == -1):
        return (i1 +1, j1)
    elif (i - i1 == 0) and (j - j1 == -1):
        return (i1 + 1, j1)
    elif (i - i1 == -1) and (j - j1 == -1):
        return (i1, j1 - 1)
    elif (i - i1 == -1) and (j - j1 == 0):
        return (i1, j1 - 1)
    elif (i - i1 == -1) and (j - j1 == 1):
        return (i1 - 1, j1)
    elif (i - i1 == 0) and (j - j1 == 1):
        return (i1 - 1, j1)

def findContours(img):
    rows = len(img)
    cols = len(img[0])
    LNBD = 1
    NBD = 1
    contours = []


    for i in range(1, rows - 1):
        LNBD = 1
        for j in range(1, cols - 1):
            # Step 1
            if (img[i][j] == 1 and img[i][j - 1] == 0):
                NBD += 1
                contourType = 1
                i2 = i
                j2 = j - 1

            elif (img[i][j] >= 1 and img[i][j+1] == 0):
                NBD += 1
                contourType = 2
                i2 = i
                j2 = j + 1
                if img[i][j] > 1:
                    LNBD = img[i][j]
                    break

            else:
                contourType = 0

            # # step 2
            # if (contourType != 0):

            if (contourType != 0):
                img, contour = traceContour(img, (i, j), (i2, j2), NBD)
                contours.append(contour)

            # step 4
            if img[i][j] != 1:
                LNBD = abs(img[i][j])

    return contours


# i = [[0,0,0,0,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,1,0,1,0,0],
#        [0,1,1,1,1,1,0],
#        [0,0,0,0,0,0,0]]
#
# contours = findContours(i)
# for line in i:
#     print (line)
f = open("sample.txt", "w")

img = cv2.imread("sample.png")
i = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for x in range(0, len(i)):
    for y in range(0, len(i[x])):
        if (i[x][y] != 0):
            i[x][y] = 1

print("done convert")

contours = findContours(i)
print(len(contours))

s = [[str(e) for e in row] for row in i]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ('\n'.join(table))

f.write('\n'.join(table))

f.close()