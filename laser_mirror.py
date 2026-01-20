import numpy

class Position:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y
    x: int
    y: int

    def __eq__(self, value):
        if not isinstance(value, Position):
            return False
        
        if self.x == value.x and self.y == value.y:
            return True
        
        return False

# calculates the distance between 2 points
def distance(position_1: Position, position_2: Position) -> float:
    """Calculates the distance between 2 points. Returns the distance
    """
    distance_x = position_1.x - position_2.x
    distance_y = position_1.y - position_2.y
    total_distance = numpy.sqrt(distance_x**2 + distance_y**2)
    return total_distance

# finds in which quarter position 2 is in relation to position 1
def find_quarter(position_1: Position, position_2: Position) -> int:
    """finds in which quarter position 2 is in relation to position 1.

    Returns the lowest angle of the quarter. Goes counterclockwise. 0 means it's to the right and below, 90 to the right and above etc.
    As such, if you receive 0, that means position 2 is to the right and below position 1.

    Returns 0 if the positions are the same
    """
    if position_1 == position_2:
        return 0
    
    if position_1.x <= position_2.x and position_1.y > position_2.y:
        return 0
    if position_1.x < position_2.x and position_1.y <= position_2.y:
        return 90
    if position_1.x >= position_2.x and position_1.y < position_2.y:
        return 180
    if position_1.x > position_2.x and position_1.y >= position_2.y:
        return 270


def angle_between_points(origin: Position, destination: Position) -> int:
    distance_x = numpy.abs(destination.x - origin.x)
    distance_y = numpy.abs(destination.y - origin.y)
    _distance = distance(origin, destination)
    
    destination_quarter = find_quarter(origin, destination)

    # we select whethet to count the sinus from distance x or distance y, depending on the quarter the destination is in
    if destination_quarter == 0 or destination_quarter == 180:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(distance_x / _distance)))
    if destination_quarter == 90 or destination_quarter == 270:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(distance_y / _distance)))

    angle_to_destination += destination_quarter
    return angle_to_destination


def one_sided_mirror_angle(laser_origin: Position, mirror: Position, destination: Position) -> int:
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
