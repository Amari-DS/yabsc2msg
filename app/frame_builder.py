from app.models import Camera, Transition, Frame
from app.transitions.base import PointGeneratorFactory


class FrameBuilder:

    def __init__(self, start_cam: Camera, end_cam: Camera, transition: Transition):
        self.__start_cam = start_cam
        self.__end_cam = end_cam
        self.__transition = transition

    def build(self) -> list[Frame]:
        frame_count = int(self.__transition.duration / self.__transition.keyframe_interval)
        frame_duration = round(self.__transition.duration / frame_count, 5)
        position_generator = PointGeneratorFactory.create(start=self.__start_cam.position,
                                                          end=self.__end_cam.position,
                                                          interpolation=self.__transition.position_interpolation)
        rotation_generator = PointGeneratorFactory.create(start=self.__start_cam.rotation,
                                                          end=self.__end_cam.rotation,
                                                          interpolation=self.__transition.rotation_interpolation)
        frames = []
        for i in range(1, frame_count + 1):
            t_linear = i / frame_count
            position = position_generator.generate(t_linear)
            rotation = rotation_generator.generate(t_linear)
            frame = Frame(
                Position=position,
                Rotation=rotation,
                Duration=frame_duration,
                HoldTime=0.0,
            )
            frames.append(frame)
        last_frame = frames[-1]
        last_frame.HoldTime = self.__transition.hold
        return frames
