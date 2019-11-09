import sys
import math
import itertools
from functools import total_ordering


@total_ordering
class Point:
    """ Represents 2-D point """

    def __init__(self, x: int, y: int):
        """ Creates Point instance by supplying x and y coordinate 
        """
        self._x: int = x
        self._y: int = y

    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"[x: {self._x}, y: {self._y}]"

    def __eq__(self, other) -> bool:
        """X and Y coordinates are compared.

        Return:
        True if both coordinates are same"""
        if isinstance(other, Point):
            return self._x == other.x and self._y == other.y            
        return NotImplemented


    def __ne__(self, other) -> bool:
        return not (self == other)


    def __lt__(self, other):
        """ Points are compared in X coordinate at first. If X are equals use Y coordinate
        """
        retVal = None

        if self._x < other.x:
            retVal = True
        elif self._x == other.x:
            retVal = self._y < other.y
        else:
            retVal = False
        
        return retVal


    def __hash__(self):
        return hash((self._x, self._y))


    def getSlopeTo(self, that: "Point") -> float:
        """ Returns slope between this and that point

            Returns:
            slope between this and that point or positive infinity if line is horizontal
        """
        retVal = None

        if that.x == self._x and that.y == self._y:
            retVal = (-1) * math.inf
        elif that.x == self._x:
            retVal = math.inf            
        else:
            retVal = (that.y - self._y) / (that.x - self._x)

        return retVal



class Utils:
    """ Utiliry class for collinear points """

    @staticmethod
    def areFloatsSame(f1: float, f2: float):
        return math.isclose(f1, f2, rel_tol=1e-05)


    @staticmethod
    def arePointsCollinear(pts: list) -> bool:
        """ Tests if input points are collinear.
            To check whether the 4 points p, q, r, and s are collinear, 
            check whether the three slopes between p and q, between p and r, 
            and between p and s are all equal.
            Take first point in the list and check its collinearity with each other.

            If length of input array is lower then 2 ValueError is thrown.

            Parameters:
            pts: input points to be tested

            Returns:
            True if all points are collinear
        """

        if pts is None or len(pts) < 2:
            raise ValueError("Input array cannot be None of contain only one point")


        retVal = True
        slope: float = None
        firstPoint: Point = pts[0]

        for p in pts:
            if firstPoint == p:
                continue
            if slope is None:
                slope = firstPoint.getSlopeTo(p)
            else:
                if not Utils.areFloatsSame(slope, firstPoint.getSlopeTo(p)):
                    retVal = False
                    break

        return retVal



class LineSegment:
    """ List of collinear points """

    def __init__(self, pts: list):
        """ Creates line segment. Input points are in sorted order in 
            line segment instance to be able to compare instances easily

            Parameters:
            pts list of 2-D points
        """
        self._points = sorted(pts)

    @property
    def points(self):
        return self._points


    def __repr__(self):
        return f"LineSegment: <{len(self._points)}> | <{self._points}>"


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, LineSegment):
            return self._points == other.points
            
        return NotImplemented

    def contains(self, other: "LineSegment") -> bool:
        """ Checks if line segment other is part of self line segment

            Return:
            True if all points of other line segment are already part of another line point
        """
        retVal = True

        for i in other.points:
            if not i in self._points:
                retVal = False

        return retVal




class FindCollinearPoints:
    """ Super class for both find methods
    """

    def __init__(self, points: list):
        """ Creates instance from input points 

            Parameters:
            points: list of Point instances to find the max. collinear points
        """
        self._points: list = points
        self._lineSegments: list = []


    @property
    def lineSegments(self):
        return self._lineSegments


    def _addLineSegment(self, ls: LineSegment) -> None:
        """ Checks if line segment is also included in line segments.
            It also checks whether some line segment is part of another line segment.
            Both cases are not inluded in line segment
        """
        alreadyIncluded = False

        for myls in self._lineSegments:
            if myls.contains(ls):
                alreadyIncluded = True
                break

        if not alreadyIncluded:
            self._lineSegments.append(ls)


    def findLineSegments(self) -> None:
        """ Method to be implemeted in subclasses """
        raise NotImplementedError("Method must be overriden")




class BruteCollinearPoints(FindCollinearPoints):
    """ Find line segments with maximum number of collinear points 
       (at least 4 collinear points) by brute force solution """

    def __init__(self, points: list):
        """ Creates instance from input points 

            Parameters:
            points: list of Point instances to find the max. collinear points
        """
        super().__init__(points)


    def findLineSegments(self) -> None:
        """ Finds all line segments and store them to be accessible via lineSegment.
            Finds longest line segments of collinear points first. Create all possible combinations 
            of points where first combinations are of size of input array.
            Size of each next combinations are decremented by 1 until we reach
            size of 4 what is max. count of collinear points in line segment.
        """
        n = len(self._points)

        for i in range(n, 3, -1):
            for c in itertools.combinations(self._points, i):
                if Utils.arePointsCollinear(c):
                    ls = LineSegment(c)
                    self._addLineSegment(ls)

           







class FastCollinearPoints(FindCollinearPoints):
    """ Find line segments with maximum number of collinear points 
       (at least 4 collinear points). Algorithm takes one point from the list
       after another where for each point are points sorted according to
       slope with this point. Afterwards are taken all adjacent points with the same
       slope to be collinear.
    """

    def __init__(self, points: list):
        """ Creates instance from input points 

            Parameters:
            points: list of Point instances to find the max. collinear points
        """
        super().__init__(points)




    def findLineSegments(self) -> None:
        """ Finds all line segments and store them to be accessible via lineSegment.
        """
        # Possible improvements could be to create dictionary at first with keys as points
        # and values as slopes to calcucate slope only once

        for p in self._points:
            
            # Sort the list according to slope of each point to the point p
            sortedPts = sorted(self._points, key = lambda x: p.getSlopeTo(x))

            # Find the groups of at least four points with the same slope
            currSlope = p.getSlopeTo(p)
            currPts = [p]
            # First point in sorted list is always skipped (slope between point p and p is negative infinity)               
            for tp in sortedPts[1:]:
                if Utils.areFloatsSame(currSlope, p.getSlopeTo(tp)):
                    currPts.append(tp)
                else:
                    if len(currPts) > 3:
                        ls = LineSegment(currPts)
                        self._addLineSegment(ls)
                    currPts = [p, tp] # create new array                        
                    currSlope = p.getSlopeTo(tp) # start comparing with new slope            


