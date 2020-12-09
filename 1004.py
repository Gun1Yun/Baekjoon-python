"""
어린왕자

==풀이==
시작점이 원 내부
출발점이 원 내부
합하기
"""
import sys
In = sys.stdin.readline


def solving(point, maps):
    start = point[:2]
    finish = point[2:]

    result = 0

    for planet in maps:
        planet_point = planet[:2]
        planet_r = planet[2]

        start_distance = (start[0]-planet_point[0])**2 + \
            (start[1]-planet_point[1])**2
        finish_distance = (finish[0]-planet_point[0]
                           )**2 + (finish[1]-planet_point[1])**2

        planet_r = planet_r**2

        start_in = (start_distance < planet_r)
        finish_in = (finish_distance < planet_r)

        if start_in == False and finish_in == True:
            result += 1
        elif start_in == True and finish_in == False:
            result += 1

    return result


def main():
    case_cnt = int(In())
    point_set = []
    map_set = []
    for _ in range(case_cnt):
        point = list(map(int, In().split()))
        point_set.append(point)

        map_size = int(In())
        maps = []
        for _ in range(map_size):
            planet = list(map(int, In().split()))
            maps.append(planet)
        map_set.append(maps)

    for point, maps in zip(point_set, map_set):
        print(solving(point, maps))


main()
