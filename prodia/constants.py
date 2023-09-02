
class Endpoint:
    base = "https://api.prodia.com/v1"
    sdxlGenerate = base + "/sdxl/generate"
    sdGenerate = base + "/sd/generate"
    sdTransform = base + "/sd/transform"
    sdControl = base + "/sd/controlnet"
    retrieve = base + "/job/"
    models = base + "/models/list"
 
class SdxlModel:
    BASE_1_0 = "sd_xl_base_1.0.safetensors [be9edd61]"
    DREAMSHAPER_ALPHA2 =  "dreamshaperXL10_alpha2.safetensors [c8afe2ef]"
    DYNAVISION = "dynavisionXL_0411.safetensors [c39cc051]"

class SdModel:
    ABSOLUTE_R_V16 = "absolutereality_V16.safetensors [37db0fc3]"
    ABSOLUTE_R_V181 = "absolutereality_v181.safetensors [3d9d4d2b]"
    ANALOG = "analog-diffusion-1.0.ckpt [9ca13f02]"
    ANYTHING_V3 = "anythingv3_0-pruned.ckpt [2700c435]"
    ANYTHING_V4_5 = "anything-v4.5-pruned.ckpt [65745d25]"
    ANYTHING_V5 = "anythingV5_PrtRE.safetensors [893e49b9]"
    AOM3 = "AOM3A3_orangemixs.safetensors [9600da17]"
    CHILDRENSSTORIES_V13D = "childrensStories_v13D.safetensors [9dfaabcb]"
    CHILDRENSSTORIES_V1SEMIR = "childrensStories_v1SemiReal.safetensors [a1c56dbb]"
    CHILDRENSSTORIES_V1TOONANIME = "childrensStories_v1ToonAnime.safetensors [2ec7b88b]"
    CYBERREALISTIC_V33 = "cyberrealistic_v33.safetensors [82b0d085]"
    DELIBERATE_V2 = "deliberate_v2.safetensors [10ec4b29]"
    DREAMLIKE_ANIME_1 = "dreamlike-anime-1.0.safetensors [4520e090]"
    DREAMLIKE_DIFFUSION_1 = "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]"
    DREAMLIKE_PHOTOREAL_2 = "dreamlike-photoreal-2.0.safetensors [fdcf65e7]"
    DREAMSHAPER_6 = "dreamshaper_6BakedVae.safetensors [114c8abb]"
    DREAMSHAPER_7 = "dreamshaper_7.safetensors [5cf5ae06]"
    DREAMSHAPER_8 = "dreamshaper_8.safetensors [9d40847d]"
    EORV20 = "edgeOfRealism_eorV20.safetensors [3ed5de15]"
    EIMISANIMEDIFFUSION_V1 = "EimisAnimeDiffusion_V1.ckpt [4f828a15]"
    ELLDRETHS_VIVID_MIX = "elldreths-vivid-mix.safetensors [342d9d26]"
    EPICREALISM_NATURALSINRC1VAE = "epicrealism_naturalSinRC1VAE.safetensors [90a4c676]"
    ICBPIAP = "ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]"
    JUGGERNAUT_AFTERMATH = "juggernaut_aftermath.safetensors [5e20c455]"
    LYRIEL_V16 = "lyriel_v16.safetensors [68fceea2]"
    MECHAMIX_V10 = "mechamix_v10.safetensors [ee685731]"
    MEINAV9 = "meinamix_meinaV9.safetensors [2ec66ab0]"
    MEINAV11 = "meinamix_meinaV11.safetensors [b56ce717]"
    OPENJOURNEY_V4 = "openjourney_V4.ckpt [ca2f377f]"
    PORTRAITPLUS_V1 = "portraitplus_V1.0.safetensors [1400e684]"
    REALISTIC_VIS_V1_4 = "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]"
    REALISTIC_VIS_V2_0 = "Realistic_Vision_V2.0.safetensors [79587710]"
    REALISTIC_VIS_V4_0 = "Realistic_Vision_V4.0.safetensors [29a7afaa]"
    REALISTIC_VIS_V5_0 = "Realistic_Vision_V5.0.safetensors [614d1063]"
    REDSHIFT_V10 = "redshift_diffusion-V10.safetensors [1400e684]"
    REVANIMATED_V122 = "revAnimated_v122.safetensors [3f4fefd9]"
    RUNDIFFUSIONFX25D_V10 = "rundiffusionFX25D_v10.safetensors [cd12b0ee]"
    RUNDIFFUSIONFX_V10 = "rundiffusionFX_v10.safetensors [cd4e694d]"
    SDV1_4 = "sdv1_4.ckpt [7460a6fa]"
    SDV1_5 = "v1-5-pruned-emaonly.safetensors [d7049739]"
    SHONINSBEAUTIFUL_V10 = "shoninsBeautiful_v10.safetensors [25d8c546]"
    THEALLYS = "theallys-mix-ii-churned.safetensors [5d9225a4]"
    TIMELESS_1 = "timeless-1.0.ckpt [7c4971d4]"
    TOONYOU_6 = "toonyou_beta6.safetensors [980f6b15]"


class Sampler:
    EULER = "Euler"
    EULER_A = "Euler a"
    HEUN = "Heun"
    DPM_2M_KARRAS = "DPM++ 2M Karras"
    DPM_SDE_KARRAS = 'DPM++ SDE Karras'
    DDIM = "DDIM"


class ControlModels:
    CANNY = "control_v11p_sd15_canny [d14c016b]"
    OPENPOSE = "control_v11p_sd15_openpose [cab727d4]"
    SOFTEDGE = "control_v11p_sd15_softedge [a8575a2a]"
    SCRIBBLE = "control_v11p_sd15_scribble [d4ba51ff]"



