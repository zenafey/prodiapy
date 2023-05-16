---
title: "img2img()"
slug: "img2img"
excerpt: "Full info about img2img() method"
hidden: false
createdAt: "2023-05-16T13:43:07.066Z"
updatedAt: "2023-05-16T15:19:22.111Z"
---
# Description

This is a method for generating images with using another image



# Arguments

1. imageUrl:str URL of image that you want to use as initial
2. model:str check all available models on `Models and samplers` page
3. prompt:str describe new picture
4. denoising_strength:float default is 0.7
5. negative_prompt:str
6. steps:int from 1 to 50
7. scale:int from 1 to 20
8. seed:int leave -1(default) to use random
9. upscale:bool Enable/Disable 2xUpscaling
10. sampler:str check all available samplers on `Models and samplers` page