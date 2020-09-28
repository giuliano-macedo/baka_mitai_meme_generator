#!/usr/bin/env python3
from pathlib import Path
import argparse

RESULTS_PATH=Path("./results")

parser=argparse.ArgumentParser()
parser.add_argument("image",type=Path)
parser.add_argument("-a","--adversary",action="store_true")
parser.add_argument("-r","--relative",action="store_false")
parser.add_argument("-A","--adapt-movement-scale",action="store_false")
parser.add_argument("-c","--cpu",action="store_true",help="Use CPU instead of CUDA GPU")

args=parser.parse_args()

assert(args.image.is_file())

print("loading libraries")

import imageio
from skimage.transform import resize
import warnings
import sys;sys.path.append("./first-order-model")
from demo import load_checkpoints,make_animation
from skimage import img_as_ubyte
from subprocess import run
import shlex
warnings.filterwarnings("ignore")

print("loading model,","using" if args.adversary else "not using","adversary")
generator, kp_detector = load_checkpoints(
	config_path='./first-order-model/config/vox-256.yaml', 
    checkpoint_path='./data/vox-cpk.pth.tar' if not args.adversary else "./data/vox-adv-cpk.pth.tar",
    cpu=args.cpu
)

print("loading input")
source_image = imageio.imread(args.image)
driving_video = imageio.mimread('data/template.mp4', memtest=False)

source_image = resize(source_image, (256, 256))[..., :3]
driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]
print("making predictions")
predictions = make_animation(
	source_image, driving_video, generator, kp_detector,
	relative=args.relative,
	adapt_movement_scale=args.adapt_movement_scale,
	cpu=args.cpu
)
RESULTS_PATH.mkdir(exist_ok=True)

output_base=str(RESULTS_PATH/Path(args.image.stem))
output_no_audio=output_base+".mp4"
output_audio=output_base+"_audio.mp4"

print("saving",output_no_audio)
imageio.mimsave(output_no_audio, [img_as_ubyte(frame) for frame in predictions], fps=30)

print("adding audio",output_audio)
cmd=f"ffmpeg -y -i {output_no_audio} -i data/template.mp3 -codec copy -shortest {output_audio}"
ret=run(shlex.split(cmd),capture_output=True)
if ret.returncode!=0:
	print(f"ERROR EXECUTING '{cmd}'")
	print("-"*48)
	print(ret.stderr)
	print("-"*48)
	exit(-1)

print("done.")