import pytest
from alg import coll_points as cp
import time


def test_utils_1():
    assert not cp.Utils.areFloatsSame(0.01, 0.015)
    assert cp.Utils.areFloatsSame(2.3501, 2.3501)
    assert not cp.Utils.areFloatsSame(2.3501, 2.3507)
    assert cp.Utils.areFloatsSame(2.3500001, 2.3500007)


def test_utils_2():
    a = []

    # create list of collinear points
    a.append(cp.Point(200, 1000))
    a.append(cp.Point(300, 1500))
    a.append(cp.Point(400, 2000))
    a.append(cp.Point(500, 2500))

    assert cp.Utils.arePointsCollinear(a)

    # append not collinear points
    a.append(cp.Point(3000, 7000))

    assert not cp.Utils.arePointsCollinear(a)


def test_utils_3():
    a = []

    # append not collinear points
    a.append(cp.Point(3000, 7000))
    a.append(cp.Point(3200, 7000))
    a.append(cp.Point(3000, 7300))
    a.append(cp.Point(3700, 7800))

    assert not cp.Utils.arePointsCollinear(a)


def getPoints():
    a = []

    # create list of collinear points
    a.append(cp.Point(200, 1000))
    a.append(cp.Point(300, 1500))
    a.append(cp.Point(400, 2000))
    a.append(cp.Point(500, 2500))

    # create another list of collinear points
    a.append(cp.Point(200, 800))
    a.append(cp.Point(300, 1200))
    a.append(cp.Point(400, 1600))
    a.append(cp.Point(500, 2000))

    # append not collinear points
    a.append(cp.Point(3000, 7000))
    a.append(cp.Point(3200, 7000))
    a.append(cp.Point(3000, 7300))
    a.append(cp.Point(3700, 7800))
    a.append(cp.Point(4300, 8200))
    a.append(cp.Point(3000, 7500))
    a.append(cp.Point(3200, 7500))
    a.append(cp.Point(3400, 7500))

    # append collinear points
    a.append(cp.Point(600, 3000))
    a.append(cp.Point(700, 3500))

    return a


def getTestResult():
    t = []
    t.append(cp.Point(200, 1000))
    t.append(cp.Point(300, 1500))
    t.append(cp.Point(400, 2000))
    t.append(cp.Point(500, 2500))
    t.append(cp.Point(600, 3000))
    t.append(cp.Point(700, 3500))

    t2 = []
    t2.append(cp.Point(200, 800))
    t2.append(cp.Point(300, 1200))
    t2.append(cp.Point(400, 1600))
    t2.append(cp.Point(500, 2000))

    tls = [cp.LineSegment(t), cp.LineSegment(t2)]

    return tls


def test_brute_force():
    a = getPoints()
    tls = getTestResult()

    bf = cp.BruteCollinearPoints(a)
    bf.findLineSegments()

    assert bf.lineSegments == tls  # Expected result

    # for b in bf.lineSegments:
    #     print(b)


def test_fast():
    a = getPoints()
    tls = getTestResult()

    ff = cp.FastCollinearPoints(a)
    ff.findLineSegments()

    assert ff.lineSegments == tls  # Expected result
    # for f in ff.lineSegments:
    #     print(f)


# test_utils_1()
# test_utils_2()
# test_utils_3()

# start_time = time.time()
# test_brute_force()
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# test_fast()
# print("--- %s seconds ---" % (time.time() - start_time))
