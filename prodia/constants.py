from enum import Enum

class Endpoint:
    base = "https://api.prodia.com/v1"
    txt2img = base + "/job"
    img2img = base + "/transform"
    controlnet = base + "/controlnet"
    retrieve = base + "/job/{}"
    models = base + "/models/list"


class Model(Enum):
    ABSOLUTE_R = ("absolutereality_V16.safetensors [37db0fc3]", 'Absolute Reality V1.6')
    ANALOG = ("analog-diffusion-1.0.ckpt [9ca13f02]", "Analog V1")
    ANYTHING_V3 = ("anythingv3_0-pruned.ckpt [2700c435]", "Anything V3")
    ANYTHING_V4 = ("anything-v4.5-pruned.ckpt [65745d25]", "Anything V4.5")
    ANYTHING_V5 = ("anythingV5_PrtRE.safetensors [893e49b9]", 'Anything V5')
    ABYSSORANGEMIX = ("AOM3A3_orangemixs.safetensors [9600da17]", "AbyssOrangeMix V3")
    DELIBERATE = ("deliberate_v2.safetensors [10ec4b29]", "Deliberate V2")
    DREAMLIKE_V1 = ("dreamlike-diffusion-1.0.safetensors [5c9fd6e0]", "Dreamlike Diffusion V1")
    DREAMLIKE_V2 = ("dreamlike-diffusion-2.0.safetensors [fdcf65e7]", "Dreamlike Diffusion V2")
    DREAMSHAPER_6 = ("dreamshaper_6BakedVae.safetensors [114c8abb]", "Dreamshaper 6 baked vae")
    DREAMSHAPER_7 = ("dreamshaper_7.safetensors [5cf5ae06]", 'Dreamshaper 7')
    DREAMSHAPER_8 = ("dreamshaper_8.safetensors [9d40847d]", 'Dreamshaper 8')
    EIMISANIME = ("EimisAnimeDiffusion_V1.ckpt [4f828a15]", 'Eimis Anime V1')
    ELLDRETHVIVIDMIX = ("elldreths-vivid-mix.safetensors [342d9d26]", "Elldreth's Vivid")
    LYRIEL_V16 = ("lyriel_v16.safetensors [68fceea2]", "Lyriel V1.6")
    MECHAMIX = ("mechamix_v10.safetensors [ee685731]", "MechaMix V1.0")
    MEINAMIX_V9 = ("meinamix_meinaV9.safetensors [2ec66ab0]", "MeinaMix V9")
    MEINAMIX_V11 = ("meinamix_meinaV11.safetensors [b56ce717]", 'MeinaMix V11')
    OPENJOURNEY = ("openjourney_V4.ckpt [ca2f377f]", "Openjourney V4")
    PORTRAIT = ("portraitplus_V1.0.safetensors [1400e684]", "Portrait+ V1")
    REALISTICVS_V14 = ("Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]", "Realistic Vision V1.4")
    REALISTICVS_V40 = ("Realistic_Vision_V4.0.safetensors [29a7afaa]", "Realistic Vision V4.0")
    REALISTICVS_V50 = ("Realistic_Vision_V5.0.safetensors [614d1063]", "Realistic Vision V5.0")
    REDSHIFT = ("redshift_diffusion-V10.safetensors [1400e684]", "Redshift V1")
    REV_ANIMATED = ("revAnimated_v122.safetensors [3f4fefd9]", "ReV Animated V1.2.2")
    SD_V14 = ("sdv1_4.ckpt [7460a6fa]", "Stable Diffusion V1.4", "21")
    SD_V15 = ("v1-5-pruned-emaonly.ckpt [81761151]", "Stable Diffusion V1.5", "22")
    SBP = ("shoninsBeautiful_v10.safetensors [25d8c546]", "Shonin's Beautiful People V1.0", "23")
    THEALLYSMIX = ("theallys-mix-ii-churned.safetensors [5d9225a4]", "TheAlly's Mix II", "24")
    TIMELESS = ("timeless-1.0.ckpt [7c4971d4]", "Timeless V1", "25")


class Sampler(Enum):
    EULER = "Euler"
    EULER_A = "Euler a"
    HEUN = "Heun"
    DPM_2M_KARRAS = "DPM++ 2M Karras"
    DPM_SDE_KARRAS = 'DPM++ SDE Karras'
    DDIM = "DDIM"


class Control(Enum):
    SOFT_EDGE = ("control_v11p_sd15_softedge [a8575a2a]", 'Soft Edge')
    SCRIBBLE = ("control_v11p_sd15_scribble [d4ba51ff]", 'Scribble')
