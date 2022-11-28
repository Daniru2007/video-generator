import moviepy.editor as mv
import os


def generate_vid(content):
    print("generating video")
    clips = []

    clip = mv.ImageClip(content["path"]).set_duration(content["len"])
    clips.append(clip)
    for data in content["data"]:
        file = data["path"]
        clip = mv.ImageClip(file).set_duration(data["len"])
        clips.append(clip)

    video_clip = mv.concatenate_videoclips(clips, method="compose")
    audio = mv.AudioFileClip("out.mp3")
    audio_clip = mv.CompositeAudioClip([audio])
    video_clip.audio = audio_clip
    video_clip.write_videofile("output.mp4", fps=24, remove_temp=True)
