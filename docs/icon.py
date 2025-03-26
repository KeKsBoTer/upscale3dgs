# %%
import os
import torch
from matplotlib import pyplot as plt
import seaborn as sns
from PIL import Image, ImageDraw, ImageFilter

def gaussian(pos):
    dg_dx =-2*pos[:,0]
    dg_dy =-2*pos[:,1]
    dg_dxy = 0
    return (dg_dx * dg_dy+ dg_dxy) *torch.exp(-pos[:,0]**2 - pos[:,1]**2)

res = 256
x = torch.linspace(-2.5, 2.5, res)
y = torch.linspace(-2.5, 2.5, res)
pos = torch.stack(torch.meshgrid(x, y), -1).reshape(-1, 2)
z = gaussian(pos).reshape(res, res)
z_n = (z - z.min()) / (z.max() - z.min())
img = sns.cm.icefire(z_n)
# Convert img to PIL Image
img_pil = Image.fromarray((img * 255).astype('uint8'))

# Create a mask for rounded corners
mask = Image.new("L", img_pil.size, 0)
draw = ImageDraw.Draw(mask)
corner_radius = 50
draw.rounded_rectangle((0, 0, img_pil.size[0]-1, img_pil.size[1]-1), corner_radius, fill=255)

# Apply a Gaussian blur to the mask
mask = mask.filter(ImageFilter.GaussianBlur(1))
# Apply the mask to add rounded corners
img_pil.putalpha(mask)
img_pil.save(os.path.join(os.path.dirname(__file__),"static/img/icon.png"))