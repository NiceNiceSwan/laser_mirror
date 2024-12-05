import numpy

class position:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y
    x: int
    y: int


def distance(position_1: position, position_2: position) -> float:
    distance_x = position_1.x - position_2.x
    distance_y = position_1.y - position_2.y
    total_distance = numpy.sqrt(distance_x**2 + distance_y**2)
    return total_distance


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


def main():
    laser_origin_point = position(2, 0)
    mirror_position = position(0, 0)
    destination_point = position(4, 5)
    angle_to_laser: int = 0
    angle_to_destination: int = 0

    origin_mirror_distance_x = numpy.abs(laser_origin_point.x - mirror_position.x)
    origin_mirror_distance_y = numpy.abs(laser_origin_point.y - mirror_position.y)
    origin_mirror_distance = distance(mirror_position, laser_origin_point)

    laser_quarter = find_quarter(mirror_position, laser_origin_point)
    if laser_quarter == 0 or laser_quarter == 180:
        angle_to_laser = round(numpy.degrees(numpy.arcsin(origin_mirror_distance_x / origin_mirror_distance)))
    if laser_quarter == 90 or laser_quarter == 270:
        angle_to_laser = round(numpy.degrees(numpy.arcsin(origin_mirror_distance_y / origin_mirror_distance)))
    
    print("laser quarter: ", laser_quarter)
    print("angle in quarter: ", angle_to_laser)
    print("Global angle: ", angle_to_laser + laser_quarter)
    angle_to_laser += laser_quarter

    mirror_destination_distance_x = numpy.abs(destination_point.x - mirror_position.x)
    mirror_destination_distance_y = numpy.abs(destination_point.y - mirror_position.y)
    mirror_destination_distance = distance(mirror_position, destination_point)
    
    destination_quarter = find_quarter(mirror_position, destination_point)
    if destination_quarter == 0 or destination_quarter == 180:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(mirror_destination_distance_x / mirror_destination_distance)))
    if destination_quarter == 90 or destination_quarter == 270:
        angle_to_destination = round(numpy.degrees(numpy.arcsin(mirror_destination_distance_y / mirror_destination_distance)))

    print("destination quarter: ", destination_quarter)
    print("angle in quarter: ", angle_to_destination)
    print("Global angle: ", angle_to_destination + destination_quarter)
    angle_to_destination += destination_quarter

    # we check the angle between the 2 points
    angle = numpy.abs(angle_to_destination - angle_to_laser)
    # we find the middle point
    angle //= 2
    # we add the lower angle to find it's global position
    angle += min(angle_to_laser, angle_to_destination)

    # if the angle between the points is higher than 180, we must offset the final angle by 180 degrees
    if numpy.abs(angle_to_destination - angle_to_laser) >= 180:
        angle = (angle + 180) % 360
    else:
        angle %= 360
    print(angle)


main()