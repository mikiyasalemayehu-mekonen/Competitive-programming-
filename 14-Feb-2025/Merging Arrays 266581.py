# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
merged = []
first, second = 0, 0

while first < n and second < k:
    if list1[first] < list2[second]:
        merged.append(list1[first])
        first += 1
    else:
        merged.append(list2[second])
        second += 1

merged.extend(list1[first:])
merged.extend(list2[second:])

for i in range(len(merged)):
    print(merged[i], end=" ")