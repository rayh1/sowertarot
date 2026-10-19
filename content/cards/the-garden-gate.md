---
title: "The Garden Gate"
concept: "Entry to paradise, choice"
key_terms: ["garden", "gate"]
created: "2025-12-24"
seed: 454674838
image_status: "present"
prompt_status: "original"
image: "card_the-garden-gate.png"
clip: "the-garden-gate_code_v2.mp4"
joplin_note: "bd8aef6b87964d26a84c686f278fa7f3"
---

# The Garden Gate

*An original tarot card in the Rider-Waite tradition*

![The Garden Gate](/media/card_the-garden-gate.png)

## Visual Description

### Composition
A weathered wooden garden gate stands half open between two grey stone pillars, a pair of iron shears hanging from its latch. On the near side, tall wild grass grows over the threshold and red climbing roses cover the right-hand pillar; fruit trees with small golden fruit lean over the tops of the walls. Through the gateway a path of flat pale stones curves between rounded green hedges, past a freshly planted bed, toward a single tall pine. Bees and white butterflies drift through the air, and a large pale sun hangs above the garden. No person is in sight.

### Symbolism
The half-open gate is an invitation: the way in is offered but not forced, and stepping through is a choice. The wild grass and roses on the near side are untended nature, beautiful but unshaped; the neat hedges and planted bed beyond are what patient tending makes of the same ground. The shears left on the latch are the tool and the work waiting for whoever enters. The empty path says the garden belongs to the one who chooses to walk it. The bees moving freely through the gate are the life that flows between wild and cultivated.

### Atmosphere
Warm late afternoon, a soft blue-green sky and a pale sun. The air is still and humming with bees. The mood is peaceful and inviting.

## Archetypal Essence

The Garden Gate embodies the archetype of the meaningful boundary - the threshold that exists not to keep us out but to make us conscious of our crossing. It represents the truth that some gates stand alone by design, that we create the limits we experience, and that choosing to honor a boundary when we could ignore it is an act of power. This card teaches that what we pay attention to flourishes, and that the garden of our lives grows in the image of what we tend.

## Render Prompt

```
A weathered wooden garden gate stands half open on its iron hinges in an old stone wall, a pair of iron pruning shears hanging from its latch. On the near side of the gate grow wild brambles, tall weeds and tangled red roses. Through the open gateway lies a tended garden of neat green hedges, rows of young seedlings and a pear tree heavy with fruit. A worn path of flat stones leads through the gate. Bees and white butterflies drift through the gateway. Warm late afternoon sun, soft blue sky. Peaceful, inviting mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE GARDEN GATE" at the bottom.

A weathered wooden gate stands alone at the center of an overgrown garden, with no fence or wall attached to either side — it could easily be walked around, yet a winding line of footprints leading up to and through it shows that visitors always choose to walk through. The gate is slightly ajar, neither fully open nor fully closed. Carved into the wooden crossbeam above are the words "WHAT YOU TEND GROWS" in simple serif lettering.

On the left side of the gate, the garden is wild and overgrown: dense brambles, weeds, and tangled wild roses compete for space in riotous disorder, yet there is real beauty in the chaos. On the right side of the gate, the same garden appears in multiple simultaneous stages: one section of perfectly manicured geometric hedges, another of newly planted seedlings in neat rows, and a third section in full autumn harvest with pumpkins and ripe fruit — all coexisting in the same frame.

A soft leather gardener's glove rests on the left gatepost; a pair of well-used pruning shears lies on the right gatepost. Butterflies and honeybees move freely through the gate in both directions. Morning glories climb the gate's wooden slats, their trumpet-shaped blossoms both opening and closing at once along the same vine. On the gate's surface, a small child's handprint is visible in blue paint, and beside it, a much larger and faded older handprint in the same blue.

Atmosphere: late summer afternoon light, warm and golden, quietly miraculous — the boundary as invitation.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE GARDEN GATE" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 454674838 · tarot_flux_final_01316_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-02T09:17:08+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01316_.png`
- Seed: 454674838
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-02T09:17:08+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01316_.png",
  "seed": 454674838,
  "title": "The Garden Gate",
  "scene": "A weathered wooden garden gate stands half open on its iron hinges in an old stone wall, a pair of iron pruning shears hanging from its latch. On the near side of the gate grow wild brambles, tall weeds and tangled red roses. Through the open gateway lies a tended garden of neat green hedges, rows of young seedlings and a pear tree heavy with fruit. A worn path of flat stones leads through the gate. Bees and white butterflies drift through the gateway. Warm late afternoon sun, soft blue sky. Peaceful, inviting mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA weathered wooden garden gate stands half open on its iron hinges in an old stone wall, a pair of iron pruning shears hanging from its latch. On the near side of the gate grow wild brambles, tall weeds and tangled red roses. Through the open gateway lies a tended garden of neat green hedges, rows of young seedlings and a pear tree heavy with fruit. A worn path of flat stones leads through the gate. Bees and white butterflies drift through the gateway. Warm late afternoon sun, soft blue sky. Peaceful, inviting mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA weathered wooden garden gate stands half open on its iron hinges in an old stone wall, a pair of iron pruning shears hanging from its latch. On the near side of the gate grow wild brambles, tall weeds and tangled red roses. Through the open gateway lies a tended garden of neat green hedges, rows of young seedlings and a pear tree heavy with fruit. A worn path of flat stones leads through the gate. Bees and white butterflies drift through the gateway. Warm late afternoon sun, soft blue sky. Peaceful, inviting mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 454674838,
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
