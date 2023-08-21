import sys
from pixelation import pixelate_multi
from pixelation import pixelate

level = 0.25
files = []
path = ""
cmdline = sys.argv[1:]
multi = False
single = False
if len(cmdline) == 0:
  print("Usage:")
  print("-s    Choose % level of pixelation: [25%, 10%, 5%] - Defaults to 25%")
  print("-i    file input: /path/to/file.png")
  print("-m    multi-file input: /path/to/file.png /path/to/other_file.png")
  exit(0)
else:
  for i in range(len(cmdline)):
    if cmdline[i] == "-s":
      level = cmdline[i + 1]
      i = i + 1
      level = int(level) / 100
    elif cmdline[i] == "-m":
      multi = True
      files.append(cmdline[(i + 1):])
    elif cmdline[i] == "-i":
      single = True
      path = cmdline[(i + 1)]

if multi == True and single == True:
  print("ERROR: Only use -i or -m. Both cannot be used at once.")
elif multi == True:
  for i in range(len(files) + 1):
    print("Converting {}".format(files[0][i]))
    img = pixelate_multi(level, i, files)
    img.save(files[0][i] + ".jpg")
    print("Finished converting")
else:
  print("Converting {}".format(path))
  img = pixelate(level, path)
  img.save(path.join(".jpg"))
  print("Finished converting")
