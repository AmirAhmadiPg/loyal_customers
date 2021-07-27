
def gen(centroids_color, c=1):
    guide_string = f'Guide {c}:\n\t'
    for i in range(len(centroids_color)):
        guide_string += f'Clustur {i}: '

        guide_string += f'{centroids_color[i]} dot\n\t'

    return guide_string