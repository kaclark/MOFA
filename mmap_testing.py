import mmap

f = open("path.extension", 'r+b')
mm = mmap.mmap(f.fileno(), 0)
lines = mm.readline()
while lines:
    print(lines)
    lines == mm.readline()
f.close()
