

def compare_triplets(a, b):
    zipped = zip(a, b)
    a_score = 0
    b_score = 0
    for alice, bob in zipped:
        if alice > bob:
            a_score += 1
        elif bob > alice:
            b_score += 1
        else:
            continue
    return [a_score, b_score]
