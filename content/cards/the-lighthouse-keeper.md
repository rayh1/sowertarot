---
title: "The Lighthouse Keeper"
concept: "Solitary guide, service through isolation"
key_terms: ["lighthouse", "keeper", "beacon", "fresnel", "vigil", "storm petrel"]
created: "2026-04-20"
seed: 212431655
image_status: "present"
prompt_status: "original"
image: "card_the-lighthouse-keeper.png"
clip: "the-lighthouse-keeper_code_v1.mp4"
joplin_note: "bd4cbb7331624f8b9d8d592a7a7ad806"
---

# The Lighthouse Keeper

*An original tarot card in the Rider-Waite tradition*

![The Lighthouse Keeper](/media/card_the-lighthouse-keeper.png)

## Visual Description

### Composition
A keeper in a dark blue coat stands on the iron gallery at the top of a tall stone lighthouse, beside the great lamp that throws broad beams of pale light across the sky. The tower rises from a steep rocky headland, with waves breaking white on black rocks below. Out at sea a tall sailing ship heads toward the light. Clouds drift across the night sky.

### Symbolism
The lighthouse keeper is the solitary guide: his work is to keep the light burning so that others, whom he will never meet, find their way safely. The beam is guidance given freely. The ship steering by it is everyone who relies on that steady service. The isolated tower on the rocks is the cost and the strength of serving alone.

### Atmosphere
Night, a dark sky with drifting clouds, the sea dark and restless. The mood is watchful and steadfast.

## Archetypal Essence

The Lighthouse Keeper represents the archetype of purposeful solitude: a life whose meaning arises from being steadily useful to strangers one will never meet. This card speaks to the dignity of unseen work, to the watchfulness that stays unblinking through every hour no one is looking, and to the particular loneliness that arises from occupying a post no one else will take. The Lighthouse Keeper teaches that isolation, when chosen in service of something beyond oneself, stops being deprivation and becomes a form of love cast outward into the dark.

## Render Prompt

```
An old lighthouse keeper in a heavy navy oilskin coat stands on the narrow iron gallery that runs around the top of a tall stone lighthouse, holding a lit lantern and looking out to sea. Above him, the great lamp throws a broad beam of pale light across the dark water. Far out, a small sailing ship rides the rough swell, heading toward the light. Below, white foam breaks against black rocks at the foot of the tower. Night sky with a half moon between dark clouds. Watchful, steadfast mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE LIGHTHOUSE KEEPER" at the bottom.

A figure in a weathered navy blue cloak stands at the top of a stone lighthouse, their back to the viewer as they face the open sea through the curved glass windows of the lamp chamber. The brass Fresnel lens machinery and angled mirrors of the great light are visible around them, catching moonlight. A narrow iron spiral staircase descends into shadow below. In the far distance a small ship rides rough swells, steering toward the beam.

The lighthouse rises from a jagged promontory with white foam breaking against black rock. An unlit oil lantern hangs from the keeper's belt. Their hands rest on a wooden railing worn smooth by years of vigil. A single storm petrel perches on the railing beside them, unbothered by the wind. The keeper's face is visible in three-quarter profile, neither young nor old, lined with long watching; a wedding band glints on one hand. Seven gulls wheel below in the beam's halo. A brass logbook lies open on a small ledge, pages heavy with ink.

Late night into the darkest hour: deep indigo sky overhead fading to slate at the horizon, a single breaking star just visible. Warm gold beacon light cutting through bands of grey fog.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE LIGHTHOUSE KEEPER" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 212431655 · tarot_flux_final_01128_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T22:00:48+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01128_.png`
- Seed: 212431655
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: sun/moon filled from the sky, no AI edit (box [235, 390, 475, 630], grow 24, thresh 18, 2026-10-03T23:23:50+02:00)

```json
{
  "rendered": "2026-10-01T22:00:48+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01128_.png",
  "seed": 212431655,
  "title": "The Lighthouse Keeper",
  "scene": "An old lighthouse keeper in a heavy navy oilskin coat stands on the narrow iron gallery that runs around the top of a tall stone lighthouse, holding a lit lantern and looking out to sea. Above him, the great lamp throws a broad beam of pale light across the dark water. Far out, a small sailing ship rides the rough swell, heading toward the light. Below, white foam breaks against black rocks at the foot of the tower. Night sky with a half moon between dark clouds. Watchful, steadfast mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old lighthouse keeper in a heavy navy oilskin coat stands on the narrow iron gallery that runs around the top of a tall stone lighthouse, holding a lit lantern and looking out to sea. Above him, the great lamp throws a broad beam of pale light across the dark water. Far out, a small sailing ship rides the rough swell, heading toward the light. Below, white foam breaks against black rocks at the foot of the tower. Night sky with a half moon between dark clouds. Watchful, steadfast mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old lighthouse keeper in a heavy navy oilskin coat stands on the narrow iron gallery that runs around the top of a tall stone lighthouse, holding a lit lantern and looking out to sea. Above him, the great lamp throws a broad beam of pale light across the dark water. Far out, a small sailing ship rides the rough swell, heading toward the light. Below, white foam breaks against black rocks at the foot of the tower. Night sky with a half moon between dark clouds. Watchful, steadfast mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 212431655,
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
      "edited": "2026-10-03T23:23:50+02:00",
      "method": "fill_disc",
      "box": [
        235,
        390,
        475,
        630
      ],
      "grow": 24,
      "disc_pixels": 44527,
      "thresh": 18
    }
  ]
}
```

</details>
