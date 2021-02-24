import imageio
import os

clip = os.path.abspath('video.mp4')


def gif_maker(input_path, target_format):
    output_path = os.path.splitext(input_path)[0] + target_format

    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)
    
    print('Done!')
    writer.close()

gif_maker(clip, '.gif')

'''
 - Let's run that beaty
 - Ops I guess it's called split ext, Now let's try this one more time
 - Oh my god this is taking forever -> Meme of Pablo waiting
'''