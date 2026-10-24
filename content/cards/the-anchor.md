---
title: "The Anchor"
concept: "Stability, grounding"
key_terms: ["anchor", "chain", "mooring"]
created: "2025-12-24"
seed: 573733418
image_status: "present"
prompt_status: "original"
image: "card_the-anchor.png"
clip: "the-anchor_code_v6.mp4"
joplin_note: "7868cd7c7c944ead9622dfd5d221d8dc"
---

# The Anchor

*An original tarot card in the Rider-Waite tradition*

![The Anchor](/media/card_the-anchor.png)

## Visual Description

### Composition
A bearded sailor in a long grey canvas coat with a red sash and a plain red knitted cap stands on a sandy shore with one hand resting on a huge old iron anchor. The anchor stands upright on the sand, its crown pressed into it, wound with green vines and small purple flowers, its heavy chain running across the beach. Calm turquoise sea stretches to a tall sailing ship on the horizon. Gulls circle overhead.

### Symbolism
The anchor is stability: what holds us in place while the world moves around us. The hand resting on it is trust in what is solid. The vines and flowers growing over the iron show that what is steady can also become a home for new life. The ship far out at sea is the pull of the voyage, always there, which the anchor makes it safe to wait out.

### Atmosphere
Clear morning light, soft clouds over a calm sea. The mood is steady and grounded.

## Archetypal Essence

The Anchor represents the paradox of security - it is both the thing that saves us from being swept away and the thing that holds us in place. This archetype speaks to our fundamental need for stability and belonging while acknowledging that what grounds us can also bind us. It teaches that true security comes not from never moving but from choosing what to hold onto and what to release, understanding that even the deepest roots can be lifted when the time is right. The Anchor reminds us that we are always tethered to something - the question is whether we have chosen our anchors consciously or drifted into them by default.

## Render Prompt

```
A weathered sailor in a tarred canvas coat and a red knitted cap stands on a sandy shore with one hand resting on a huge old iron anchor that is half sunk in the shallow water beside him. The anchor is crusted with barnacles, and green vines with small purple flowers climb its shank. A thick iron chain runs from the anchor across the sand. Calm turquoise water stretches out to a far sailing ship on the horizon. Gulls circle overhead. Clear morning light, a pale sun low over the sea. Steady, grounded mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE ANCHOR" at the bottom.

A massive iron anchor dominates the center of the card, half-submerged in shallow, crystalline water. The anchor is ancient and barnacle-encrusted, its metal weathered and partially rusted, yet it reads as solid and unwavering. Its heavy chain extends straight up out of the anchor's ring and disappears into soft clouds above.

The water is impossibly clear: through the surface, the anchor's flukes can be seen embedded deep in white sand below, and a small garden of coral and sea anemones has made a home around the buried iron. Small silver fish swim through the anchor's upper ring in a slow circular pattern. Above the waterline, a pair of seabirds has built a nest in the curve of the anchor's shank, and green vines with tiny purple flowers grow along the rusted metal. The chain links ascending into the sky alternate in color — iron link, then gold, then iron, then gold — as they rise toward the clouds.

In the water's surface reflection, a three-masted sailing ship is visible on the horizon — but when looking up at the actual sky, the ship is absent, suggesting memory or possibility rather than present fact.

On the beach at the lower left, a figure stands with one hand laid gently against the anchor's side and the other hand reaching toward the horizon. The sky is split: on the left, dark storm clouds retreat; on the right, clear open sky emerges into pale gold. Carved into the anchor's crossbar are countless tiny symbols and names, evidence of many travelers who have passed and left their mark.

Atmosphere: the perfect pause between storm and calm; grounded stillness with the pull of horizon.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE ANCHOR" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 573733418 · tarot_flux_final_00659_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T15:54:22+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00659_.png`
- Seed: 573733418
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Replace the man's red bobble beanie in <image1> with a plain close-fitting red knitted woollen cap with a rolled brim and no bobble on top. Keep his face, hair and beard the same. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [240, 290, 430, 470], seed 1, output `tarot_qwen21_edit_00030_.png`, 2026-10-02T01:53:05+02:00)
- Repair: sun/moon filled from the sky, no AI edit (box [330, 80, 690, 410], grow 14, thresh 45, 2026-10-03T23:23:59+02:00)
- Repair: light rim round the linework filled from the sky, no AI edit (box [400, 140, 620, 265], grow 2, 2026-10-24T14:10:59+02:00)
- Repair: Remove the short dangling string of dark beads hanging at the man's hip below the end of his red sash in <image1>. Fill its place with the back edge of his grey coat and the turquoise sea behind it. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [355, 770, 425, 890], seed 1, output `tarot_qwen21_edit_00067_.png`, tone-matched, 2026-10-24T13:44:21+02:00)
- Repair: Remove the small round metal ring threaded on the green vine at the left side of the anchor shank in <image1>. The vine continues as one smooth curving dark stem with its yellow-green leaves, on the plain sand. Keep the anchor the same. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [520, 1210, 650, 1340], seed 3, output `tarot_qwen21_edit_00078_.png`, tone-matched, 2026-10-24T14:13:49+02:00)
- Note: 2026-10-24: replaying the base workflow no longer reproduces this picture (the FLUX render drifted: it draws a chain over the anchor). The art after the fill_disc repair is dropbox:Tarot/seed-sheets/discs/the-anchor_f_art.png; the art after all repairs is dropbox:Tarot/animations/source/procedural/the-anchor_full_art.png. Edit those, not a replay.

```json
{
  "rendered": "2026-10-01T15:54:22+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00659_.png",
  "seed": 573733418,
  "title": "The Anchor",
  "scene": "A weathered sailor in a tarred canvas coat and a red knitted cap stands on a sandy shore with one hand resting on a huge old iron anchor that is half sunk in the shallow water beside him. The anchor is crusted with barnacles, and green vines with small purple flowers climb its shank. A thick iron chain runs from the anchor across the sand. Calm turquoise water stretches out to a far sailing ship on the horizon. Gulls circle overhead. Clear morning light, a pale sun low over the sea. Steady, grounded mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA weathered sailor in a tarred canvas coat and a red knitted cap stands on a sandy shore with one hand resting on a huge old iron anchor that is half sunk in the shallow water beside him. The anchor is crusted with barnacles, and green vines with small purple flowers climb its shank. A thick iron chain runs from the anchor across the sand. Calm turquoise water stretches out to a far sailing ship on the horizon. Gulls circle overhead. Clear morning light, a pale sun low over the sea. Steady, grounded mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA weathered sailor in a tarred canvas coat and a red knitted cap stands on a sandy shore with one hand resting on a huge old iron anchor that is half sunk in the shallow water beside him. The anchor is crusted with barnacles, and green vines with small purple flowers climb its shank. A thick iron chain runs from the anchor across the sand. Calm turquoise water stretches out to a far sailing ship on the horizon. Gulls circle overhead. Clear morning light, a pale sun low over the sea. Steady, grounded mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 573733418,
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
      "edited": "2026-10-02T01:53:05+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00030_.png",
      "seed": 1,
      "instruction": "Replace the man's red bobble beanie in <image1> with a plain close-fitting red knitted woollen cap with a rolled brim and no bobble on top. Keep his face, hair and beard the same. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        240,
        290,
        430,
        470
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
            "image": "tarot_src_5e263506.png"
          },
          "is_changed": [
            "6e356a65c4629a4c2c41f9a630d97bde5d82572597e7ec4e4adabff27ebd91a5"
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
            "prompt": "Replace the man's red bobble beanie in <image1> with a plain close-fitting red knitted woollen cap with a rolled brim and no bobble on top. Keep his face, hair and beard the same. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-03T23:23:59+02:00",
      "method": "fill_disc",
      "box": [
        330,
        80,
        690,
        410
      ],
      "grow": 14,
      "disc_pixels": 50903,
      "thresh": 45
    },
    {
      "edited": "2026-10-24T14:10:59+02:00",
      "method": "fill_halo",
      "box": [
        400,
        140,
        620,
        265
      ],
      "grow": 2,
      "rim_pixels": 3327
    },
    {
      "edited": "2026-10-24T13:44:21+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00067_.png",
      "seed": 1,
      "instruction": "Remove the short dangling string of dark beads hanging at the man's hip below the end of his red sash in <image1>. Fill its place with the back edge of his grey coat and the turquoise sea behind it. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        355,
        770,
        425,
        890
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        -43.8,
        -87.9,
        -77.7
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
            "image": "tarot_src_d45337fc.png"
          },
          "is_changed": [
            "b47d92167b3cc0db8de041791af801e1cc0abe1227eb4e049314eda1626fd25d"
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
            "prompt": "Remove the short dangling string of dark beads hanging at the man's hip below the end of his red sash in <image1>. Fill its place with the back edge of his grey coat and the turquoise sea behind it. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T14:13:49+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00078_.png",
      "seed": 3,
      "instruction": "Remove the small round metal ring threaded on the green vine at the left side of the anchor shank in <image1>. The vine continues as one smooth curving dark stem with its yellow-green leaves, on the plain sand. Keep the anchor the same. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        520,
        1210,
        650,
        1340
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        2.2,
        3.2,
        1.6
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
            "image": "tarot_src_77692a1c.png"
          },
          "is_changed": [
            "b47d92167b3cc0db8de041791af801e1cc0abe1227eb4e049314eda1626fd25d"
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
            "prompt": "Remove the small round metal ring threaded on the green vine at the left side of the anchor shank in <image1>. The vine continues as one smooth curving dark stem with its yellow-green leaves, on the plain sand. Keep the anchor the same. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
            "seed": 3,
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
  ],
  "note": "2026-10-24: replaying the base workflow no longer reproduces this picture (the FLUX render drifted: it draws a chain over the anchor). The art after the fill_disc repair is dropbox:Tarot/seed-sheets/discs/the-anchor_f_art.png; the art after all repairs is dropbox:Tarot/animations/source/procedural/the-anchor_full_art.png. Edit those, not a replay."
}
```

</details>
