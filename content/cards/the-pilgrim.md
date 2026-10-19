---
title: "The Pilgrim"
concept: "Sacred journey, seeking"
key_terms: ["pilgrim", "traveler", "wanderer"]
created: "2025-12-24"
seed: 120964052
image_status: "present"
prompt_status: "original"
image: "card_the-pilgrim.png"
clip: "the-pilgrim_code_v1.mp4"
joplin_note: "8e28ef36c3e247b89e0c7979da1fc6d0"
---

# The Pilgrim

*An original tarot card in the Rider-Waite tradition*

![The Pilgrim](/media/card_the-pilgrim.png)

## Visual Description

### Composition
A small figure of a pilgrim in an ochre travelling coat and a wide-brimmed hat, leaning on a tall staff, walks away from us along a long dirt road that winds back and forth across a vast landscape of green foothills. Small stacked-stone cairns mark the roadside. Far ahead, where the road ends, a small golden chapel with a cross stands at the foot of purple mountains. A line of white cranes flies across the sky toward it.

### Symbolism
The road is the journey itself, long and winding, the destination visible but far. The pilgrim is small against the land: the journey is greater than the one who makes it. The staff is discipline and support. The cairns are the marks of those who walked before. The distant chapel is the sacred goal that draws the seeker on; the cranes flying the same way are fellow travellers and good omens.

### Atmosphere
Dawn, the sky shading from pale green-grey overhead to peach at the mountains. The light is calm and clear. The mood is steady and determined, the quiet resolve of someone who has chosen the long way.

## Archetypal Essence

The Pilgrim represents the archetype of the seeker who understands that transformation requires movement, both physical and spiritual. This card speaks to those who answer a call that others may not hear, who are willing to leave behind comfort and certainty in pursuit of something more essential. It reminds us that pilgrimage is not tourism—it is a deliberate practice of seeking the sacred through discipline, sacrifice, and open-hearted presence to each step of the journey, knowing that we are changed not by reaching the destination but by everything we encounter along the way.

## Render Prompt

```
A tiny distant figure of a pilgrim in an ochre travelling coat and a wide-brimmed hat, leaning on a tall staff, walks away from us along a long winding dirt road that crosses a vast landscape of green foothills. The road curves on and on toward distant purple mountains, where a small golden-domed chapel sits on a far ridge in soft morning mist. Small stacked-stone cairns mark the roadside, and a line of white cranes flies high toward the chapel. Warm amber dawn light, the sky turning clear blue ahead. Steady, determined, solitary mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE PILGRIM" at the bottom.

A solitary traveler walks along a winding dirt path that stretches from the foreground into distant purple mountains. The figure is centered in the lower-middle of the card, seen from a three-quarter rear angle as they move deeper into the scene. They wear a simple hooded cloak of deep weathered brown, marked by sun and rain, and carry a worn wooden walking staff in one hand. A small leather satchel hangs across their shoulders on a plain strap, well-packed and well-used. Their feet are bare and dusty on the path, showing both the hardship and humility of the journey. The pilgrim's face is partially shadowed by the hood, but what is visible shows a steady, quietly determined forward gaze.

The winding path is marked at intervals by small stone cairns — evidence of the many others who have walked this way before. Wild sage and rosemary grow along both sides of the road, their purple and silver-grey leaves stirring in a gentle breeze. To the left of the path sits an ancient stone well offering water to travelers, a weathered wooden dipper hanging from its chain. To the right, a simple wooden shrine holds small offerings on its ledge: dried flowers tied with twine, smooth stones, and a single lit candle whose flame somehow burns steadily despite the wind.

In the far distance, barely visible through morning mist, a golden dome or spire marks the sacred destination, still many days' walk away. The sky above transitions from warm amber sunrise colors behind the pilgrim to cool clear blue ahead in the direction of travel. Seven white cranes fly in formation overhead, heading in the same direction as the traveler. The pilgrim's shadow extends long on the path behind them, a constant companion marking the passage of time and distance.

Atmosphere: the hush of early morning on the road, humble and devotional.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE PILGRIM" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 120964052 · tarot_flux_final_00246_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-03T03:19:55+02:00 · ComfyUI 0.38.0 · output `tarot_flux_final_00246_.png`
- Seed: 120964052
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-03T03:19:55+02:00",
  "comfyui_version": "0.38.0",
  "comfy_file": "tarot_flux_final_00246_.png",
  "seed": 120964052,
  "title": "The Pilgrim",
  "scene": "A tiny distant figure of a pilgrim in an ochre travelling coat and a wide-brimmed hat, leaning on a tall staff, walks away from us along a long winding dirt road that crosses a vast landscape of green foothills. The road curves on and on toward distant purple mountains, where a small golden-domed chapel sits on a far ridge in soft morning mist. Small stacked-stone cairns mark the roadside, and a line of white cranes flies high toward the chapel. Warm amber dawn light, the sky turning clear blue ahead. Steady, determined, solitary mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA tiny distant figure of a pilgrim in an ochre travelling coat and a wide-brimmed hat, leaning on a tall staff, walks away from us along a long winding dirt road that crosses a vast landscape of green foothills. The road curves on and on toward distant purple mountains, where a small golden-domed chapel sits on a far ridge in soft morning mist. Small stacked-stone cairns mark the roadside, and a line of white cranes flies high toward the chapel. Warm amber dawn light, the sky turning clear blue ahead. Steady, determined, solitary mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA tiny distant figure of a pilgrim in an ochre travelling coat and a wide-brimmed hat, leaning on a tall staff, walks away from us along a long winding dirt road that crosses a vast landscape of green foothills. The road curves on and on toward distant purple mountains, where a small golden-domed chapel sits on a far ridge in soft morning mist. Small stacked-stone cairns mark the roadside, and a line of white cranes flies high toward the chapel. Warm amber dawn light, the sky turning clear blue ahead. Steady, determined, solitary mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 120964052,
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
