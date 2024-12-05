import numpy

class position:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y
    x: int
    y: int

# calculates the distance between 2 points
def distance(position_1: position, position_2: position) -> float:
    distance_x = position_1.x - position_2.x
    distance_y = position_1.y - position_2.y
    total_distance = numpy.sqrt(distance_x**2 + distance_y**2)
    return total_distance

# finds in which quarter position 2 is in relation to position 1
def find_quarter(position_1: position, position_2: position) -> int:
    if position_1.x <= position_2.x and position_1.y > position_2.y:
        return 0
    if position_1.x < position_2.x and position_1.y <= position_2.y:
        return 90
    if position_1.x >= position_2.x and position_1.y < position_2.y:
        return 180
    if position_1.x > position_2.x and position_1.y >= position_2.y:
        return 270
    quit("couldn't find quarter")


def angle_between_points(origin: position, destination: position) -> int:
    distance_x = numpy.abs(destination.x - origin.x)
    distance_y = numpy.abs(destination.y - origin.y)
    _distance = distance(origin, destination)
    
    destination_quarter = find_quarter(origin, destination)

    # we select whethet to count the sinus from distance x or distance y, depending on the quarter the destination is in
    if destination_quarter == 0 or destination_quarter == 180:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(distance_x / _distance)))
    if destination_quarter == 90 or destination_quarter == 270:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(distance_y / _distance)))

    # print("destination quarter: ", destination_quarter)
    # print("angle in quarter: ", angle_to_destination)
    # print("Global angle: ", angle_to_destination + destination_quarter)

    angle_to_destination += destination_quarter
    return angle_to_destination


def one_sided_mirror_angle(laser_origin: position, mirror: position, destination: position) -> int:
    angle_to_laser: int = angle_between_points(mirror, laser_origin)
    angle_to_destination: int = angle_between_points(mirror, destination)

    # we check the angle between the 2 points
    angle = numpy.abs(angle_to_destination - angle_to_laser)
    # we find the middle point
    angle //= 2
    # we add the lower angle to find it's global position
    angle += min(angle_to_laser, angle_to_destination)

    # if the angle between the points is higher than 180, we must offset the final angle by 180 degrees
    if numpy.abs(angle_to_destination - angle_to_laser) >= 180:
        angle = (angle + 180) % 360
    return angle


# test data
if __name__ == "__main__":
    print("test1")
    laser_origin = position(2, 0)
    mirror = position(0, 0)
    destination = position(0, 2)

    result = one_sided_mirror_angle(laser_origin, mirror, destination)
    print(result)
    print(result == 135)

    result = angle_between_points(mirror, destination)
    print(result)
    print(result == 180)

    result = angle_between_points(mirror, laser_origin)
    print(result)
    print(result == 90)

    
    print("\ntest2")
    laser_origin = position(0, 0)
    mirror = position(2, 0)
    destination = position(2, 2)

    result = one_sided_mirror_angle(laser_origin, mirror, destination)
    print(result)
    print(result == 225)

    result = angle_between_points(mirror, destination)
    print(result)
    print(result == 180)

    result = angle_between_points(mirror, laser_origin)
    print(result)
    print(result == 270)