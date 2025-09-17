<div align="center">

# Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images


<font size="4">
Simon Niedermayr &emsp; Christoph Neuhauser  &emsp; Rüdiger Westermann
</font>
<br>

<font size="4">
 Technical University of Munich 
</font>

<a href="https://keksboter.github.io/upscale3dgs/">Webpage</a> | <a href="https://arxiv.org/abs/2503.14171">arXiv</a> 

<img src="docs/static/img/teaser_project_page.svg" alt="Rendering Pipeline"/>
</div>

## Abstract
We introduce an image upscaling technique tailored for 3D Gaussian Splatting (3DGS) on lightweight GPUs. Compared to 3DGS, it achieves significantly higher rendering speeds and reduces artifacts commonly observed in 3DGS reconstructions. Our technique upscales low-resolution 3DGS renderings with a marginal increase in cost by directly leveraging the analytical image gradients of Gaussians for gradient-based bicubic spline interpolation. The technique is agnostic to the specific 3DGS implementation, achieving novel view synthesis at rates 3x-4x higher than the baseline implementation. Through extensive experiments on multiple datasets, we showcase the performance improvements and high reconstruction fidelity attainable with gradient-aware upscaling of 3DGS images. We further demonstrate the integration of gradient-aware upscaling into the gradient-based optimization of a 3DGS model and analyze its effects on reconstruction quality and performance. 

## Citation
If you find our work useful, please cite:
```
@misc{niedermayr2025upscaling3dgs,
    title={Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images}, 
    author={Simon Niedermayr and Christoph Neuhauser Rüdiger Westermann},
    year={2025},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    year = {2025},
}
```

## Code
Coming soon...