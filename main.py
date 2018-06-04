from src.probability import get_uniform_vector, sense, move
import yaml
import io


def main():
    with io.open('world.yaml', 'r') as file:
        world = yaml.load(file)
        grid = world['grid']
        z = world['z']
        u = world['u']

    p = get_uniform_vector(len(grid))
    for i in range(len(z)):
        p = move(p, u[i], 0.8, 0.1, 0.1)
        p = sense(p, z[i], grid, 0.6, 0.2)
        print(p)


if __name__ == '__main__':
    main()

