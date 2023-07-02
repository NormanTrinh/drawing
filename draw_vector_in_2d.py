import matplotlib.pyplot as plt

def draw_vector(vector, color, label):
    plt.arrow(0, 0, vector[0], vector[1], head_width=0.3, head_length=0.3, fc=color, ec=color)
    plt.text(vector[0] + 0.5, vector[1] + 0.5, label)

def draw_vectors(vectors_dict):
    max_x = max(v[0] for v in vectors_dict.values())
    max_y = max(v[1] for v in vectors_dict.values())

    plt.xlim(0, max_x + 2)
    plt.ylim(0, max_y + 2)
    plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to equal

    # Set major and minor ticks to show grid lines
    plt.gca().set_xticks(range(0, max_x + 2), minor=False)
    plt.gca().set_yticks(range(0, max_y + 2), minor=False)
    plt.gca().set_xticks(range(0, max_x + 1), minor=True)
    plt.gca().set_yticks(range(0, max_y + 1), minor=True)

    plt.grid(which='both', color='gray', linestyle='-', linewidth=0.5)
    plt.grid(which='minor', alpha=0)  # Hide minor grid lines

    for i, (name, vector) in enumerate(vectors_dict.items()):
        color = ['r', 'g', 'b', 'c', 'm', 'y', 'k'][i % 7]  # Cycle through colors

        draw_vector(vector, color, name)

    plt.show()

vectors_dict = {
    'a': [4, 8],
    'b': [9, 3],
    'c': [6, 2],
    'd': [5, 5]
}

draw_vectors(vectors_dict)
