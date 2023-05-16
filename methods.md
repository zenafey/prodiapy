---
title: "Methods"
slug: "methods"
excerpt: "Here is full list of available methods and link to them"
hidden: false
createdAt: "2023-05-16T13:21:13.008Z"
updatedAt: "2023-05-16T15:22:40.990Z"
---
# Authorization

Before starting creating images, obtain your api key on [Prodia API page](https://docs.prodia.com/reference/getting-started)

Now, you need to define api key in you script, to do this user `prodia.Client()`:

```python
import prodia

prodia.Client(api_key="paste here your api key")

#...
```

# Normal mode

> 🚧 This is a list with generating methods that is not `asynchronous` and blocks script until completing generation

## txt2img generation

```python txt2img example
image = prodia.txt2img(prompt="kittens on cloud") 
```

## img2img generation

```python img2img example
image = prodia.img2img(
  imageUrl='https://cdn.discordapp.com/attachments/1083332256493482014/1107954523881873459/6AAE9DB9.png',
  prompt="photo of dog"
)  #imageUrl and prompt are required arguments
```

# Asynchronous

> 🚧 This is a list of generating methods that is  `asynchronous` and work only inside  `asynchronous` function

## arunv1 generation(async text to image)

```python arunv1 example
async def test():
#...
	image = await prodia.arunv1(prompt="kittens on cloud")
```

## arunv2 generation(async image to image)

```python arunv2 example
async def test():
#...
	image = await prodia.arunv2(
  imageUrl="https://cdn.discordapp.com/attachments/1083332256493482014/1107954523881873459/6AAE9DB9.png",
  prompt="photo of dog"
)
```

> 📘 Note that all methods(at the moment) returns url of generated image