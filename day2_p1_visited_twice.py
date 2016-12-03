def findBunnyHQ(document):
    # West - 0, North - 1, East - 2, South - 3
    direction = 1
    coord = [0, 0]
    visited = set()
    for i in document:
        # Figure out what direction you're facing
        if i[0] == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        # Add steps to coordinates
        steps = int(i[1:])

        # Should be able to improve efficiency here
        for s in range(steps):
            if tuple(coord) in visited:
                print abs(coord[0]) + abs(coord[1])
                return

            visited.add((coord[0], coord[1]))

            if direction == 0:
                coord[0] -= 1
            elif direction == 1:
                coord[1] += 1
            elif direction == 2:
                coord[0] += 1
            elif direction == 3:
                coord[1] -= 1

if __name__ == '__main__':
    findBunnyHQ(["R3", "L5", "R1", "R2", "L5", "R2", "R3", "L2", "L5", "R5",
                 "L4", "L3", "R5", "L1", "R3", "R4", "R1", "L3", "R3", "L2",
                 "L5", "L2", "R4", "R5", "R5", "L4", "L3", "L3", "R4", "R4",
                 "R5", "L5", "L3", "R2", "R2", "L3", "L4", "L5", "R1", "R3",
                 "L3", "R2", "L3", "R5", "L194", "L2", "L5", "R2", "R1", "R1",
                 "L1", "L5", "L4", "R4", "R2", "R2", "L4", "L1", "R2", "R53",
                 "R3", "L5", "R72", "R2", "L5", "R3", "L4", "R187", "L4", "L5",
                 "L2", "R1", "R3", "R5", "L4", "L4", "R2", "R5", "L5", "L4",
                 "L3", "R5", "L2", "R1", "R1", "R4", "L1", "R2", "L3", "R5",
                 "L4", "R2", "L3", "R1", "L4", "R4", "L1", "L2", "R3", "L1",
                 "L1", "R4", "R3", "L4", "R2", "R5", "L2", "L3", "L3", "L1",
                 "R3", "R5", "R2", "R3", "R1", "R2", "L1", "L4", "L5", "L2",
                 "R4", "R5", "L2", "R4", "R4", "L3", "R2", "R1", "L4", "R3",
                 "L3", "L4", "L3", "L1", "R3", "L2", "R2", "L4", "L4", "L5",
                 "R3", "R5", "R3", "L2", "R5", "L2", "L1", "L5", "L1", "R2",
                 "R4", "L5", "R2", "L4", "L5", "L4", "L5", "L2", "L5", "L4",
                 "R5", "R3", "R2", "R2", "L3", "R3", "L2", "L5"])
