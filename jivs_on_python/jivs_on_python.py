def Function(Point):
    x1 = Point[0]
    x2 = Point[1]
    func = (1 - x1)**2 + 100*(x2 - x1**2)**2   
    return func


def expSearch(Point, delta):
    check = [Point[0] + delta, Point[1]]
    newPoint = []
    if Function(check) < Function(Point):
        newPoint.append(check[0])
    else:
        check[0] = Point[0] - delta
        if Function(check) < Function(Point):
            newPoint.append(check[0])
        else:
            newPoint.append(Point[0])

    check = [newPoint[0], Point[1] + delta]
    if Function(check) < Function(Point):
        newPoint.append(check[1])
    else:
        check[1] = Point[1] - delta
        if Function(check) < Function(Point):
            newPoint.append(check[1])
        else:
            newPoint.append(Point[1])
    return newPoint
