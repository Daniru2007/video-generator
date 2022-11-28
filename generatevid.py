import moviepy.editor as mv
import os


def generate_vid(content):
    clips = []

    clip = mv.ImageClip(content["path"]).set_duration(2)
    clips.append(clip)
    for data in content["data"]:
        file = data["path"]
        clip = mv.ImageClip(file).set_duration(2)
        clips.append(clip)

    video_clip = mv.concatenate_videoclips(clips, method="compose")
    video_clip.write_videofile("output.mp4", fps=24, remove_temp=True)
