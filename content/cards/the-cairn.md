---
title: "The Cairn"
concept: "Cumulative testimony, the silent gift forward"
key_terms: ["cairn", "stones", "stacked stones", "marker", "memorial", "trail"]
created: "2026-04-19"
seed: 420824485
image_status: "present"
prompt_status: "original"
image: "card_the-cairn.png"
clip: "the-cairn_code_v1.mp4"
joplin_note: "eef11cb2186f4c0c95b1a6aeb6b61ec5"
---

# The Cairn

*An original tarot card in the Rider-Waite tradition*

![The Cairn](/media/card_the-cairn.png)

## Visual Description

### Composition
On a windswept mountain pass an old traveller with a white beard, in a long brown checked wool cloak, bends to set a smooth round grey stone on top of a waist-high cairn of grey stones balanced one on another. A small girl in a red knitted hood and a green coat stands beside him, reaching toward the cairn. Behind them the stony path winds down between rocky slopes into a grassy valley, marked along the way by two smaller cairns. A faint pale sun shows through the haze above the far mountains.

### Symbolism
The cairn is cumulative testimony: each traveller adds one stone, and together they mark the way for those who come after. The old traveller and the child are that gift passing between generations, the knowledge of the road handed from the one who has walked it to the one who will. The smaller cairns along the path show that others have walked here before.

### Atmosphere
Clear early morning, a pale hazy sky, the valley in soft light. The mood is reverent and tender.

## Archetypal Essence

The Cairn represents the archetype of accumulated wisdom and collective human endeavor. Each stone is a moment, a lesson, a deliberate choice—alone insignificant, but together creating something that endures and guides. This card speaks to our deep need to both receive guidance from those who walked before us and to leave markers for those who follow. It reminds us that we are always both beneficiaries of past efforts and contributors to future journeys. The Cairn teaches that meaning is built stone by stone, that legacy is created through patient accumulation, and that even the smallest contribution to the path matters when placed with intention and care.

## Render Prompt

```
On a windswept mountain pass an old traveller with a white beard, in a brown and green checked wool cloak, bends to hand a smooth white stone to a small girl in a red knitted hood. The girl stands on tiptoe beside a waist-high cairn of grey, rust-red and white stones, reaching up to place the stone on top. Behind them the stony path winds down into misty valleys, and two smaller cairns mark the way ahead along the pass. Clear morning sky with thin wisps of cloud, a pale sun rising over the ridges. Tender, deliberate mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE CAIRN" at the bottom.

A figure in earth-toned robes of brown and deep green kneels beside a carefully balanced stack of stones on a windswept mountain pass. They place the final stone on top of the cairn with both hands, their posture reverent and deliberate. The cairn is waist-high, composed of eight visible stones of varying sizes and colors: granite gray, rust red, and river-smoothed white. The stones are distinct yet contributing to the stable whole.

The setting is a windswept mountain pass with a winding path that stretches behind the figure down through mist-shrouded valleys, and ahead disappears around a rocky outcrop. Three smaller cairns are visible in the distance marking the trail. The sky is a clear morning blue with wisps of cloud. Golden sunlight illuminates the scene from the left, casting long shadows from each stone in the stack.

Around the base of the cairn, small alpine flowers grow between rocks: purple saxifrage and white mountain avens. The figure has weathered, earth-stained hands. A leather travel bag filled with smooth river stones sits beside them. In the middle distance, a hawk circles on thermal currents. Faint footprints of previous travelers mark the path. In the background, scattered through the landscape, are ruins of older cairns — some toppled by time, others still standing after decades.

Atmosphere: contemplative and reverent, emphasizing guidance, legacy, and patient accumulation of wisdom.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE CAIRN" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 420824485 · tarot_flux_final_00131_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-03T02:12:14+02:00 · ComfyUI 0.38.0 · output `tarot_flux_final_00131_.png`
- Seed: 420824485
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-03T02:12:14+02:00",
  "comfyui_version": "0.38.0",
  "comfy_file": "tarot_flux_final_00131_.png",
  "seed": 420824485,
  "title": "The Cairn",
  "scene": "On a windswept mountain pass an old traveller with a white beard, in a brown and green checked wool cloak, bends to hand a smooth white stone to a small girl in a red knitted hood. The girl stands on tiptoe beside a waist-high cairn of grey, rust-red and white stones, reaching up to place the stone on top. Behind them the stony path winds down into misty valleys, and two smaller cairns mark the way ahead along the pass. Clear morning sky with thin wisps of cloud, a pale sun rising over the ridges. Tender, deliberate mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nOn a windswept mountain pass an old traveller with a white beard, in a brown and green checked wool cloak, bends to hand a smooth white stone to a small girl in a red knitted hood. The girl stands on tiptoe beside a waist-high cairn of grey, rust-red and white stones, reaching up to place the stone on top. Behind them the stony path winds down into misty valleys, and two smaller cairns mark the way ahead along the pass. Clear morning sky with thin wisps of cloud, a pale sun rising over the ridges. Tender, deliberate mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nOn a windswept mountain pass an old traveller with a white beard, in a brown and green checked wool cloak, bends to hand a smooth white stone to a small girl in a red knitted hood. The girl stands on tiptoe beside a waist-high cairn of grey, rust-red and white stones, reaching up to place the stone on top. Behind them the stony path winds down into misty valleys, and two smaller cairns mark the way ahead along the pass. Clear morning sky with thin wisps of cloud, a pale sun rising over the ridges. Tender, deliberate mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 420824485,
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
