import cv2
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Bad command line argument! \nProvide the mage path as the only argument")
    exit()
imagePath = sys.argv[1]
image = cv2.imread(imagePath)
colorNames = {"b":"Blue", "g":"Green", "r":"Red"}
figure, axis = plt.subplots(2,2,figsize=(12, 10))
plt.title("All channels combined")
plt.xlabel("Strenght of pixel")
plt.ylabel("Number of pixels")
for (channel, color, location) in zip(cv2.split(image), ["b", "g", "r"],[(0,0),(0,1),(1,0)]):
    hist = cv2.calcHist([channel], [0], None, [256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])
    x, y = location
    axis[x, y].plot(hist, color=color)
    axis[x,y].set_xlabel('Strength of pixel')
    axis[x,y].set_ylabel("Number of pixels")
    axis[x,y].set_xlim([0,256])
    axis[x,y].set_title(f"Color: {colorNames[color]}")
figure.tight_layout(pad=2.0)
plt.show()
