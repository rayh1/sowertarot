---
title: "The Compass Rose"
concept: "Finding true direction, inner guidance"
key_terms: ["compass", "rose", "direction", "navigation", "cardinal", "orientation"]
created: "2025-12-28"
seed: 334979220
image_status: "present"
prompt_status: "original"
image: "card_the-compass-rose.png"
clip: "the-compass-rose_code_v3.mp4"
joplin_note: "3928ce57f90448b090c9fe217d270ada"
---

# The Compass Rose

*An original tarot card in the Rider-Waite tradition*

![The Compass Rose](/media/card_the-compass-rose.png)

## Visual Description

### Composition
A young traveller in a long grey hooded cloak and tall leather boots stands on a rocky summit, holding an open brass compass on his palm. Below him a broad river winds between steep mountain ridges toward a distant sea. A single bright star shines among many small stars in the deep teal-green sky above, and golden clouds glow along the horizon.

### Symbolism
The compass is inner guidance made visible: direction found by steadiness rather than by seeing the whole way. The single bright star, brighter than all the others, is the fixed point to steer by. The winding river below is the path of life, never straight but always moving toward the sea. The summit is the moment of overview, where one can see where to go next.

### Atmosphere
Twilight, the sky deepening to teal-green overhead with gold at the horizon. The mood is focused and certain.

## Archetypal Essence

The Compass Rose represents the eternal human need for orientation—both in the physical world and in the landscape of the soul. It embodies the mysterious faculty we possess to sense true direction even when lost, to find our way home even in darkness. This card speaks to the alignment between our deepest knowing and the cosmic order, reminding us that we carry within ourselves an infallible guide. When we stand centered and grounded, we can perceive all paths available to us and choose with wisdom rather than fear.

## Render Prompt

```
A young traveller in a short grey wool tunic and tall leather boots stands on a rocky mountain summit, holding an open brass compass flat on his palm and looking out across the land. Below him, mountain ridges and valleys fall away in every direction, a river winding through them toward a distant sea. A single bright star shines low in the north above the farthest peaks. Clear twilight sky of deep blue fading to gold at the horizon. Wind stirs his cloak. Focused, certain mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE COMPASS ROSE" at the bottom.

A magnificent ornate compass rose floats at the center of a deep twilight sky scattered with stars. The compass rose is rendered in burnished gold and silver metalwork, with eight primary points radiating outward in perfect symmetry. Each cardinal direction bears a different elemental symbol: a delicate snowflake for North, a small flame for South, a radiant sun for East, and a crescent moon for West. The compass rose should be detailed and beautiful, like an ancient navigational instrument.

Below the floating compass, a solitary figure in a flowing deep blue cloak stands on a mountaintop with arms outstretched, palms facing upward. The cloak billows dramatically in the wind. The figure's bare feet are planted on ancient weathered stone. A small pendant compass hangs on a chain around their neck.

The background shows four distinct landscapes extending from each cardinal direction: snow-capped mountain peaks to the North, red desert sands to the South, golden sunrise over green plains to the East, and a dark mysterious forest under moonlight to the West. Each landscape fades into soft mist at its edges.

The sky transitions from deep indigo at the top to soft lavender at the horizon. Seven bright stars form a subtle arc above the compass rose. At the bottom, a winding path splits into four directions leading toward the four landscapes. Delicate lines of golden light connect the floating compass rose to the figure's pendant, creating a mystical connection.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE COMPASS ROSE" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 334979220 · tarot_flux_final_00950_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T18:46:16+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00950_.png`
- Seed: 334979220
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-01T18:46:16+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00950_.png",
  "seed": 334979220,
  "title": "The Compass Rose",
  "scene": "A young traveller in a short grey wool tunic and tall leather boots stands on a rocky mountain summit, holding an open brass compass flat on his palm and looking out across the land. Below him, mountain ridges and valleys fall away in every direction, a river winding through them toward a distant sea. A single bright star shines low in the north above the farthest peaks. Clear twilight sky of deep blue fading to gold at the horizon. Wind stirs his cloak. Focused, certain mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young traveller in a short grey wool tunic and tall leather boots stands on a rocky mountain summit, holding an open brass compass flat on his palm and looking out across the land. Below him, mountain ridges and valleys fall away in every direction, a river winding through them toward a distant sea. A single bright star shines low in the north above the farthest peaks. Clear twilight sky of deep blue fading to gold at the horizon. Wind stirs his cloak. Focused, certain mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young traveller in a short grey wool tunic and tall leather boots stands on a rocky mountain summit, holding an open brass compass flat on his palm and looking out across the land. Below him, mountain ridges and valleys fall away in every direction, a river winding through them toward a distant sea. A single bright star shines low in the north above the farthest peaks. Clear twilight sky of deep blue fading to gold at the horizon. Wind stirs his cloak. Focused, certain mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 334979220,
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
