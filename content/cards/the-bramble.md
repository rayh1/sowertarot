---
title: "The Bramble"
concept: "Untamed edges, fierce wild beauty, the defended wilderness"
key_terms: ["bramble", "thorn", "thicket", "hedgerow", "wild growth", "untamed edge"]
created: "2026-04-21"
seed: 281673759
image_status: "present"
prompt_status: "original"
image: "card_the-bramble.png"
clip: "the-bramble_code_v1.mp4"
joplin_note: "0767d0fad2334ac3beb68154ab23e52c"
---

# The Bramble

*An original tarot card in the Rider-Waite tradition*

![The Bramble](/media/card_the-bramble.png)

## Visual Description

### Composition
A young woman in a green dress, a wicker basket on her arm, stands on a narrow path between dense thickets of thorny bramble, reaching carefully into the thorns to pick a dark blackberry. A small bird with an orange breast perches among the canes beside her hand. Behind the hedge, golden fields roll away to low hills under a pink-and-gold evening sky, where a single bright evening star shines.

### Symbolism
The bramble is the defended wilderness: fierce and thorny, yet it shelters birds and gives its fruit to those who reach in with care. Her careful hand is respect for the wild, taking only what is offered. The little bird nesting safely in the thorns shows what the bramble protects. The cultivated fields beyond mark the boundary between tamed and untamed land.

### Atmosphere
Evening, a sky of soft pink, gold and grey, with the first star. The mood is wild, careful and defiant.

## Archetypal Essence

The Bramble represents the sacred function of the unwelcoming edge — the wild, thorned growth that protects what tender life has chosen to shelter there. It names the beauty and legitimacy of hedgerow consciousness: the self, the place, or the truth that remains unavailable without having to apologize for being defended. In the archetypal field, the Bramble stands for what grows fiercely precisely because nothing has trained it, and for the quiet miracle that small, tender living things find their safest home inside what the world calls impassable.

## Render Prompt

```
A young woman in a moss-green dress, a wicker basket on her arm, reaches carefully into a dense thicket of thorny bramble canes to pick a ripe dark blackberry. Deep among the thorns, a small brown wren perches with its tail cocked. The bramble hedge runs between a ploughed field on the left and open wild heathland on the right. Low rolling hills lie behind under a twilight sky of soft violet and gold, with one bright evening star. Wild, careful, defiant mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE BRAMBLE" at the bottom.

Foreground: A dense, sinuous thicket of wild bramble canes fills the lower two-thirds of the card, arranged in interlocking loops with dark green serrated leaves and sharp visible thorns. Scattered through the thicket are clusters of bright red rosehips and a few late dark berries. At the center-right of the bramble, nestled deep and safe among the thorns, is a single small brown wren with a tiny upturned tail, its eye catching the light.

Middle ground: The bramble extends rightward into a wild hedgerow forming a living boundary between a neatly furrowed cultivated field on the left and open uncultivated heathland on the right.

Background: A twilight sky in deep indigo fading to pale gold at the horizon, low rolling hills in silhouette, and a single bright evening star emerging high in the sky.

Mood: still, defended, quiet, watchful — the sacred beauty of the wild untamed edge. Lighting is the soft blue hour, warm browns in the brambles against the cool indigo sky.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE BRAMBLE" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout                                     
```

## Render Record

<details>
<summary>Seed 281673759 · tarot_flux_final_01162_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T22:20:22+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01162_.png`
- Seed: 281673759
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-01T22:20:22+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01162_.png",
  "seed": 281673759,
  "title": "The Bramble",
  "scene": "A young woman in a moss-green dress, a wicker basket on her arm, reaches carefully into a dense thicket of thorny bramble canes to pick a ripe dark blackberry. Deep among the thorns, a small brown wren perches with its tail cocked. The bramble hedge runs between a ploughed field on the left and open wild heathland on the right. Low rolling hills lie behind under a twilight sky of soft violet and gold, with one bright evening star. Wild, careful, defiant mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a moss-green dress, a wicker basket on her arm, reaches carefully into a dense thicket of thorny bramble canes to pick a ripe dark blackberry. Deep among the thorns, a small brown wren perches with its tail cocked. The bramble hedge runs between a ploughed field on the left and open wild heathland on the right. Low rolling hills lie behind under a twilight sky of soft violet and gold, with one bright evening star. Wild, careful, defiant mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a moss-green dress, a wicker basket on her arm, reaches carefully into a dense thicket of thorny bramble canes to pick a ripe dark blackberry. Deep among the thorns, a small brown wren perches with its tail cocked. The bramble hedge runs between a ploughed field on the left and open wild heathland on the right. Low rolling hills lie behind under a twilight sky of soft violet and gold, with one bright evening star. Wild, careful, defiant mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 281673759,
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
