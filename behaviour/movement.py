import math

# 🔷 Behaviour using multiple frames
def get_behaviour_sequence(frames_positions):

    movements = []

    for i in range(len(frames_positions) - 1):
        f1 = frames_positions[i]
        f2 = frames_positions[i + 1]

        for j in range(min(len(f1), len(f2))):
            x1, y1 = f1[j]
            x2, y2 = f2[j]

            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            movements.append(dist)

    if not movements:
        return "resting"

    avg = sum(movements) / len(movements)

    if avg > 40:
        return "crossing"
    elif avg > 10:
        return "moving"
    else:
        return "resting"


# 🔷 Flock density
def get_density(positions):

    if len(positions) < 2:
        return "low"

    distances = []

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances.append(d)

    avg = sum(distances) / len(distances)

    if avg < 100:
        return "high"
    elif avg < 300:
        return "medium"
    else:
        return "low"


# 🔷 Runway zone logic
def get_runway_zone(positions, image_height):

    danger = 0

    for x, y in positions:
        if y > image_height * 0.6:
            danger += 1

    if danger >= 3:
        return "high"
    elif danger >= 1:
        return "medium"
    else:
        return "low"