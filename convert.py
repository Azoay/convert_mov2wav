import pathlib, subprocess

def main(infile, outfile):
	command = "ffmpeg.exe -i {} {}".format(infile,outfile)
	print(command)
	subprocess.call(command.split())

def wrap(dist="."):
	p = pathlib.Path(dist)
	for c in sorted(p.iterdir()):
		if c.suffix in [".MOV",".mov"]:
			out = p / "{}.wav".format(c.stem)
			main(c.as_posix(), out.as_posix())

if __name__ == '__main__':
    wrap()

