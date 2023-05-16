---
title: "txt2img()"
slug: "txt2img"
excerpt: "Full info about txt2img method"
hidden: false
createdAt: "2023-05-16T13:21:22.195Z"
updatedAt: "2023-05-16T15:19:31.835Z"
---
# Description

This is a method for generating images from text prompt and other parameters(check arguments)

# Arguments

1. prompt:str 
2. negative_prompt:str
3. model:str check all available models on `Models and samplers` page
4. sampler:str check all available samplers on `Models and samplers` page
5. aspect_ratio:str "square" or "landscape" or "portrait"
6. steps:int from 1 to 50
7. cfg_scale:int from 1 to 20
8. seed:int leave -1(default) for random
9. upscale:bool Enable/Disable 2xUpscaling

# Asynchronous usage

For asynchronous usage(inside async functions) use `arunv1()` method, it have same arguments as `txt2image()`

How to use `arunv1()` - check `Methods` page