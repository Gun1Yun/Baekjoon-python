# 주유소
import sys
In = sys.stdin.readline


def main():
    city_num = int(In())
    distance = list(map(int, In().split()))
    cost = list(map(int, In().split()))

    distance.append(0)

    n_cost = cost[0]
    n_distance = distance[0]
    answer = 0

    for i in range(1, city_num):
        if i == city_num-1:
            answer += n_cost*n_distance
            break

        if cost[i] < n_cost:
            answer += n_cost*n_distance
            n_cost = cost[i]
            n_distance = distance[i]
        else:
            n_distance += distance[i]

    print(answer)


if __name__ == "__main__":
    main()
