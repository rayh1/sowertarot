---
title: "The Well"
concept: "Deep wisdom, nourishment"
key_terms: ["well", "bucket", "water source"]
created: "2025-12-24"
seed: 477967108
image_status: "present"
prompt_status: "original"
image: "card_the-well.png"
clip: "the-well_s6_v2.mp4"
joplin_note: "b8b3b5812d4147eb837b844e03904777"
---

# The Well

*An original tarot card in the Rider-Waite tradition*

![The Well](/media/card_the-well.png)

## Visual Description

### Composition
A young woman in a long russet dress with rolled sleeves stands at a round stone well in open grassland, drawing water. One hand grips the rope where it runs up to a wooden crossbeam; the other steadies a copper bucket that pours a stream of clear water back into the well. A small copper cup hangs below a hook on the beam, just above her raised hand. A bare old tree leans in from the left, its branches spreading across the sky. Low rolling hills lie behind her.

### Symbolism
The well is the deep inner source: what sustains us lies below the surface and must be drawn up by deliberate effort. The rope is the work of reaching down and the trust that something waits there; the overflowing bucket is the reward, water brought up into the light. The hanging cup is readiness to share what is drawn. The crescent moon marks the hidden, intuitive side of wisdom; the bare tree is patience and endurance through dry seasons.

### Atmosphere
Twilight deepening into night: a dark teal sky with a thin crescent moon and the first stars. The grass still holds the last pale light. The mood is quiet, steady and reverent, the stillness of a daily act done with care.

## Archetypal Essence

The Well represents the archetype of the deep inner source—the place within each of us that holds accumulated wisdom, hidden truths, and life-sustaining resources. Unlike a spring that bubbles up spontaneously, the well requires the deliberate act of lowering the bucket into darkness, trusting there is something valuable below, and doing the work to draw it back up into the light. This card reminds us that the most essential truths and the most nourishing waters often lie in our deepest, darkest places, and that we must be willing to regularly descend into ourselves to bring forth what we and others need.

## Render Prompt

```
A young woman in a russet woollen kirtle with rolled sleeves hauls a wooden bucket up out of an old round stone well, both hands gripping the wet rope, water spilling over the bucket's rim. The well stands on a small grassy rise, its grey stones patched with green moss, a wooden crossbeam above it with a copper cup hanging from an iron hook. Behind her an old willow bends its long silver-green branches down toward the well. Low rolling hills in the distance. Twilight sky of deep blue fading to pale gold at the horizon, a thin crescent moon and the first stars above. Quiet, reverent mood; the drawn water catches the last light.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE WELL" at the bottom.

An ancient circular stone well sits at the exact center of the card. Its round opening is bordered by weathered gray stones covered in soft green moss and climbing ivy. A simple wooden bucket hangs on a worn hemp rope resting on the stone rim, water still dripping slowly from its lower edge. Looking down into the well reveals only darkness with a single distant point of light far below — like a star glowing at the bottom of the world.

Around the well, the ground is composed of smooth round river stones arranged in meditative concentric circles. Seven worn stone steps lead down to the central well platform from the foreground, suggesting this is a place of repeated pilgrimage. To the left of the well, a small polished copper cup hangs from an iron hook, its surface worn smooth by countless hands. To the right, fresh wildflowers have been placed as recent offerings: yarrow, forget-me-nots, and white clover laid carefully on the stone.

Behind the well, an old willow tree bends its graceful long branches down toward the stone rim, as if the tree itself is drinking from the ancient source. The willow's leaves are silver-green and trembling gently. The sky overhead is twilight — neither day nor night — deep blue-violet with the first few stars just beginning to appear.

The well's outer stones are carved with worn sacred symbols: spirals, crescent moons, and curved wave-forms flowing in an endless circle around the rim. In the water inside the bucket, the reflections shimmer not of the sky above but of depths below — suggesting this is a well that shows inner truth rather than surface appearance.

Atmosphere: hush of dusk, contemplative reverence, ancient and still.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE WELL" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 477967108 · tarot_flux_final_00280_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T00:51:11+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00280_.png`
- Seed: 477967108
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-01T00:51:11+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00280_.png",
  "seed": 477967108,
  "title": "The Well",
  "scene": "A young woman in a russet woollen kirtle with rolled sleeves hauls a wooden bucket up out of an old round stone well, both hands gripping the wet rope, water spilling over the bucket's rim. The well stands on a small grassy rise, its grey stones patched with green moss, a wooden crossbeam above it with a copper cup hanging from an iron hook. Behind her an old willow bends its long silver-green branches down toward the well. Low rolling hills in the distance. Twilight sky of deep blue fading to pale gold at the horizon, a thin crescent moon and the first stars above. Quiet, reverent mood; the drawn water catches the last light.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a russet woollen kirtle with rolled sleeves hauls a wooden bucket up out of an old round stone well, both hands gripping the wet rope, water spilling over the bucket's rim. The well stands on a small grassy rise, its grey stones patched with green moss, a wooden crossbeam above it with a copper cup hanging from an iron hook. Behind her an old willow bends its long silver-green branches down toward the well. Low rolling hills in the distance. Twilight sky of deep blue fading to pale gold at the horizon, a thin crescent moon and the first stars above. Quiet, reverent mood; the drawn water catches the last light.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a russet woollen kirtle with rolled sleeves hauls a wooden bucket up out of an old round stone well, both hands gripping the wet rope, water spilling over the bucket's rim. The well stands on a small grassy rise, its grey stones patched with green moss, a wooden crossbeam above it with a copper cup hanging from an iron hook. Behind her an old willow bends its long silver-green branches down toward the well. Low rolling hills in the distance. Twilight sky of deep blue fading to pale gold at the horizon, a thin crescent moon and the first stars above. Quiet, reverent mood; the drawn water catches the last light.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 477967108,
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
