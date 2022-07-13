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



def HookeJeeves(startPoint, delta, accuracy):
    print('Начальная точка:', startPoint[0], startPoint[1], '; F(x, y) =', Function(startPoint))
    stop = False
    Point1 = startPoint
    while not stop:
        print()
        print('     Исслед. поиск:')
        delta_ = delta
        while not stop and Point1 == startPoint:
            Point1 = expSearch(startPoint, delta_)  
            if delta_ > accuracy:
                delta_ = delta_/10
            else:
                stop = True
            print('нашел точку:', Point1[0], Point1[1], Function(Point1))
        print('     Результат поиска:', Point1[0], Point1[1], Function(Point1))
        print()
        print('     Поиск по образцу:')

        Point2 = Point1
        isLess = True
        while not stop and isLess:
            Point1 = Point2
            x1 = startPoint[0] + 2*(Point1[0] - startPoint[0])
            x2 = startPoint[1] + 2*(Point1[1] - startPoint[1])
            Point2 = expSearch([x1, x2], delta)
            if Function(Point1) <= Function(Point2):
                isLess = False
            print('нашел точку:', Point2[0], Point2[1], Function(Point2))
        print('     Результат поиска:', Point1[0], Point1[1], Function(Point1))
        startPoint = Point1

    result = startPoint
    return result


x1 = 1.5
x2 = 2.0
Point = [x1, x2]
delta = 0.0004
accuracy = 0.00001
result = HookeJeeves(Point, delta, accuracy)
print()
print('Результат работы алгоритма:', result[0], result[1], Function(result))
print()
