import numpy as np
from moviepy import VideoFileClip

from gptOS.lmi.components.description import Description


Video = Description.variant(
    "Video", VideoFileClip | np.array, loader=lambda path: VideoFileClip(path)
)
