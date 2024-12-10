import os

import numpy as np
import rawpy
import matplotlib.pyplot as plt

#import cv2

plt.close('all')

path="."
raw_name_sony = "DSC00046.ARW"
output_name= "output.JPG"
with rawpy.imread(os.path.join(path,raw_name_sony)) as raw:
  print(f" raw pattern:\n {raw.raw_pattern}\n raw type\n {raw.raw_type}\n sizes: {raw.sizes}")
#  decoded = raw.postprocess()[:, :, [2, 1, 0]]
  #cv2.imwrite(os.path.join(path,output_name),decoded)
  try:
    thumb = raw.extract_thumb()
  except rawpy.LibRawNoThumbnailError:
    print('no thumbnail found')
  except rawpy.LibRawUnsupportedThumbnailError:
    print('unsupported thumbnail')
  else:
    if thumb.format == rawpy.ThumbFormat.JPEG:
      with open('thumb.jpg', 'wb') as f:
        f.write(thumb.data)
    elif thumb.format == rawpy.ThumbFormat.BITMAP:
      imageio.imsave('thumb.tiff', thumb.data)

  counts = np.bincount(raw.raw_image.flatten())
  fig, ax = plt.subplots(1, 1)
  ax.plot(counts, '.')
  plt.savefig("total_histogram.png")

  # Get pixel value
  im = raw.raw_image_visible # .astype(np.float32)
  print(im[0:4, 0:12])
  #im = np.expand_dims(im, axis=2)
  #img_shape = im.shape
  H = im.shape[0]
  W = im.shape[1]
  print(im.max())
  image = np.stack([im[0:H:2, 0:W:2],
                    im[0:H:2, 1:W:2],
                    im[1:H:2, 0:W:2],
                    im[1:H:2, 1:W:2],], dtype=np.uint16)
  for ch in range(4):
    print(image[0:3, 0:3, ch])
  print(image.max())

  fig, ax = plt.subplots(4, 1, sharex=True)
  fig.suptitle("Pixel Value Distribution for Each Channel")
  for ch in range(4):
    print(f'channel {ch+1} description {raw.color_desc[ch]}')
    channel_values = image[:, :, ch]
    mean_value = np.mean(channel_values)
    max_value = np.max(channel_values)
    min_value = np.min(channel_values)
    counts = np.bincount(channel_values.flatten())
    #channel_stats.append((mean_value, max_value, min_value))
    print(f"Channel {ch}: Mean={mean_value:}, Max={max_value}, Min={min_value}")
    ax[ch].plot(counts, '.')
    #ax[ch].set_xlim([0, 1023])
    print(counts[1000:1030])
  input()
  plt.savefig("histogram.png")
  
  region_indices = {0: [560, 3000],
                    1: [1420, 3000],
                    2: [2240, 3000],
                    3: [3040, 3020],
                    4: [3860, 3020],
                    5: [4680, 3020]
                    }
  raw_values = {0:[], 1:[], 2:[], 3:[]}
  for k, pt in region_indices.items():
    _im = im[pt[1]:pt[1]+400, pt[0]:pt[0]+400]
    image = { 0: _im[0:400:2, 0:400:2],
              1: _im[0:400:2, 1:400:2],
              2: _im[1:400:2, 1:400:2],
              3: _im[1:400:2, 0:400:2]}
    for ch in range(4):
      #print(f'channel {ch+1} description {raw.color_desc[ch]}')
      channel_values = image[ch]
      mean_value = np.mean(channel_values)
      std_value = np.std(channel_values)
      max_value = np.max(channel_values)
      min_value = np.min(channel_values)
      print(f"{k} Channel {ch}: Mean={mean_value}, {std_value} Max={max_value}, Min={min_value}")
      raw_values[ch].append(mean_value)
  fig, ax = plt.subplots(1, 1)
  for ch in range(4):
    ax.plot(raw_values[ch], '.')
  ax.set_yscale('log')
  fig.savefig('gray.png')
    
"""
604, 3524
953, 3069

1411, 3525
1820, 3000

2240, 3516
2680, 3044

3040, 3480
3440, 3080

3860, 3500
4300, 3020

4680, 3513
5080, 3020
"""

