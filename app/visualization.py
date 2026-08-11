from matplotlib import pyplot as plt

from app.models import Frame


def visualize(frame_list: list[Frame]):
    fig = plt.figure(figsize=(30, 30, 'cm'))
    ax = fig.add_subplot(111, projection='3d')

    xs = [f.Position.x for f in frame_list]
    ys = [f.Position.y for f in frame_list]
    zs = [f.Position.z for f in frame_list]

    # Траектория
    ax.plot(xs, ys, zs, 'b--')
    ax.scatter(xs[1:-1], ys[1:-1], zs[1:-1], color='blue', s=30)

    # Точки
    ax.scatter(xs[0], ys[0], zs[0], color='green', s=100)
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=100)

    ax.scatter([0.0, 0.0], [0.0, 2.0], [0.0, 0.0], color='#FFA500', s=120)
    ax.plot([0.0, 0.0], [0.0, 2.0], [0.0, 0.0], '#FFA500')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.invert_xaxis()
    ax.view_init(elev=-70, azim=160, roll=-70)

    plt.show()
