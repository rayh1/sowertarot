---
title: "The Miner"
concept: "Costly descent to bring up hidden worth"
key_terms: ["miner", "ore", "tailings", "extraction", "descent", "lamp"]
created: "2026-10-15"
seed: 597539018
image_status: "present"
prompt_status: "original"
image: "card_the-miner.png"
clip: "the-miner_code_v1.mp4"
joplin_note: "c7b5cc8ddd3f46deaa1d98dc9b41580a"
---

# The Miner

*An original tarot card in the Rider-Waite tradition*

![The Miner](/media/card_the-miner.png)

## Visual Description

### Composition

A miner kneels in a tunnel of rough dark rock and holds a fist-sized lump of ore close to his face, turning it in the light of a small oil lamp that stands on the floor beside him. Flecks of gold glint in the ore. He is broad-shouldered and bare-headed, with short brown hair and a short beard, in a long belted tunic of rough orange cloth. A short iron pick lies on the floor near the lamp. Behind him a heap of broken grey rock lies along the tunnel floor. Heavy timber props hold up the rock ceiling, and beyond the lamplight the passage fades into deep shadow. There is no sky: the whole card lies below ground.

### Symbolism

The small lamp is the only light carried into the dark: the attention that makes finding possible, as in the alchemists' motto VITRIOL, "visit the interior of the earth, and by purifying you will find the hidden stone." The ore held up before his eyes is the worth found, and the gesture of taking: lifted out of the rock, it will never grow back. The heap of broken rock is the cost, since most of what is dug out is waste. The timber props hold back the weight above, a risk kept at bay rather than removed. The pick at rest marks the work already done; kneeling marks both labour and descent. The missing sky sets this card against The Sower, who works in open light, and against The Root, whose cross-section still keeps the world above in view.

### Atmosphere

Deep underground, outside of day and night. Close, still and heavy, with the quiet of held breath. Warm amber lamplight falls on the miner's face, hands and the ore; everything beyond it sinks into dark brown shadow.

## Archetypal Essence

The Miner is the one who goes down into the dark to bring up what the surface will not give. Every gain is wrested from rock and paid for in labour, risk and a great heap of waste, and what he carries up must still be refined before it is worth anything. Where the Sower gives seed to the light and waits, the Miner takes from a store that will not grow back, and the descent is also inward: what lies hidden is worth finding only once it is brought into the light. The card asks what you are digging for, what the digging costs, and whether you can tell the ore from the rock around it.

## Render Prompt

```
A miner kneels at the dead end of a low tunnel, side-on to the working face of rough dark rock, and holds a rough, jagged lump of grey ore flecked with gold close to his face, turning it in the light. A small open oil lamp of plain reddish clay, a shallow dish with a pinched spout and a single small flame, stands on the tunnel floor beside his knee. He is broad-shouldered and bare-headed, with short dark hair and a short dark beard, and wears a long-sleeved knee-length tunic of rough brown wool belted with a rope, the sleeves pushed up to the elbow. A short iron pick with a wooden haft lies on the floor beside the lamp. Behind him a heap of broken grey rock lies against the tunnel wall. The rough rock face fills the background behind and beside him, heavy rough-hewn timber props hold up the low rock ceiling across the top of the picture, and the far side of the picture is solid rock wall in deep brown shadow. Warm amber lamplight from below on his face, hands, the ore and the rock face. Close, still and heavy.
```

<!-- DALL-E fallback: add a "## DALL-E Prompt" fenced block here ONLY when taking the External-render fallback -->

## Render Record

<details>
<summary>Seed 597539018 · tarot_flux_final_01685_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-16T13:57:38+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01685_.png`
- Seed: 597539018
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-16T13:57:38+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01685_.png",
  "seed": 597539018,
  "title": "The Miner",
  "scene": "A miner kneels at the dead end of a low tunnel, side-on to the working face of rough dark rock, and holds a rough, jagged lump of grey ore flecked with gold close to his face, turning it in the light. A small open oil lamp of plain reddish clay, a shallow dish with a pinched spout and a single small flame, stands on the tunnel floor beside his knee. He is broad-shouldered and bare-headed, with short dark hair and a short dark beard, and wears a long-sleeved knee-length tunic of rough brown wool belted with a rope, the sleeves pushed up to the elbow. A short iron pick with a wooden haft lies on the floor beside the lamp. Behind him a heap of broken grey rock lies against the tunnel wall. The rough rock face fills the background behind and beside him, heavy rough-hewn timber props hold up the low rock ceiling across the top of the picture, and the far side of the picture is solid rock wall in deep brown shadow. Warm amber lamplight from below on his face, hands, the ore and the rock face. Close, still and heavy.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA miner kneels at the dead end of a low tunnel, side-on to the working face of rough dark rock, and holds a rough, jagged lump of grey ore flecked with gold close to his face, turning it in the light. A small open oil lamp of plain reddish clay, a shallow dish with a pinched spout and a single small flame, stands on the tunnel floor beside his knee. He is broad-shouldered and bare-headed, with short dark hair and a short dark beard, and wears a long-sleeved knee-length tunic of rough brown wool belted with a rope, the sleeves pushed up to the elbow. A short iron pick with a wooden haft lies on the floor beside the lamp. Behind him a heap of broken grey rock lies against the tunnel wall. The rough rock face fills the background behind and beside him, heavy rough-hewn timber props hold up the low rock ceiling across the top of the picture, and the far side of the picture is solid rock wall in deep brown shadow. Warm amber lamplight from below on his face, hands, the ore and the rock face. Close, still and heavy.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA miner kneels at the dead end of a low tunnel, side-on to the working face of rough dark rock, and holds a rough, jagged lump of grey ore flecked with gold close to his face, turning it in the light. A small open oil lamp of plain reddish clay, a shallow dish with a pinched spout and a single small flame, stands on the tunnel floor beside his knee. He is broad-shouldered and bare-headed, with short dark hair and a short dark beard, and wears a long-sleeved knee-length tunic of rough brown wool belted with a rope, the sleeves pushed up to the elbow. A short iron pick with a wooden haft lies on the floor beside the lamp. Behind him a heap of broken grey rock lies against the tunnel wall. The rough rock face fills the background behind and beside him, heavy rough-hewn timber props hold up the low rock ceiling across the top of the picture, and the far side of the picture is solid rock wall in deep brown shadow. Warm amber lamplight from below on his face, hands, the ore and the rock face. Close, still and heavy.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 597539018,
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
