---
title: "The Ember"
concept: "Dormant potential, rekindling"
key_terms: ["ember", "coal", "spark"]
created: "2025-12-24"
seed: 600000
image_status: "present"
prompt_status: "original"
image: "card_the-ember.png"
clip: "the-ember_s5_v2.mp4"
joplin_note: "3967e8b4e43f4d4bb581112a69225df9"
---

# The Ember

*An original tarot card in the Rider-Waite tradition*

![The Ember](/media/card_the-ember.png)

## Visual Description

At the center of the card, a single glowing ember rests in a bed of white ash within a simple clay bowl. The ember glows deep orange and crimson, but its small light does not reach the dark room around it. One weathered hand rests on the figure's knee; the other is held open toward the bowl, close enough to feel its warmth. The hands belong to a figure whose face is obscured by shadow, making them universal, timeless. Behind the figure, the room is dimly lit, with evidence of both life and stillness: a doorway leading to darkness on the left, a tall arched window on the right showing a pale sky over hills and pine forest. The white ash is the remnant of what was; nearby lie the materials of rekindling: a few sticks of fresh kindling on the stone floor. Smoke rises from the ember in a thin, steady stream, neither dissipating nor growing stronger. The ember itself seems almost alive, its surface showing intricate patterns of cooling black and glowing red, like a miniature landscape of volcanic potential.

## Archetypal Essence

The Ember represents the archetype of latent potential - the seed of fire that waits between extinction and conflagration, requiring both protection and eventual commitment. This card speaks to the delicate art of preservation, the wisdom of knowing what can be rekindled and what must be released, and the courage required to cup our hands around vulnerable light in the darkness. It teaches that some things need to burn down to embers before they can be transformed into new flame, and that the ember stage - neither dead nor fully alive - is itself a state of power. The Ember reminds us that we are all tenders of inner fires, responsible for knowing when to shelter, when to breathe life into, and when to finally let go.

## Render Prompt

```
A robed monk in a coarse woollen habit with a deep cowl sits cross-legged facing the viewer, face lost in the shadow of the cowl. On the floor before the monk stands a simple clay bowl of white ash, and in the ash rests a single walnut-sized lump of black charcoal cracked with glowing red veins, the only warm light in the scene. The monk's open palms are held on either side of the bowl, a hand's width away, sheltering the glow, lit warm from below. A faint grey wisp of smoke curls softly upward from the coal. A small pale moth hovers beside one hand. To the right a narrow window shows a pale grey pre-dawn sky over distant hills; the rest of the room fades into deep shadow. A few sticks of dry kindling lie beside the bowl. Plain dark floor in the lower part of the scene. Hushed, patient, protective stillness.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE EMBER" at the bottom.

At the exact center of the card, a single glowing ember rests in a bed of soft white ash held within a simple unglazed clay bowl. The ember pulses with deep orange and crimson light, casting dancing warm shadows across the surrounding scene. Its surface shows intricate patterns of cooling black and glowing red, like a miniature landscape of volcanic potential.

A pair of weathered hands cups around the bowl protectively — not touching it, but hovering close enough to feel the warmth. The hands belong to a seated figure whose face is obscured in shadow, rendering them universal and timeless. A thin steady stream of smoke rises from the ember, neither dissipating nor growing stronger, vanishing into the dim air above.

Behind the figure, the room is dimly lit with a warm amber tone closest to the ember, fading into cool shadow at the edges. On the left, a doorway leads into deeper darkness. On the right, a small window shows the first pale hint of pre-dawn gray light. Scattered around the bowl are the remnants of what was: charred black wood, spent matches, cold stones that once held heat. But the materials of rekindling are also present: a small stack of fresh dry kindling to one side, bundles of dried herbs hanging from rafters, and a leather-and-wood bellows resting against the stone wall.

On the floor around the bowl, ash has been swept into deliberate patterns — soft spirals and geometric symbols suggesting careful ritual. A moth circles the ember's glow, drawn toward the light but maintaining careful distance from the heat.

Atmosphere: the sacred hush of pre-dawn, protected light in the dark, patient care.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE EMBER" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 600000 · tarot_flux_final_00085_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`. The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00085_.png`
- Seed: 600000
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00085_.png, matched to the attached image by pixel comparison (mean difference 1.0 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00086_.png at 54.4). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00085_.png",
  "seed": 600000,
  "title": "The Ember",
  "scene": "A robed monk in a coarse woollen habit with a deep cowl sits cross-legged facing the viewer, face lost in the shadow of the cowl. On the floor before the monk stands a simple clay bowl of white ash, and in the ash rests a single walnut-sized lump of black charcoal cracked with glowing red veins, the only warm light in the scene. The monk's open palms are held on either side of the bowl, a hand's width away, sheltering the glow, lit warm from below. A faint grey wisp of smoke curls softly upward from the coal. A small pale moth hovers beside one hand. To the right a narrow window shows a pale grey pre-dawn sky over distant hills; the rest of the room fades into deep shadow. A few sticks of dry kindling lie beside the bowl. Plain dark floor in the lower part of the scene. Hushed, patient, protective stillness.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA robed monk in a coarse woollen habit with a deep cowl sits cross-legged facing the viewer, face lost in the shadow of the cowl. On the floor before the monk stands a simple clay bowl of white ash, and in the ash rests a single walnut-sized lump of black charcoal cracked with glowing red veins, the only warm light in the scene. The monk's open palms are held on either side of the bowl, a hand's width away, sheltering the glow, lit warm from below. A faint grey wisp of smoke curls softly upward from the coal. A small pale moth hovers beside one hand. To the right a narrow window shows a pale grey pre-dawn sky over distant hills; the rest of the room fades into deep shadow. A few sticks of dry kindling lie beside the bowl. Plain dark floor in the lower part of the scene. Hushed, patient, protective stillness.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA robed monk in a coarse woollen habit with a deep cowl sits cross-legged facing the viewer, face lost in the shadow of the cowl. On the floor before the monk stands a simple clay bowl of white ash, and in the ash rests a single walnut-sized lump of black charcoal cracked with glowing red veins, the only warm light in the scene. The monk's open palms are held on either side of the bowl, a hand's width away, sheltering the glow, lit warm from below. A faint grey wisp of smoke curls softly upward from the coal. A small pale moth hovers beside one hand. To the right a narrow window shows a pale grey pre-dawn sky over distant hills; the rest of the room fades into deep shadow. A few sticks of dry kindling lie beside the bowl. Plain dark floor in the lower part of the scene. Hushed, patient, protective stillness.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 600000,
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
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00085_.png, matched to the attached image by pixel comparison (mean difference 1.0 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00086_.png at 54.4). Render date unknown."
}
```

</details>
