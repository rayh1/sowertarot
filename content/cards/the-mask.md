---
title: "The Mask"
concept: "Many honest roles, one chooser"
key_terms: ["mask", "persona", "player", "roles", "many faces", "stage"]
created: "2026-10-10"
seed: 141592
image_status: "present"
prompt_status: "original"
image: "card_the-mask.png"
clip: "the-mask_code_v2.mp4"
joplin_note: "a6649b304ef045d7a0ccd74b60a36919"
---

# The Mask

*An original tarot card in the Rider-Waite tradition*

![The Mask](/media/card_the-mask.png)

## Visual Description

### Composition
A travelling player stands at the centre of a small wooden stage-cart, turned three-quarters toward the viewer. He holds a carved wooden mask out at arm's length in his right hand and studies its face; his own face is bare, calm and open. Further along the boards lie three more masks, one pale and serene, one ochre and smiling, one pale and sorrowful, beside a red curtain-cloth hung over a rail at the back of the cart. Behind, a village green with a few thatched cottages and a line of trees recedes under an evening sky.

### Symbolism
The mask held at arm's length is a role seen from outside: worn, but not mistaken for the self. The bare face between the masks is the one who chooses. The smiling and sorrowful masks are the old twin faces of the stage, comedy and tragedy, lying side by side as equally true. The ochre and green doublet joins earth and growth: the player is a worker, not a trickster. The red curtain-cloth, taken down from its place, marks the line between stage and life, and shows that the line can be crossed both ways. The village behind is the audience, the community each role serves.

### Atmosphere
Dusk after the performance, under soft grey clouds and pale fading light. The mood is quiet and thoughtful, neither triumphant nor sad: the moment between one role and the next.

## Archetypal Essence

The Mask is the archetype of the persona: the faces a person wears to meet the world, and the self who wears them. It holds that one life contains many honest roles (parent, worker, friend, stranger) and that each shows a true facet without being the whole. Its wisdom is neither tearing the masks off nor hiding behind them, but holding each at arm's length long enough to choose it freely. It is the card of the actor, the diplomat and anyone who must be many things to many people and still know whose hand holds the mask.

## Render Prompt

```
A travelling player stands on the wooden boards of a small stage-cart and holds a carved wooden mask out at arm's length in his right hand, studying its face, his own bare face calm and open. He wears a patched doublet of ochre and green with puffed sleeves, dark hose and soft leather boots. The mask is pale with a serene painted expression and a ribbon tie hanging from it. On the boards at his feet lie two more masks, one laughing and one weeping. A half-drawn red curtain hangs at the back of the cart. Behind, a village green with a few thatched cottages and a line of trees under a pale evening sky of soft grey clouds. Quiet, thoughtful dusk.
```

## Render Record

<details>
<summary>Seed 141592 · tarot_flux_final_01607_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-10T12:02:20+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01607_.png`
- Seed: 141592
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0)
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`

```json
{
  "rendered": "2026-10-10T12:02:20+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01607_.png",
  "seed": 141592,
  "title": "The Mask",
  "scene": "A travelling player stands on the wooden boards of a small stage-cart and holds a carved wooden mask out at arm's length in his right hand, studying its face, his own bare face calm and open. He wears a patched doublet of ochre and green with puffed sleeves, dark hose and soft leather boots. The mask is pale with a serene painted expression and a ribbon tie hanging from it. On the boards at his feet lie two more masks, one laughing and one weeping. A half-drawn red curtain hangs at the back of the cart. Behind, a village green with a few thatched cottages and a line of trees under a pale evening sky of soft grey clouds. Quiet, thoughtful dusk.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA travelling player stands on the wooden boards of a small stage-cart and holds a carved wooden mask out at arm's length in his right hand, studying its face, his own bare face calm and open. He wears a patched doublet of ochre and green with puffed sleeves, dark hose and soft leather boots. The mask is pale with a serene painted expression and a ribbon tie hanging from it. On the boards at his feet lie two more masks, one laughing and one weeping. A half-drawn red curtain hangs at the back of the cart. Behind, a village green with a few thatched cottages and a line of trees under a pale evening sky of soft grey clouds. Quiet, thoughtful dusk.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA travelling player stands on the wooden boards of a small stage-cart and holds a carved wooden mask out at arm's length in his right hand, studying its face, his own bare face calm and open. He wears a patched doublet of ochre and green with puffed sleeves, dark hose and soft leather boots. The mask is pale with a serene painted expression and a ribbon tie hanging from it. On the boards at his feet lie two more masks, one laughing and one weeping. A half-drawn red curtain hangs at the back of the cart. Behind, a village green with a few thatched cottages and a line of trees under a pale evening sky of soft grey clouds. Quiet, thoughtful dusk.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 141592,
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
