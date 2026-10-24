---
title: "The Weaver"
concept: "Creating destiny, interconnection"
key_terms: ["weaver", "threads", "loom"]
created: "2025-12-24"
seed: 437801600
image_status: "present"
prompt_status: "original"
image: "card_the-weaver.png"
clip: "the-weaver_code_v1.mp4"
joplin_note: "ddc8ad1f05804cb0a5b773286f021f21"
---

# The Weaver

*An original tarot card in the Rider-Waite tradition*

![The Weaver](/media/card_the-weaver.png)

## Visual Description

### Composition
A young woman in a long red woollen dress, her hair in a long braid, sits on a low wooden stool weaving at a tall upright wooden loom outside a stone cottage with a red-tiled roof. She holds a ball of blue yarn and a thin stick up to the warp; the cloth on the loom shows bands of red, yellow and blue above a small woven sun. Baskets of coloured yarn stand at her feet, and green hills roll away behind her under a soft blue-grey sky.

### Symbolism
The weaver is the maker of patterns: each thread small on its own, together forming a whole that none of them could make alone. The loom is the structure that holds the work, the warp of what is given, the weft of what we add. The bands of colour are the different strands of a life woven together. The baskets of yarn are possibility still waiting to be used.

### Atmosphere
Bright, calm daylight over green hills. The mood is calm, steady and purposeful.

## Archetypal Essence

The Weaver embodies the great cosmic principle that nothing exists in isolation - every thread touches every other thread, and a pull on one reverberates through the whole. This card speaks to the creative power we wield when we understand ourselves as both weavers and threads, both creators of the pattern and part of the design. It reminds us that we are always weaving our lives, whether consciously or unconsciously, and that attention to each strand creates beauty in the whole.

## Render Prompt

```
A woman in a deep red woollen dress, her hair in a long braid, sits on a low stool weaving at a tall upright wooden loom set outside a stone cottage, passing a shuttle of golden thread through the warp with one hand. The cloth growing on the loom shows simple bands of crimson, blue, green and gold. Baskets of coloured yarn stand at her feet. A spider's web glistens in the corner of the loom frame. Behind her, rolling green hills under a soft evening sky with a rising moon. Calm, steady, purposeful mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE WEAVER" at the bottom.

An androgynous figure sits cross-legged at the center of the card before an enormous vertical loom that stretches beyond the frame in all directions, upward and to the sides, suggesting infinite expanse. The Weaver's hands move through countless threads of every color — gold, crimson, midnight blue, silver, emerald — some glowing with inner light, others dark and barely visible. The partial tapestry on the loom is impossibly intricate, showing fragmentary images of faces, places, and moments all interconnected in a single weave.

The Weaver wears flowing robes covered in geometric sacred patterns — triangles, spirals, and interlocking lines. Their eyes contain swirling galaxies. Behind them, the workshop fades into deep space: stars and galaxies are visible through the back wall, and some of the loom's threads extend outward to touch distant constellations, as if the tapestry is being woven from the cosmos itself.

At the Weaver's feet, three spindles rest on the floor side by side: one of polished gold (past), one of burnished silver (present), and one of clear crystal (future). In the upper corner of the card, a spider works on a delicate web, mirroring the Weaver's work at smaller scale.

Atmosphere: cosmic, sacred, meditative — the quiet attention of endless patient making.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE WEAVER" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 437801600 · tarot_flux_final_00801_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T17:16:48+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00801_.png`
- Seed: 437801600
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the white sparkling star from the sky in <image1>. Fill its place with the same plain blue-grey sky. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [350, 140, 560, 370], seed 1, output `tarot_qwen21_edit_00033_.png`, 2026-10-02T02:13:56+02:00)
- Repair: sun/moon filled from the sky, no AI edit (box [570, 90, 800, 320], grow 24, thresh 18, 2026-10-03T23:23:35+02:00)

```json
{
  "rendered": "2026-10-01T17:16:48+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00801_.png",
  "seed": 437801600,
  "title": "The Weaver",
  "scene": "A woman in a deep red woollen dress, her hair in a long braid, sits on a low stool weaving at a tall upright wooden loom set outside a stone cottage, passing a shuttle of golden thread through the warp with one hand. The cloth growing on the loom shows simple bands of crimson, blue, green and gold. Baskets of coloured yarn stand at her feet. A spider's web glistens in the corner of the loom frame. Behind her, rolling green hills under a soft evening sky with a rising moon. Calm, steady, purposeful mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA woman in a deep red woollen dress, her hair in a long braid, sits on a low stool weaving at a tall upright wooden loom set outside a stone cottage, passing a shuttle of golden thread through the warp with one hand. The cloth growing on the loom shows simple bands of crimson, blue, green and gold. Baskets of coloured yarn stand at her feet. A spider's web glistens in the corner of the loom frame. Behind her, rolling green hills under a soft evening sky with a rising moon. Calm, steady, purposeful mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA woman in a deep red woollen dress, her hair in a long braid, sits on a low stool weaving at a tall upright wooden loom set outside a stone cottage, passing a shuttle of golden thread through the warp with one hand. The cloth growing on the loom shows simple bands of crimson, blue, green and gold. Baskets of coloured yarn stand at her feet. A spider's web glistens in the corner of the loom frame. Behind her, rolling green hills under a soft evening sky with a rising moon. Calm, steady, purposeful mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 437801600,
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
      "edited": "2026-10-02T02:13:56+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00033_.png",
      "seed": 1,
      "instruction": "Remove the white sparkling star from the sky in <image1>. Fill its place with the same plain blue-grey sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        350,
        140,
        560,
        370
      ],
      "feather": 24,
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
            "image": "tarot_src_9bb2f93c.png"
          },
          "is_changed": [
            "65d8a2ee53d6d9f6c5a7c6d656f725262bb0172fdedb76832176105c9d4b90ed"
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
            "prompt": "Remove the white sparkling star from the sky in <image1>. Fill its place with the same plain blue-grey sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
            "seed": 1,
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
    },
    {
      "edited": "2026-10-03T23:23:35+02:00",
      "method": "fill_disc",
      "box": [
        570,
        90,
        800,
        320
      ],
      "grow": 24,
      "disc_pixels": 34017,
      "thresh": 18
    }
  ]
}
```

</details>
