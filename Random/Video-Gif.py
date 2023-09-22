from moviepy.editor import *
video=VideoFileClip("video.mp4").subclip(10,20)
video.write_gif("gif.gif")