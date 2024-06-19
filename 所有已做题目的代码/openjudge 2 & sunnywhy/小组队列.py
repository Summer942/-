from collections import deque
t=int(input())
groups_dict={}
members_dict={}
for _ in range(t):
    members=list(map(int,input().split()))
    groups_dict[_+1]=deque()
    for member in members:
        members_dict[member]=_+1
queue=deque()
queue_set=set()
while True:
    command=input().split()
    if command[0]=='STOP':
        break
    elif command[0]=='ENQUEUE':
        person=int(command[1])
        group=members_dict[person]
        groups_dict[group].append(person)
        if group not in queue_set:
            queue.append(group)
            queue_set.add(group)
    else:
        if queue:
            group=queue[0]
            person=groups_dict[group].popleft()
            print(person)
            if not groups_dict[group]:
                queue.popleft()
                queue_set.remove(group)
    
