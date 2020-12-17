import copy
import sys

SCAN_DIRETION = 0  # 扫描方向，0代表向小的方向，1代表向大的方向
START_SCAN = 0  # 开始扫描的位置
MAX_DISK_COUNT = 100  # 最大磁道数为一百
Request_Count = 0


def FCFS(Request_List):
    # 先来先服务算法
    result_queue = copy.copy(Request_List)
    result_queue.insert(0, START_SCAN)
    return result_queue


def findNearest(current, Request_List, visited):
    # 寻找最短路径节点
    minDis = MAX_DISK_COUNT
    minIndex = -1
    for i in range(len(Request_List)):
        if visited[i] is False:
            dis = abs(current - Request_List[i])
            if dis < minDis:
                minDis = dis
                minIndex = i
    visited[minIndex] = True
    return minIndex, minDis


def SSTF(Request_List):
    # 最短寻道时间
    visited = [False] * len(Request_List)
    queue = []
    current = START_SCAN  # 开始扫描的位置
    for i in range(len(Request_List) + 1):
        index, dis = findNearest(current, Request_List, visited)
        queue.append(current)
        current = Request_List[index]
    return queue


def Elevator(Request_List):
    # 电梯算法
    global SCAN_DIRETION
    queue = []
    current = START_SCAN
    queue.append(current)

    request = Request_List
    while True:
        if SCAN_DIRETION == 1:
            request.sort()
            for i in range(len(request)):
                if request[i] >= current:
                    queue.append(request[i])
                i += 1
            SCAN_DIRETION = 0
            if len(request) < len(queue):
                break

        if SCAN_DIRETION == 0:
            request.sort(reverse=True)
            for i in range(len(request)):
                if request[i] <= current:
                    queue.append(request[i])
                i += 1
            SCAN_DIRETION = 1
            if len(request) < len(queue):
                break

    return queue


def show(List):
    print('访问磁道的序列为：', end=' ')
    for item in List:
        print('{} '.format(item), end=' ')
    count = sum(abs((List[i] - List[i - 1])) for i in range(1, len(List)))
    print('\n总寻到数为：' + '{}'.format(count))
    print('平均移动磁道数为： %.2f' % (count / Request_Count))


if __name__ == '__main__':
    Request_List = []
    Request_Count = eval(input('请输入寻道次数：'))
    count = Request_Count
    START_SCAN = eval(input('请输入磁头移动起点：'))
    while True:
        if START_SCAN < 0 or START_SCAN > 100:
            print('磁头起点应在（0-100）范围内')
        START_SCAN = eval(input())
    print('请输入磁道访问序列(以空格分隔)：')
    while True:
        string = input()
        num = [int(n) for n in string.split()]
        if len(num) != count:
            print('您的输入有误，请重新输入')
        else:
            break
    for index in num:
        if index > MAX_DISK_COUNT:
            print('磁道数最大为100，请重新输入！')
        if index < 0:
            print('磁道数应大于0，请重新输入！')
    Request_List = num
    print('请选择调度算法：')
    print('1.先来先服务算法')
    print('2.最短寻道时间算法')
    print('3.电梯算法')
    print('4.输出所有算法')

    select = eval(input())
    while True:
        if select in [1, 2, 3, 4]:
            break
        else:
            print('您的输入有误，请重新输入')
            select = eval(input())

    if select == 1:
        show(FCFS(Request_List))
    elif select == 2:
        show(SSTF(Request_List))
    elif select == 3:
        while True:
            print('您选择的方向是：\n0.小\n1.大')
            SCAN_DIRETION = eval(input())
            if SCAN_DIRETION in [0, 1]:
                break
            else:
                print('您的输入有误，请重新输入')
        show(Elevator(Request_List))
    elif select == 4:
        while True:
            print('您选择的方向是：\n0.小\n1.大')
            SCAN_DIRETION = eval(input())
            if SCAN_DIRETION in [0, 1]:
                break
            else:
                print('您的输入有误，请重新输入')
        print('1.先来先服务：\n')
        show(FCFS(Request_List))
        print('2.最短寻道时间\n')
        show(SSTF(Request_List))
        print('3.电梯算法\n')
        show(Elevator(Request_List))
    sys.exit(0)
