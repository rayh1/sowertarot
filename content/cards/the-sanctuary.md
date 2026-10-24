---
title: "The Sanctuary"
concept: "Sacred refuge, spiritual protection"
key_terms: ["sanctuary", "refuge", "temple", "sacred space", "haven"]
created: "2026-01-06"
seed: 601734569
image_status: "present"
prompt_status: "original"
image: "card_the-sanctuary.png"
clip: "the-sanctuary_code_v1.mp4"
joplin_note: "a0ece8c6d6e94d838428ca2f6547daa1"
---

# The Sanctuary

*An original tarot card in the Rider-Waite tradition*

![The Sanctuary](/media/card_the-sanctuary.png)

## Visual Description

### Composition
A small round shrine of white stone with a plain dome and a small round knob on top stands among tall dark cypresses. In its open arched doorway an old keeper with a white beard, in a plain undyed habit, stands facing us and raises a small flame on a short handle in welcome, warm golden light glowing from the room behind him. Worn stone steps lead down toward us. Tall stems of white roses grow beside the walls, and a stone basin stands beside the steps.

### Symbolism
The sanctuary is refuge: a place set apart where the weary can rest and be restored. The keeper facing us with his flame raised is welcome freely given, the host who waits for the traveller. The steps are the last effort of the journey before rest. The basin of water is cleansing and renewal. The cypresses, evergreen and watchful, are protection and endurance.

### Atmosphere
Evening, a rose and violet sky behind the dark trees, warm light from the doorway. The mood is safe, welcoming and peaceful.

## Archetypal Essence

The Sanctuary represents the universal human need for sacred refuge—a place untouched by the profane demands of the world where the soul can rest and renew. It embodies the temple within, that inviolable core of self that remains pure regardless of external circumstances. This card reminds us that true sanctuary is not merely physical but a state of consciousness, a deliberate turning inward to reconnect with the divine source. It teaches that we must sometimes withdraw from the world not to escape it, but to gather the spiritual strength needed to engage with it authentically.

## Render Prompt

```
Close view: an old keeper with a white beard, in a plain undyed wool habit, stands on the top step just outside the open arched doorway of a small round shrine of white stone, turned toward us with his face and chest to the viewer, smiling, holding up a lit oil lamp in his right hand in welcome. Warm golden light glows from the room behind him and outlines his shoulders. Worn stone steps lead down toward us. White climbing roses grow up the walls, and a small spring flows into a stone basin beside the steps. The shrine's low dome is plain smooth white stone with a rounded top. Tall dark cypress trees stand on both sides against a soft rose and violet evening sky. Safe, welcoming mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE SANCTUARY" at the bottom.

A white marble domed temple with an open archway entrance stands at the center, glowing with inner radiance. Two alabaster columns carved with ascending spiral vines and white roses frame the entrance. Golden light emanates from within the temple. The temple sits on a circular platform with seven rainbow-colored steps (red to violet from bottom to top).

At the base of the platform, a clear spring bubbles forth with four streams flowing toward the cardinal directions. Four tall dark green cypress trees stand at the north, south, east, and west points around the temple. The sky transitions from deep indigo with stars at the top to soft lavender at the horizon, suggesting dawn or dusk.

In the foreground, a figure in a simple white robe kneels at the bottom step with head bowed and hands pressed together in prayer. The figure is barefoot. A white dove perches on the temple's dome with wings slightly spread.

Additional details: oil lamps burning at the entrance, white lilies growing near the spring, a faint rainbow arc in the misty air around the temple.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE SANCTUARY" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 601734569 · tarot_flux_final_00045_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-03T23:53:02+02:00 · ComfyUI 0.38.0 · output `tarot_flux_final_00045_.png`
- Seed: 601734569
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-03T23:53:02+02:00",
  "comfyui_version": "0.38.0",
  "comfy_file": "tarot_flux_final_00045_.png",
  "seed": 601734569,
  "title": "The Sanctuary",
  "scene": "Close view: an old keeper with a white beard, in a plain undyed wool habit, stands on the top step just outside the open arched doorway of a small round shrine of white stone, turned toward us with his face and chest to the viewer, smiling, holding up a lit oil lamp in his right hand in welcome. Warm golden light glows from the room behind him and outlines his shoulders. Worn stone steps lead down toward us. White climbing roses grow up the walls, and a small spring flows into a stone basin beside the steps. The shrine's low dome is plain smooth white stone with a rounded top. Tall dark cypress trees stand on both sides against a soft rose and violet evening sky. Safe, welcoming mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nClose view: an old keeper with a white beard, in a plain undyed wool habit, stands on the top step just outside the open arched doorway of a small round shrine of white stone, turned toward us with his face and chest to the viewer, smiling, holding up a lit oil lamp in his right hand in welcome. Warm golden light glows from the room behind him and outlines his shoulders. Worn stone steps lead down toward us. White climbing roses grow up the walls, and a small spring flows into a stone basin beside the steps. The shrine's low dome is plain smooth white stone with a rounded top. Tall dark cypress trees stand on both sides against a soft rose and violet evening sky. Safe, welcoming mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nClose view: an old keeper with a white beard, in a plain undyed wool habit, stands on the top step just outside the open arched doorway of a small round shrine of white stone, turned toward us with his face and chest to the viewer, smiling, holding up a lit oil lamp in his right hand in welcome. Warm golden light glows from the room behind him and outlines his shoulders. Worn stone steps lead down toward us. White climbing roses grow up the walls, and a small spring flows into a stone basin beside the steps. The shrine's low dome is plain smooth white stone with a rounded top. Tall dark cypress trees stand on both sides against a soft rose and violet evening sky. Safe, welcoming mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 601734569,
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
