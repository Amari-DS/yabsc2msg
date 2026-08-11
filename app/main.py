from app.frame_builder import FrameBuilder
from app.io_module import load_config_from_json, save_to_json
from app.models import Frame, MovementScript
from app.visualization import visualize


def main():
    config = load_config_from_json('input.json')
    cameras_dict = {c.name: c for c in config.cameras}
    start_cam = cameras_dict.get('default')
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
    save_to_json('output.json', movement_script)
    return all_frames


if __name__ == "__main__":
    # YABSCMSG
    frame_list = main()
    visualize(frame_list)
