---
title: "The Ferryman"
concept: "passage entrusted to another between states"
key_terms: ["ferryman", "ferry", "crossing", "river", "boatman", "passage"]
created: "2026-09-21"
seed: 51015
image_status: "present"
prompt_status: "original"
image: "card_the-ferryman.png"
clip: "the-ferryman_code_v4.mp4"
joplin_note: "a0c4955c6d364779a979c9a75b8e4153"
---

# The Ferryman

*An original tarot card in the Rider-Waite tradition*

![The Ferryman](/media/card_the-ferryman.png)

## Visual Description

### Composition
A hooded ferryman stands at the stern of a long flat wooden boat, poling across a wide, still river at dusk. The near bank is thick with tall reeds; the far shore shows low hills and a pale rising moon. The boat is centered, moving from the viewer's bank toward the far one; the water is glassy and calm.

### Symbolism
The still water is the threshold between one state and the next. The pole in another's hands marks passage entrusted to a guide rather than taken alone. A single coin resting on the gunwale is the fare — the price every crossing asks. The reeds are the liminal edge; dusk is the hour of transition; the far bank, half-seen, is the unknown destination.

### Atmosphere
Hushed dusk, mist lying low on the water, the air still and cool. Solemn, calm, and weighted — the quiet of a passage underway.

## Archetypal Essence

The Ferryman is passage that must be entrusted to another — the crossing you cannot make alone, where you set down the oar and let a steady hand carry you between one shore and the next. It speaks to transitions taken on faith: grief, upheaval, the movement from a known life into an unknown one. Its truth is that some thresholds are not doors you open but waters you are carried across, and that to arrive you must first let go of the bank.

## Render Prompt

```
A hooded ferryman stands poling a long flat wooden boat across a wide still river at dusk, mist lying low on the glassy water, tall reeds along the near bank, a single coin resting on the boat's edge, a pale moon rising over low hills on the far shore. The figure is calm and solemn, the boat moving from the near bank toward the far one.
```

## Render Record

<details>
<summary>Seed 51015 · tarot_flux_final_00030_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`. The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00030_.png`
- Seed: 51015
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00030_.png, matched to the attached image by pixel comparison (mean difference 1.0 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00031_.png at 53.3). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00030_.png",
  "seed": 51015,
  "title": "The Ferryman",
  "scene": "A hooded ferryman stands poling a long flat wooden boat across a wide still river at dusk, mist lying low on the glassy water, tall reeds along the near bank, a single coin resting on the boat's edge, a pale moon rising over low hills on the far shore. The figure is calm and solemn, the boat moving from the near bank toward the far one.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA hooded ferryman stands poling a long flat wooden boat across a wide still river at dusk, mist lying low on the glassy water, tall reeds along the near bank, a single coin resting on the boat's edge, a pale moon rising over low hills on the far shore. The figure is calm and solemn, the boat moving from the near bank toward the far one.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA hooded ferryman stands poling a long flat wooden boat across a wide still river at dusk, mist lying low on the glassy water, tall reeds along the near bank, a single coin resting on the boat's edge, a pale moon rising over low hills on the far shore. The figure is calm and solemn, the boat moving from the near bank toward the far one.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 51015,
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
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00030_.png, matched to the attached image by pixel comparison (mean difference 1.0 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00031_.png at 53.3). Render date unknown."
}
```

</details>
