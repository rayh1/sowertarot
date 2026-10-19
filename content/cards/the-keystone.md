---
title: "The Keystone"
concept: "essential element that locks a whole together"
key_terms: ["keystone", "arch", "apex", "span", "integration", "voussoir"]
created: "2026-09-20"
seed: 450459341
image_status: "present"
prompt_status: "original"
image: "card_the-keystone.png"
clip: "the-keystone_code_v2.mp4"
joplin_note: "6db1564af0c94d3098f5eb03ccae551a"
---

# The Keystone

*An original tarot card in the Rider-Waite tradition*

![The Keystone](/media/card_the-keystone.png)

## Visual Description

### Composition
A tall unfinished arch of dressed grey stone fills the card. At its crown a wedge-shaped golden keystone has just been set, and a thin trail of stone dust falls from it down the open archway. Below, a mason in a leather apron and rolled-up linen shirt kneels at a low wooden bench, shaping stone. Through the arch a pale city lies on the horizon under a soft cream sky.

### Symbolism
The keystone is the one essential piece that bears the load and completes the whole. The falling dust marks the instant it locks into place. The mason working on below shows that the work which makes completion possible is humble and unseen.

### Atmosphere
Still morning air, hushed and reverent, the quiet just after long labour is completed.

## Archetypal Essence

The Keystone is the principle that a whole stands or falls on its one essential element — the piece that, once set, transfers every load into strength and turns separate parts into a single span. It speaks to integration: the moment scattered efforts, values, or people are locked together by the one thing that was missing. Its truth is that completion is not addition but alignment — the final stone adds no bulk, only coherence. To hold the keystone is to carry responsibility for what makes everything else hold.

## Render Prompt

```
Close view of the top of a great unfinished arch of dressed grey stone: its two curving halves rise in from the left and right edges of the card and stop just short of each other, leaving one narrow wedge-shaped gap at the top centre. A mason in a leather apron and a rolled-up linen shirt kneels on a plank scaffold right beside the gap and, with both hands, sets a wedge-shaped golden keystone down into it. A little stone dust falls from its edges. Far below, rough unworked boulders lie at the arch's feet. An even, overcast sky of soft cream and pale gold clouds fills the background. Hushed, reverent mood, the instant the arch locks into place.
```

## Render Record

<details>
<summary>Seed 450459341 · tarot_flux_final_01497_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-04T19:54:15+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01497_.png`
- Seed: 450459341
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-04T19:54:15+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01497_.png",
  "seed": 450459341,
  "title": "The Keystone",
  "scene": "Close view of the top of a great unfinished arch of dressed grey stone: its two curving halves rise in from the left and right edges of the card and stop just short of each other, leaving one narrow wedge-shaped gap at the top centre. A mason in a leather apron and a rolled-up linen shirt kneels on a plank scaffold right beside the gap and, with both hands, sets a wedge-shaped golden keystone down into it. A little stone dust falls from its edges. Far below, rough unworked boulders lie at the arch's feet. An even, overcast sky of soft cream and pale gold clouds fills the background. Hushed, reverent mood, the instant the arch locks into place.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nClose view of the top of a great unfinished arch of dressed grey stone: its two curving halves rise in from the left and right edges of the card and stop just short of each other, leaving one narrow wedge-shaped gap at the top centre. A mason in a leather apron and a rolled-up linen shirt kneels on a plank scaffold right beside the gap and, with both hands, sets a wedge-shaped golden keystone down into it. A little stone dust falls from its edges. Far below, rough unworked boulders lie at the arch's feet. An even, overcast sky of soft cream and pale gold clouds fills the background. Hushed, reverent mood, the instant the arch locks into place.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nClose view of the top of a great unfinished arch of dressed grey stone: its two curving halves rise in from the left and right edges of the card and stop just short of each other, leaving one narrow wedge-shaped gap at the top centre. A mason in a leather apron and a rolled-up linen shirt kneels on a plank scaffold right beside the gap and, with both hands, sets a wedge-shaped golden keystone down into it. A little stone dust falls from its edges. Far below, rough unworked boulders lie at the arch's feet. An even, overcast sky of soft cream and pale gold clouds fills the background. Hushed, reverent mood, the instant the arch locks into place.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 450459341,
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
  }
}
```

</details>
