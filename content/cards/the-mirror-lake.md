---
title: "The Mirror Lake"
concept: "Reflection, inner truth"
key_terms: ["mirror", "lake", "reflection"]
created: "2025-12-24"
seed: 519804146
image_status: "present"
prompt_status: "original"
image: "card_the-mirror-lake.png"
clip: "the-mirror-lake_code_v2.mp4"
joplin_note: "1455e0367106471b97c7225367798394"
---

# The Mirror Lake

*An original tarot card in the Rider-Waite tradition*

![The Mirror Lake](/media/card_the-mirror-lake.png)

## Visual Description

### Composition
A perfectly still mountain lake lies between steep peaks whose snow glows pink, and the peaks are mirrored upside down in its glassy surface, so the far shore and its reflection meet in one line across the middle of the card. Dark pines stand on the right bank and are reflected too. In the foreground two white water lilies open on broad green pads near a shore of smooth grey stones. Pink clouds drift in a pale cream sky.

### Symbolism
The mirror lake is the still mind: only when the water is calm does it show the world truly. The doubled peaks show the outer world and its reflection as equal halves. With no figure, the lake itself is the one who sees. The lilies, rooted in mud yet opening clean on the surface, are clarity that grows out of depth.

### Atmosphere
Evening, a pale cream sky touched with pink. The air is utterly still. The mood is silent, clear and contemplative.

## Archetypal Essence

The Mirror Lake represents the still point of consciousness where truth can be seen without distortion. It is the archetype of honest self-reflection, the moment when we dare to look at who we truly are beneath all our masks and defenses. Like the undisturbed lake that reflects both the sky and depths below, this card teaches that clarity comes through stillness, and that what we see in our reflection often reveals more truth than what we show to the world.

## Render Prompt

```
A perfectly still mountain lake lies between snow-capped peaks, which rise on both sides and are mirrored upside down in its glassy surface, so the far shore and its reflection meet in a single line across the middle of the scene. In the foreground a few white water lilies with broad green pads float near a shore of smooth grey stones. A pair of tall dark pines stands on the right bank, reflected too. Pale pink and lavender evening sky with a few soft clouds, doubled in the water. Silent, clear, contemplative mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE MIRROR LAKE" at the bottom.

A perfectly still mountain lake fills the card, reflecting the sky so clearly that the boundary between water and air is nearly imperceptible. The composition is vertically symmetrical: ancient snow-capped mountains, soft clouds, and a glowing sun appear both above in the real sky and below in the water's reflection, mirrored with crystalline precision.

At the lake's center, a figure in a simple white robe kneels at the water's edge, looking down into their own reflection. The reflection gazes back with quietly knowing eyes. But the reflected figure shows details not present above: a delicate crown of stars rests on the reflected head, and their chest glows with warm golden light from the heart.

White lotus flowers bloom on the water's surface and again in their perfect reflections. In the sky, the moon and sun appear simultaneously at opposite ends of the horizon, both perfectly mirrored in the water below. A single drop of water falls from the figure's hand, creating the first small ripples that are just beginning to disturb the perfect mirror.

Atmosphere: still, reverent, contemplative — the pristine silence of a high mountain dawn, the color palette pale and luminous with blues, silvers, whites, and soft golds.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE MIRROR LAKE" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 519804146 · tarot_flux_final_00048_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-03T01:23:26+02:00 · ComfyUI 0.38.0 · output `tarot_flux_final_00048_.png`
- Seed: 519804146
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-03T01:23:26+02:00",
  "comfyui_version": "0.38.0",
  "comfy_file": "tarot_flux_final_00048_.png",
  "seed": 519804146,
  "title": "The Mirror Lake",
  "scene": "A perfectly still mountain lake lies between snow-capped peaks, which rise on both sides and are mirrored upside down in its glassy surface, so the far shore and its reflection meet in a single line across the middle of the scene. In the foreground a few white water lilies with broad green pads float near a shore of smooth grey stones. A pair of tall dark pines stands on the right bank, reflected too. Pale pink and lavender evening sky with a few soft clouds, doubled in the water. Silent, clear, contemplative mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA perfectly still mountain lake lies between snow-capped peaks, which rise on both sides and are mirrored upside down in its glassy surface, so the far shore and its reflection meet in a single line across the middle of the scene. In the foreground a few white water lilies with broad green pads float near a shore of smooth grey stones. A pair of tall dark pines stands on the right bank, reflected too. Pale pink and lavender evening sky with a few soft clouds, doubled in the water. Silent, clear, contemplative mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA perfectly still mountain lake lies between snow-capped peaks, which rise on both sides and are mirrored upside down in its glassy surface, so the far shore and its reflection meet in a single line across the middle of the scene. In the foreground a few white water lilies with broad green pads float near a shore of smooth grey stones. A pair of tall dark pines stands on the right bank, reflected too. Pale pink and lavender evening sky with a few soft clouds, doubled in the water. Silent, clear, contemplative mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 519804146,
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
