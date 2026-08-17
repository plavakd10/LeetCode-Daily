def calc(self, drone, target):
    d = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
    return d <= drone[2], d

def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
    candidates = []

    for i, drone in enumerate(drones):
        canReach, distance = self.calc(drone, target)

        if canReach:
            candidates.append((distance, i))

    if not candidates:
        return -1

    candidates.sort()

    return candidates[0][1]  