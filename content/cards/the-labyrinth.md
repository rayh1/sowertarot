---
title: "The Labyrinth"
concept: "Complex journey, finding way"
key_terms: ["labyrinth", "maze", "puzzle"]
created: "2025-12-24"
seed: 100376223
image_status: "present"
prompt_status: "original"
image: "card_the-labyrinth.png"
clip: "the-labyrinth_code_v1.mp4"
joplin_note: "00ff2218166d4c9aa791ac849be13a8d"
---

# The Labyrinth

*An original tarot card in the Rider-Waite tradition*

![The Labyrinth](/media/card_the-labyrinth.png)

## Visual Description

### Composition
Seen from high above, a great round labyrinth of clipped hedges, pale green on top and dark at the sides, fills the card, its narrow pale paths turning in concentric rings toward the centre; near the top the rings break into straight, blocky hedges. At the heart, in a small round clearing, grows a single small tree with a round golden crown, a red thread lying at its foot. At the bottom of the card a young man in a pale grey-green tunic walks in through the entrance. Fallen autumn leaves are scattered along the paths.

### Symbolism
The hedges are the winding, enclosed path of life, whose pattern can be seen only from above. The view from the air is the card's gift: the whole way laid out, which the walker can only live through on foot. The red thread is memory and trust, the line that keeps him from being wholly lost. The golden tree at the heart is the centre that waits to be found, wholeness reached by walking rather than solving.

### Atmosphere
Soft, even daylight over muted greens. The mood is contemplative and searching, alone but not afraid.

## Archetypal Essence

The Labyrinth represents the archetypal journey of life itself, where the path to wisdom, wholeness, or enlightenment is never straight but winds through confusion, doubling back, dead ends, and unexpected openings. Unlike a maze designed to deceive, a labyrinth has a center waiting to be found—the journey is not about solving a puzzle but about the transformation that occurs through the walking itself. This card reminds us that being lost is not failure but often the necessary condition for profound discovery, and that the winding path teaches us things the direct route never could.

## Render Prompt

```
Seen from high above, a great round hedge labyrinth of dark clipped yew fills the scene, its narrow grass paths winding in tight concentric turns toward the centre. A tiny figure of a young man in a green tunic walks one of the paths, a thin red thread trailing behind him back to the entrance at the bottom. At the labyrinth's heart a single rose bush with large golden blooms grows in a small round lawn. Frost whitens the hedge tops and fallen autumn leaves lie scattered on the paths. Soft pale gold dawn light. Contemplative, searching mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE LABYRINTH" at the bottom.

An intricate maze stretches across the entire card, viewed from directly above as if looking down from a great height. The pathways are formed by tall hedges of dark green yew, their trimmed tops dusted with a thin layer of morning frost that glints silver. At the exact center of the labyrinth, the hedges open into a small circular clearing containing a white marble fountain whose water is still and mirror-like, and beside it blooms a single magnificent golden rose that radiates soft luminous light outward.

Multiple small figures can be seen at various points within the maze — some traveling alone, others in pairs — each at different distances from the center. One prominent figure stands at the labyrinth's entrance at the bottom of the card, one hand resting on a low stone pillar where three paths diverge. Their shadow extends long behind them in the warm amber light of dawn coming from the lower edge.

Thin red threads wind through certain pathways, some leading successfully toward the center, others trailing into dead ends. Above the labyrinth, a large raven circles with wings spread wide, as if mapping the pattern from above. In each of the four corners of the card, a weathered stone statue stands guard, half-covered in climbing ivy and green vines: a lion in the upper-left, an eagle in the upper-right, a bull in the lower-left, and an angel in the lower-right.

The outer edges of the card show the labyrinth's walls extending beyond the frame in every direction, suggesting infinite complexity. Along some pathways, fallen russet and gold autumn leaves are scattered; other pathways remain pristine and untouched.

Atmosphere: the amber first light of dawn over ancient green hedges — pilgrimage, patience, sacred wandering.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE LABYRINTH" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 100376223 · tarot_flux_final_00307_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-03T03:55:20+02:00 · ComfyUI 0.38.0 · output `tarot_flux_final_00307_.png`
- Seed: 100376223
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-03T03:55:20+02:00",
  "comfyui_version": "0.38.0",
  "comfy_file": "tarot_flux_final_00307_.png",
  "seed": 100376223,
  "title": "The Labyrinth",
  "scene": "Seen from high above, a great round hedge labyrinth of dark clipped yew fills the scene, its narrow grass paths winding in tight concentric turns toward the centre. A tiny figure of a young man in a green tunic walks one of the paths, a thin red thread trailing behind him back to the entrance at the bottom. At the labyrinth's heart a single rose bush with large golden blooms grows in a small round lawn. Frost whitens the hedge tops and fallen autumn leaves lie scattered on the paths. Soft pale gold dawn light. Contemplative, searching mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nSeen from high above, a great round hedge labyrinth of dark clipped yew fills the scene, its narrow grass paths winding in tight concentric turns toward the centre. A tiny figure of a young man in a green tunic walks one of the paths, a thin red thread trailing behind him back to the entrance at the bottom. At the labyrinth's heart a single rose bush with large golden blooms grows in a small round lawn. Frost whitens the hedge tops and fallen autumn leaves lie scattered on the paths. Soft pale gold dawn light. Contemplative, searching mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nSeen from high above, a great round hedge labyrinth of dark clipped yew fills the scene, its narrow grass paths winding in tight concentric turns toward the centre. A tiny figure of a young man in a green tunic walks one of the paths, a thin red thread trailing behind him back to the entrance at the bottom. At the labyrinth's heart a single rose bush with large golden blooms grows in a small round lawn. Frost whitens the hedge tops and fallen autumn leaves lie scattered on the paths. Soft pale gold dawn light. Contemplative, searching mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 100376223,
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
