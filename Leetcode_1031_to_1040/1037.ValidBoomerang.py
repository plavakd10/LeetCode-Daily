def isBoomerang(points) -> bool:
    slope1_x = points[1][0]-points[0][0]
    slope1_y = points[1][1]-points[0][1]

    slope2_x = points[2][0]-points[1][0]
    slope2_y = points[2][1]-points[1][1]

    return (slope1_x*slope2_y)!=(slope2_x*slope1_y)