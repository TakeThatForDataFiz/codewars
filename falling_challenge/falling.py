def bouncing_ball(h, bounce, window):
    # check params are valid
    if h <= 0:
        return -1
    if bounce <= 0 or bounce >= 1:
        return -1
    if window >= h:
        return -1
    ball_sightings = 0

    while h > window:
        ball_sightings += 1
        h = bounce * h
        if h > window:
            ball_sightings += 1
    
    return ball_sightings

print(bouncing_ball(3, 0.66, 1.5))