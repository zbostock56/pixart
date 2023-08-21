from PIL import Image
import numpy as np

def pixelate_multi(level, i, files):
  image = Image.open(''.join(files[0][i]))
  new_dims = [int(np.round(a * level)) for a in image.size]
  return image.resize(new_dims).resize(image.size, resample = 4)

def pixelate(level, path):
  image = Image.open(path)
  new_dims = [int(np.round(a * level)) for a in image.size]
  return image.resize(new_dims).resize(image.size, resample = 4)
