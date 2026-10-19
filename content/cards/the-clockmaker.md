---
title: "The Clockmaker"
concept: "Time mastery, precision"
key_terms: ["clockmaker", "clock", "timekeeper"]
created: "2025-12-24"
seed: 509155465
image_status: "present"
prompt_status: "original"
image: "card_the-clockmaker.png"
clip: "the-clockmaker_s6_v2.mp4"
joplin_note: "004fc1f436a841b4b3c594e1bd9e6e36"
---

# The Clockmaker

*An original tarot card in the Rider-Waite tradition*

![The Clockmaker](/media/card_the-clockmaker.png)

## Visual Description

### Composition
An old clockmaker with a white beard, in a mustard shirt and a long leather apron, sits at a heavy wooden workbench under an ivy-covered arch, holding a small brass gear wheel up to the light. On the bench stand a tall wooden case with an open brass gear mechanism and a wooden hourglass, with a few tools and a small candlestick beside them. Behind him a cobbled street of tall grey houses lies in hazy sunlight.

### Symbolism
The gear held to the light is close attention: time understood by taking it apart and studying each small piece. The open mechanism shows that order is made of many parts working together. The hourglass is time that cannot be stopped, only measured and respected. The arch of ivy frames the workshop as a place apart from the busy street, where patient work is done.

### Atmosphere
Bright, hazy daylight above the rooftops. The mood is calm and absorbed, the quiet of skilled hands at work.

## Archetypal Essence

The Clockmaker represents the archetype of the master craftsperson who understands that time is not just to be measured but to be shaped, honored, and worked with as a living force. This card speaks to the profound relationship between precision and patience, reminding us that some things cannot be rushed and that mastery is earned through ten thousand small, careful movements. It teaches that we are all clockmakers in our own lives, setting rhythms and choosing what deserves our most focused attention.

## Render Prompt

```
An old clockmaker in a leather apron over a mustard-yellow shirt sits at a heavy wooden workbench outdoors beneath a vine-covered arbour, holding a small brass gear wheel up to the light between finger and thumb and studying it closely. On the bench stands a large open iron clock mechanism of interlocking toothed gear wheels and a hanging pendulum, beside a wooden hourglass with pale sand running through it. A few tools lie on the bench. Behind him, a sunlit village street with timbered houses. Calm, absorbed mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE CLOCKMAKER" at the bottom.

An elderly figure with nimble, weathered fingers sits at a workshop table crowded with gears, springs, coiled mainsprings, and partially assembled clocks of every size. The Clockmaker wears a jeweler's loupe over one eye and is focused intently on a tiny brass mechanism, holding delicate tools with precise care. Their face shows decades of quiet concentration.

Behind them, the entire wall is covered with hundreds of clocks of all styles — grandfather clocks, cuckoo clocks, carriage clocks, pocket watches pinned to the wall — each showing a different time, all ticking together in a complex polyrhythmic harmony. Some clocks run forward, some backward, and some appear frozen mid-tick. On the table near the Clockmaker's hand, an hourglass flows upward instead of down, sand rising impossibly against gravity.

Through a tall workshop window, multiple phases of the moon appear simultaneously in the same sky — new, crescent, half, gibbous, full — arranged as if time itself has been laid out in the heavens. On the workshop floor, scattered papers show intricate blueprints of escapements and mathematical equations. A pocket watch hangs from the Clockmaker's vest on a fine chain; its face shows not numbers but symbols — seasons, phases of life, planetary signs.

A young apprentice peeks through a doorway at the right edge of the frame, eager but uncertain, not yet invited in. Tools are organized with meticulous precision on hooks and trays; everything has its place.

Atmosphere: warm lamplight in a small, orderly workshop; patient, focused, timeless.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE CLOCKMAKER" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 509155465 · tarot_flux_final_00743_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T16:43:45+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00743_.png`
- Seed: 509155465
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: sun/moon filled from the sky, no AI edit (box [360, 230, 620, 490], grow 14, thresh 18, 2026-10-03T23:23:27+02:00)

```json
{
  "rendered": "2026-10-01T16:43:45+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00743_.png",
  "seed": 509155465,
  "title": "The Clockmaker",
  "scene": "An old clockmaker in a leather apron over a mustard-yellow shirt sits at a heavy wooden workbench outdoors beneath a vine-covered arbour, holding a small brass gear wheel up to the light between finger and thumb and studying it closely. On the bench stands a large open iron clock mechanism of interlocking toothed gear wheels and a hanging pendulum, beside a wooden hourglass with pale sand running through it. A few tools lie on the bench. Behind him, a sunlit village street with timbered houses. Calm, absorbed mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old clockmaker in a leather apron over a mustard-yellow shirt sits at a heavy wooden workbench outdoors beneath a vine-covered arbour, holding a small brass gear wheel up to the light between finger and thumb and studying it closely. On the bench stands a large open iron clock mechanism of interlocking toothed gear wheels and a hanging pendulum, beside a wooden hourglass with pale sand running through it. A few tools lie on the bench. Behind him, a sunlit village street with timbered houses. Calm, absorbed mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old clockmaker in a leather apron over a mustard-yellow shirt sits at a heavy wooden workbench outdoors beneath a vine-covered arbour, holding a small brass gear wheel up to the light between finger and thumb and studying it closely. On the bench stands a large open iron clock mechanism of interlocking toothed gear wheels and a hanging pendulum, beside a wooden hourglass with pale sand running through it. A few tools lie on the bench. Behind him, a sunlit village street with timbered houses. Calm, absorbed mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 509155465,
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
  "repairs": [
    {
      "edited": "2026-10-03T23:23:27+02:00",
      "method": "fill_disc",
      "box": [
        360,
        230,
        620,
        490
      ],
      "grow": 14,
      "disc_pixels": 42956,
      "thresh": 18
    }
  ]
}
```

</details>
