import argparse

from app.frame_builder import FrameBuilder
from app.io_module import load_config_from_json, save_to_json
from app.models import Frame, MovementScript
from app.visualization import visualize


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Yet Another Beat Saber Camera2 Movement Script Generator'
    )
    parser.add_argument(
        '-i',
        '--input',
        default='input.json',
        help='Path to the input JSON file (default: input.json)',
    )
    parser.add_argument(
        '-o',
        '--output',
        default='output.json',
        help='Path to the output JSON file (default: output.json)',
    )
    return parser.parse_args()


def main():
    args = _parse_args()

    config = load_config_from_json(args.input)
    cameras_dict = {c.name: c for c in config.cameras}
    start_cam = next(c for c in cameras_dict.values() if c.is_start)
    all_frames = [Frame(
        Position=start_cam.position,
        Rotation=start_cam.rotation,
        Duration=0.0,
        HoldTime=0.0
    )]
    for transition in config.transitions:
        end_cam = cameras_dict.get(transition.target)
        builder = FrameBuilder(start_cam=start_cam, end_cam=end_cam, transition=transition)
        all_frames.extend(builder.build())
        start_cam = end_cam
    movement_script = MovementScript(
        SyncToSong=config.sync_to_song,
        Loop=config.loop,
        Frames=all_frames
    )
    save_to_json(args.output, movement_script)
    visualize(all_frames, cameras_dict.values())
    return all_frames


if __name__ == "__main__":
    # YABSC2MSG
    main()
