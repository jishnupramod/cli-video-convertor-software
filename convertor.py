# This video covertor command line software only converts video to respective 
# target format. Audio format is not yet supported. 

# GUI Version is under development ! 

import imageio
# import glob
import os

# vid_file = glob.glob("./test.*") 

vid_file = input("Input File name: ")
clip = os.path.abspath(vid_file)

def video_convertor(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat 

    print(f'converting {inputPath}\nto {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
        print(f'Frame {frame}')
    
    print("Done!") 
    writer.close()

targetFormat = input("Target Format: ")
targetFormat = '.' + targetFormat

video_convertor(clip, targetFormat)

