---
title: "The Threshold"
concept: "Liminal space, transition"
key_terms: ["threshold", "doorway"]
created: "2025-12-24"
seed: 113988557
image_status: "present"
prompt_status: "original"
image: "card_the-threshold.png"
clip: "the-threshold_code_v3.mp4"
joplin_note: "e78799a2d0b04e1481586e618efae07d"
---

# The Threshold

*An original tarot card in the Rider-Waite tradition*

![The Threshold](/media/card_the-threshold.png)

## Visual Description

### Composition
A young man in a long purple cloak stands just inside an old stone archway, holding a large iron key. Beyond the arch a pale stone path winds into a misty forest of tall bare trees. A black cat walks out through the doorway at his feet, and a black raven perches on a branch inside the arch. Ivy climbs the weathered stones.

### Symbolism
The archway is the threshold between the known and the unknown. The key is the power to cross and the choice to use it. The cat walking out ahead is instinct that already moves where the mind still hesitates. The raven watching from above is the messenger of change. The misty path shows that what lies ahead can only be seen by walking it.

### Atmosphere
Early dawn, the forest pale and misty, light growing at the end of the path. The mood is expectant and hesitant, the pause before a step.

## Archetypal Essence

The Threshold represents the liminal space between what was and what will be, a place of tremendous power and profound uncertainty. This is the archetype of transition itself - neither here nor there, but in the sacred pause where old identities dissolve and new ones have not yet formed. It teaches us that doorways are not just passages but destinations unto themselves, and that standing at the edge is sometimes exactly where we need to be.

## Render Prompt

```
A young man in a deep purple travelling cloak stands in the open doorway of a ruined stone chapel, one foot stepping out from the worn flagstones onto wild grass, an iron key held in one hand. Ivy climbs the stone doorframe. Before him lies an untamed forest at dawn, with mist curling between tall old trees and a faint path leading in. A black cat walks out through the doorway at his feet. A black raven perches on top of the doorframe. Soft pale dawn light. Expectant, hesitant mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE THRESHOLD" at the bottom.

A figure stands at the center of an ancient stone doorway, one foot on marble tiles and the other on wild grass. They wear a cloak split down the center — deep purple on the left side, forest green on the right — and their face is turned neither left nor right but gazes directly forward at the viewer. Their hands are extended outward: the left hand holds an ornate brass key, the right hand holds a small brass compass.

The left side of the archway opens into a grand candlelit hallway with familiar furniture and portraits on the walls, suggesting the known and domestic. The right side of the archway reveals an untamed forest at dawn, with cool mist curling between ancient trees and a barely visible path leading deeper in.

Above the archway, two ravens perch on either side — one black on the left, one white on the right. Vines grow up the doorframe bearing both dying autumn leaves and fresh spring buds on the same twining stems. At the figure's feet, a cat walks through the doorway mid-stride, caught between both worlds.

Atmosphere: the sacred pause, neither here nor there. Warm candlelight on the left; cool dawn mist on the right; the figure illuminated evenly by both.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE THRESHOLD" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 113988557 · tarot_flux_final_00823_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T17:29:19+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00823_.png`
- Seed: 113988557
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the brown bird perched on top of the right pillar's capital, half sunk into the arch stones. Fill its place with the same dark shadow of the arch's inner side and the edge of the arch stones. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [792, 462, 885, 648], seed 2, output `tarot_qwen21_edit_00159_.png`, tone-matched, 2026-10-24T19:29:09+02:00)

```json
{
  "rendered": "2026-10-01T17:29:19+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00823_.png",
  "seed": 113988557,
  "title": "The Threshold",
  "scene": "A young man in a deep purple travelling cloak stands in the open doorway of a ruined stone chapel, one foot stepping out from the worn flagstones onto wild grass, an iron key held in one hand. Ivy climbs the stone doorframe. Before him lies an untamed forest at dawn, with mist curling between tall old trees and a faint path leading in. A black cat walks out through the doorway at his feet. A black raven perches on top of the doorframe. Soft pale dawn light. Expectant, hesitant mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young man in a deep purple travelling cloak stands in the open doorway of a ruined stone chapel, one foot stepping out from the worn flagstones onto wild grass, an iron key held in one hand. Ivy climbs the stone doorframe. Before him lies an untamed forest at dawn, with mist curling between tall old trees and a faint path leading in. A black cat walks out through the doorway at his feet. A black raven perches on top of the doorframe. Soft pale dawn light. Expectant, hesitant mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young man in a deep purple travelling cloak stands in the open doorway of a ruined stone chapel, one foot stepping out from the worn flagstones onto wild grass, an iron key held in one hand. Ivy climbs the stone doorframe. Before him lies an untamed forest at dawn, with mist curling between tall old trees and a faint path leading in. A black cat walks out through the doorway at his feet. A black raven perches on top of the doorframe. Soft pale dawn light. Expectant, hesitant mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 113988557,
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
      "edited": "2026-10-24T19:29:09+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00159_.png",
      "seed": 2,
      "instruction": "Remove the brown bird perched on top of the right pillar's capital, half sunk into the arch stones. Fill its place with the same dark shadow of the arch's inner side and the edge of the arch stones. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        792,
        462,
        885,
        648
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        2.8,
        2.6,
        0.1
      ],
      "workflow": {
        "1": {
          "class_type": "UNETLoader",
          "inputs": {
            "unet_name": "qwen_image_2.1_int8_convrot.safetensors",
            "weight_dtype": "default"
          }
        },
        "2": {
          "class_type": "CLIPLoader",
          "inputs": {
            "clip_name": "qwen3vl_8b_int8_convrot.safetensors",
            "type": "qwen_image",
            "device": "default"
          }
        },
        "3": {
          "class_type": "VAELoader",
          "inputs": {
            "vae_name": "qwen_image_2.1_vae_bf16.safetensors"
          }
        },
        "4": {
          "class_type": "QwenImage21Cache",
          "inputs": {
            "model": [
              "1",
              0
            ],
            "device": "auto",
            "dtype": "default"
          }
        },
        "5": {
          "class_type": "LoadImage",
          "inputs": {
            "image": "tarot_src_fcb4eaee.png"
          },
          "is_changed": [
            "794f3209a37da18d534e8464dc3521cc263b0c1f2be5e0f7b89ca145b62eb228"
          ]
        },
        "6": {
          "class_type": "TextEncodeQwenImage21",
          "inputs": {
            "clip": [
              "2",
              0
            ],
            "vae": [
              "3",
              0
            ],
            "prompt": "Remove the brown bird perched on top of the right pillar's capital, half sunk into the arch stones. Fill its place with the same dark shadow of the arch's inner side and the edge of the arch stones. Keep everything else, including the woodcut linework and hatching, exactly the same.",
            "negative_prompt": "",
            "resolution": 0,
            "images.image_1": [
              "5",
              0
            ]
          }
        },
        "7": {
          "class_type": "KSampler",
          "inputs": {
            "model": [
              "4",
              0
            ],
            "positive": [
              "6",
              0
            ],
            "negative": [
              "6",
              1
            ],
            "latent_image": [
              "6",
              2
            ],
            "seed": 2,
            "steps": 40,
            "cfg": 1.0,
            "sampler_name": "euler",
            "scheduler": "simple",
            "denoise": 1.0
          }
        },
        "8": {
          "class_type": "VAEDecode",
          "inputs": {
            "samples": [
              "7",
              0
            ],
            "vae": [
              "3",
              0
            ]
          }
        },
        "9": {
          "class_type": "SaveImage",
          "inputs": {
            "images": [
              "8",
              0
            ],
            "filename_prefix": "tarot_qwen21_edit"
          }
        }
      }
    }
  ]
}
```

</details>
