---
title: "The Candelabra"
concept: "Multiple paths, sacred illumination"
key_terms: ["candelabra", "candles", "flames", "seven lights", "ceremony"]
created: "2025-12-24"
seed: 450317646
image_status: "present"
prompt_status: "original"
image: "card_the-candelabra.png"
clip: "the-candelabra_code_v1.mp4"
joplin_note: "c820457ccdbe46878b89128c39be496a"
---

# The Candelabra

*An original tarot card in the Rider-Waite tradition*

![The Candelabra](/media/card_the-candelabra.png)

## Visual Description

### Composition
A woman in a long dark-green gown walks along a pale stone path through a night garden, holding up a tall silver candelabra with five lit candles in one hand. White roses grow thickly on both sides of the path. Behind her the path leads back to a small stone chapel with a green door and a cross on its roof. Bare trees frame the starry sky.

### Symbolism
The candelabra is light carried out into the dark, many flames from one stem: many paths of understanding held together. The woman bearing it walks away from the chapel, taking the sacred light out into the world. The white roses are purity and devotion along the way. The night shows that this light matters most where it is darkest.

### Atmosphere
Deep night with a scattering of stars, lit only by the candles' warm glow. The mood is reverent, quiet and glowing.

## Archetypal Essence

The Candelabra represents the eternal human quest to illuminate darkness through knowledge, faith, and shared understanding. It embodies the principle that truth reveals itself through multiple expressions - just as seven flames can burn with different colors yet all provide light. This card speaks to both the solitary scholar burning midnight oil and the community gathered in ceremony, reminding us that enlightenment is both an individual journey and a collective heritage. The Candelabra teaches that we each carry a flame meant not only to guide our own path but to join with others in creating a greater radiance that can illuminate the way for all who seek.

## Render Prompt

```
A priestess in a long dark-green velvet gown walks slowly along a stone path through an evening garden, carrying a tall seven-branched silver candelabra before her in both hands, all seven candles lit with small steady flames. The warm candlelight falls on her face and on the white roses growing beside the path. Behind her, the path leads back to the dark arched doorway of a small stone chapel. Deep blue dusk sky with the first stars. Reverent, quiet, glowing mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE CANDELABRA" at the bottom.

The central focus is an ornate seven-branched silver candelabra standing on an altar draped in deep purple velvet. Each of the seven candles burns with a distinctly different colored flame: white, gold, blue, green, red, violet, and silver, arranged from left to right. The candelabra has intricate vine-like patterns spiraling up each branch, with an ancient symbol inscription at its base.

Behind the candelabra, a large circular stained-glass window dominates the background, featuring a radiant sun at its center surrounded by phases of the moon in a mandala pattern. The colored light from this window mingles with the candlelight, casting rainbow prismatic patterns across the stone walls of the sacred chamber. The scene is set at twilight, with deep blue and purple tones in the sky visible through the window.

In the foreground, seven open books rest on the altar, one positioned before each candle, their pages glowing with reflected firelight. White roses and sprigs of rosemary are delicately woven between the books. A moth with intricate eye-patterns on its wings hovers gracefully near the central white flame, drawn to its light.

At the base of the candelabra, streams of colored wax from each candle flow downward and merge together into a single pool that forms the shape of a chalice. The stone floor features geometric patterns of interlocking circles. Small five-pointed stars are scattered throughout the darker portions of the image, particularly in the shadowed corners and around the outer edges.

The overall composition is vertically oriented and symmetrical, with rich symbolic details throughout. The atmosphere is reverent and mystical, with warm candlelight contrasting against cooler twilight tones.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE CANDELABRA" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 450317646 · tarot_flux_final_00921_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T18:29:46+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00921_.png`
- Seed: 450317646
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-01T18:29:46+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00921_.png",
  "seed": 450317646,
  "title": "The Candelabra",
  "scene": "A priestess in a long dark-green velvet gown walks slowly along a stone path through an evening garden, carrying a tall seven-branched silver candelabra before her in both hands, all seven candles lit with small steady flames. The warm candlelight falls on her face and on the white roses growing beside the path. Behind her, the path leads back to the dark arched doorway of a small stone chapel. Deep blue dusk sky with the first stars. Reverent, quiet, glowing mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA priestess in a long dark-green velvet gown walks slowly along a stone path through an evening garden, carrying a tall seven-branched silver candelabra before her in both hands, all seven candles lit with small steady flames. The warm candlelight falls on her face and on the white roses growing beside the path. Behind her, the path leads back to the dark arched doorway of a small stone chapel. Deep blue dusk sky with the first stars. Reverent, quiet, glowing mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA priestess in a long dark-green velvet gown walks slowly along a stone path through an evening garden, carrying a tall seven-branched silver candelabra before her in both hands, all seven candles lit with small steady flames. The warm candlelight falls on her face and on the white roses growing beside the path. Behind her, the path leads back to the dark arched doorway of a small stone chapel. Deep blue dusk sky with the first stars. Reverent, quiet, glowing mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 450317646,
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
