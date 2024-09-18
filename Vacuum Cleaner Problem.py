from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def is_valid(x, y, room):
    return 0 <= x < len(room) and 0 <= y < len(room[0])
def bfs_vacuum(room, start_x, start_y):
    queue = deque([(start_x, start_y)])  
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        if room[x][y] == 1:
            room[x][y] = 0
            print(f"Cleaning cell ({x}, {y})")
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y, room) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))
def is_room_clean(room):
    for row in room:
        if 1 in row:
            return False
    return True
room = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]
start_x, start_y = 0, 0
print("Initial room state:")
for row in room:
    print(row)
bfs_vacuum(room, start_x, start_y)
if is_room_clean(room):
    print("\nThe room is now clean!")
else:
    print("\nThe room is not fully clean.")
print("Final room state:")
for row in room:
    print(row)
