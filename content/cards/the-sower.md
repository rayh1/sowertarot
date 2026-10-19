---
title: "The Sower"
concept: "committing effort to an unseen future"
key_terms: ["sower", "seed", "sowing", "furrow", "planting", "potential"]
created: "2026-09-20"
seed: 628318
image_status: "present"
prompt_status: "original"
image: "card_the-sower.png"
clip: "the-sower_code_v2.mp4"
joplin_note: "c820533f03e4468990f476f74fd97c3d"
---

# The Sower

*An original tarot card in the Rider-Waite tradition*

![The Sower](/media/card_the-sower.png)

## Visual Description

### Composition
A lone figure strides across a freshly tilled field at dawn, one arm swept wide mid-cast, scattering an arc of golden seed through the air. Deep plowed furrows recede toward a low horizon. A single bare tree stands at the field's edge; birds wheel overhead. The figure is centered and dynamic, caught mid-stride.

### Symbolism
The golden seed is potential — faith in an unseen future harvest. The open furrows are prepared, receptive ground. The wide-armed gesture is generosity: casting without control over where each seed lands. A few seeds fall on stony ground at the path's edge — not all will take root. Dawn marks a beginning; the wheeling birds are chance and risk. Earthy palette: tilled umber soil, sage field, gold seed, pale dawn.

### Atmosphere
Cool dawn air, dew on the furrows, quiet and purposeful labor. Hope tempered by uncertainty under a wide open sky.

## Archetypal Essence

The Sower is the act of committing effort to an unknown future — casting what you have across ground you cannot control, trusting that some of it will take. It is faith expressed as work: the seed must leave the hand before any harvest is possible, and not every seed will grow. Its truth is that creation begins with a generous, irreversible release, and that we sow in one season what we reap in another.

## Render Prompt

```
A lone farmer strides across a freshly tilled field at dawn, one arm swept wide mid-cast, scattering a wide arc of glowing golden seed through the cool air. Deep plowed furrows recede toward a low horizon under a pale dawn sky. A single bare tree stands at the field's edge; a few birds wheel overhead; a scatter of seed falls on stony ground near the path. The figure is centered and caught mid-stride, purposeful and generous.
```

## Render Record

<details>
<summary>Seed 628318 · tarot_flux_final_00033_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`. The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00033_.png`
- Seed: 628318
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00033_.png, matched to the attached image by pixel comparison (mean difference 1.2 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00028_.png at 1.7). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00033_.png",
  "seed": 628318,
  "title": "The Sower",
  "scene": "A lone farmer strides across a freshly tilled field at dawn, one arm swept wide mid-cast, scattering a wide arc of glowing golden seed through the cool air. Deep plowed furrows recede toward a low horizon under a pale dawn sky. A single bare tree stands at the field's edge; a few birds wheel overhead. The figure is centered and caught mid-stride, purposeful and generous.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA lone farmer strides across a freshly tilled field at dawn, one arm swept wide mid-cast, scattering a wide arc of glowing golden seed through the cool air. Deep plowed furrows recede toward a low horizon under a pale dawn sky. A single bare tree stands at the field's edge; a few birds wheel overhead. The figure is centered and caught mid-stride, purposeful and generous.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
  "frame_flags": [
    "--art-crop",
    "0.035",
    "--paper",
    "216,199,158",
    "--ink",
    "26,22,18",
    "--margin-frac",
    "0.020",
    "--border-frac",
    "0.008",
    "--banner-frac",
    "0.085"
  ],
  "workflow": {
    "4445667083308169": {
      "inputs": {
        "ckpt_name": "flux1-dev-fp8.safetensors"
      },
      "class_type": "CheckpointLoaderSimple",
      "_meta": {
        "title": "Load Checkpoint"
      }
    },
    "3988400399187937": {
      "inputs": {
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA lone farmer strides across a freshly tilled field at dawn, one arm swept wide mid-cast, scattering a wide arc of glowing golden seed through the cool air. Deep plowed furrows recede toward a low horizon under a pale dawn sky. A single bare tree stands at the field's edge; a few birds wheel overhead. The figure is centered and caught mid-stride, purposeful and generous.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
        "clip": [
          "2708406073710926",
          1
        ]
      },
      "class_type": "CLIPTextEncode",
      "_meta": {
        "title": "CLIP Text Encode (Prompt)"
      }
    },
    "3351178248307577": {
      "inputs": {
        "guidance": 3.5,
        "conditioning": [
          "3988400399187937",
          0
        ]
      },
      "class_type": "FluxGuidance",
      "_meta": {
        "title": "FluxGuidance"
      }
    },
    "3966392173087885": {
      "inputs": {
        "conditioning": [
          "3988400399187937",
          0
        ]
      },
      "class_type": "ConditioningZeroOut",
      "_meta": {
        "title": "Conditioning Zero Out"
      }
    },
    "2149758162015531": {
      "inputs": {
        "width": 896,
        "height": 1536,
        "batch_size": 1
      },
      "class_type": "EmptySD3LatentImage",
      "_meta": {
        "title": "EmptySD3LatentImage"
      }
    },
    "502708169065303": {
      "inputs": {
        "seed": 628318,
        "steps": 20,
        "cfg": 1.0,
        "sampler_name": "euler",
        "scheduler": "simple",
        "denoise": 1.0,
        "model": [
          "2708406073710926",
          0
        ],
        "positive": [
          "3351178248307577",
          0
        ],
        "negative": [
          "3966392173087885",
          0
        ],
        "latent_image": [
          "2149758162015531",
          0
        ]
      },
      "class_type": "KSampler",
      "_meta": {
        "title": "KSampler"
      }
    },
    "1617950119549939": {
      "inputs": {
        "samples": [
          "502708169065303",
          0
        ],
        "vae": [
          "4445667083308169",
          2
        ]
      },
      "class_type": "VAEDecode",
      "_meta": {
        "title": "VAE Decode"
      }
    },
    "3880964665895773": {
      "inputs": {
        "filename_prefix": "tarot_flux",
        "images": [
          "1617950119549939",
          0
        ]
      },
      "class_type": "SaveImage",
      "_meta": {
        "title": "Save Image"
      }
    },
    "1279432504611721": {
      "inputs": {
        "model_name": "4x-UltraSharp.pth"
      },
      "class_type": "UpscaleModelLoader",
      "_meta": {
        "title": "Load Upscale Model"
      }
    },
    "1107469044429072": {
      "inputs": {
        "upscale_model": [
          "1279432504611721",
          0
        ],
        "image": [
          "1617950119549939",
          0
        ]
      },
      "class_type": "ImageUpscaleWithModel",
      "_meta": {
        "title": "Upscale Image (using Model)"
      }
    },
    "2411597916599562": {
      "inputs": {
        "upscale_method": "nearest-exact",
        "width": 1024,
        "height": 1792,
        "crop": "center",
        "image": [
          "1107469044429072",
          0
        ]
      },
      "class_type": "ImageScale",
      "_meta": {
        "title": "Upscale Image"
      }
    },
    "3886908355529710": {
      "inputs": {
        "filename_prefix": "tarot_flux_final",
        "images": [
          "2411597916599562",
          0
        ]
      },
      "class_type": "SaveImage",
      "_meta": {
        "title": "Save Image"
      }
    },
    "2708406073710926": {
      "inputs": {
        "lora_name": "sowtarot_woodcut-v1.safetensors",
        "strength_model": 1.0,
        "strength_clip": 1.0,
        "model": [
          "4445667083308169",
          0
        ],
        "clip": [
          "4445667083308169",
          1
        ]
      },
      "class_type": "LoraLoader",
      "_meta": {
        "title": "Load LoRA (Model and CLIP)"
      }
    }
  },
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00033_.png, matched to the attached image by pixel comparison (mean difference 1.2 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00028_.png at 1.7). Render date unknown."
}
```

</details>
