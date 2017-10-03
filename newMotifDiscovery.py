#Data Formats
#Josh Rudolph
#9/27/17

from Bio.motifs import meme

with open("test5.txt", 'r' ) as f:
	record = meme.read(f)

print record