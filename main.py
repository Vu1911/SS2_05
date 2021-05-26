import cv2

#   00  01  02
#   10  11  12
#   20  21  22
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

def travelContourclockwise(currentPoint, turnPoint):
    i, j = currentPoint
    i1, j1 = turnPoint
    if (i - i1 == 1) and (j - j1 == 1):
        return (i1 + 1, j1)
    elif (i - i1 == 1) and (j - j1 == 0):
        return (i1, j1 - 1)
    elif (i - i1 == 1) and (j - j1 == -1):
        return (i1, j1 - 1)
    elif (i - i1 == 0) and (j - j1 == -1):
        return (i1 - 1, j1)
    elif (i - i1 == -1) and (j - j1 == -1):
        return (i1 - 1, j1)
    elif (i - i1 == -1) and (j - j1 == 0):
        return (i1, j1 + 1)
    elif (i - i1 == -1) and (j - j1 == 1):
        return (i1, j1 + 1)
    elif (i - i1 == 0) and (j - j1 == 1):
        return (i1 + 1, j1)

# test travelContourclockwise
# print(travelClockwise((1,1), (1,0)))

def traceContour(img, initialCurrentPoint, initialTurnPoint, NBD, currentPoint, turnPoint):
    i2, j2 = turnPoint
    i3, j3 = currentPoint
    i2, j2 = travelContourclockwise((i3, j3),(i2, j2))
    i4, j4 = (0, 0)
    contour = []
    contour.append(currentPoint)

    while (i4 == 0 and j4 == 0):

        i2, j2 = travelContourclockwise((i3, j3),(i2, j2))
        if img[i2][j2] != 0:
            i4 = i2
            j4 = j2
            break

    if img[i3][j3+1] == 0:
        img[i3][j3] = -NBD
    if img[i3][j3+1] != 0 and img[i3][j3] == 1:
        img[i3][j3] = NBD

    while (i4, j4) != initialCurrentPoint and (i3, j3) != initialTurnPoint:

        i2, j2 = (i3, j3)
        i3, j3 = (i4, j4)
        i2, j2 = travelContourclockwise((i3, j3), (i2, j2))
        i4, j4 = (0, 0)

        contour.append((i3, j3))

        while (i4 == 0 and j4 == 0):
            i2, j2 = travelContourclockwise((i3, j3), (i2, j2))
            if img[i2][j2] != 0:
                i4 = i2
                j4 = j2
                break

        if img[i3][j3 + 1] == 0:
            img[i3][j3] = -NBD
        if img[i3][j3 + 1] != 0 and img[i3][j3] == 1:
            img[i3][j3] = NBD

    return (img, contour)

    # return (i4, j4)

def findContours(img):
    rows = len(img)
    cols = len(img[0])
    LNBD = 1
    NBD = 1
    contours = []

    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    i3 = 0

    for i in range(1, rows - 1):
        LNBD = 1
        for j in range(1, cols - 1):
            # Step 1
            currentPoint = ()
            if (img[i][j] == 1 and img[i][j - 1] == 0):
                NBD += 1
                contourType = 1
                currentPoint = (i,j)
                i2 = i
                j2 = j - 1

            elif (img[i][j] >= 1 and img[i][j+1] == 0):
                NBD += 1
                contourType = 2
                currentPoint = (i,j)
                i2 = i
                j2 = j + 1
                if img[i][j] > 1:
                    LNBD = img[i][j]
                    break

            else:
                contourType = 0

            turnPoint = (i2, j2)

            # # step 2
            # if (contourType != 0):

            if (contourType != 0):
                # step 3
                # step 3.1
                i1 = 0
                j1 = 0
                i1, j1 = travelClockwise(currentPoint, turnPoint)
                while ((i1, j1) != (turnPoint)):
                    if (img[i1][j1] != 0):
                        break
                    i1, j1 = travelClockwise(currentPoint, (i1, j1))

                if (i1 == 0 and j1 == 0):
                    contourType = 0
                else:
                    i2 = i1
                    j2 = j1
                    i3 = i
                    j3 = j
                    img, contour = traceContour(img, (i, j), (j1, j1), NBD, (i, j), (i1, j1))
                    contours.append(contour)

            # step 4
            if img[i][j] != 1:
                LNBD = abs(img[i][j])

    return contours
# test i4, j4 finding of 3.3
i = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,0,1,1,0],
     [0,0,0,1,1,1,1,0,0,0],
     [0,0,1,0,0,0,1,0,0,0],
     [0,1,1,0,0,0,1,0,0,0],
     [0,0,1,0,0,0,1,0,0,0],
     [0,0,0,1,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,0,0,0,0]]
# initialPoint = (1,3)
# currentPoint = (2,2)
# img, contour = traceContour(img, currentPoint, initialPoint, 2, currentPoint, initialPoint)
# print(contour)
f = open("sample.txt", "w")

# img = cv2.imread("hand2.png")
# i = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# for x in range(0, len(i)):
#     for y in range(0, len(i[x])):
#         if (i[x][y] != 0):
#             i[x][y] = 1
#
# print("done convert")

contours = findContours(i)
print(contours)

# for i in contours:
#     for x in i:
#         img = cv2.circle(img, x, radius=1, color=(0, 0, 255), thickness=-1)
#
# cv2.imshow("La", img)
# cv2.waitKey()

s = [[str(e) for e in row] for row in i]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print ('\n'.join(table))

f.write('\n'.join(table))

f.close()
