---
title: "The Forge"
concept: "Creation through fire, tempering"
key_terms: ["forge", "blacksmith", "anvil"]
created: "2025-12-24"
seed: 435889
image_status: "present"
prompt_status: "original"
image: "card_the-forge.png"
clip: "the-forge_5b_strong_s2_v2.mp4"
joplin_note: "ff58830924384b6a96609a4fc19e7e10"
---

# The Forge

*An original tarot card in the Rider-Waite tradition*

![The Forge](/media/card_the-forge.png)

## Visual Description

A muscular figure stands before a roaring forge, their face illuminated by orange and crimson flames that dance within a tall arched stone hearth. The blacksmith holds a glowing piece of metal on an anvil with iron tongs, their other hand holding a heavy hammer ready at chest height. Sparks cascade like golden rain, frozen in mid-air, each one catching the firelight. The blacksmith wears a leather apron scarred with burn marks and years of labor, their bare arms showing both strength and old scars—testaments to lessons learned through pain.

To the right, a tall brass jar holding two iron rods stands on the bench beside the hearth, and a single small iron tool rests on a wooden table.

A great stone arch vaults over the dim grey workshop, lit by the forge's warm glow, and firelight glows ruby-red between the flagstones of the floor. The overall atmosphere is one of intense heat, focused concentration, and purposeful creation.

## Archetypal Essence

The Forge represents the archetype of transformative creation, where raw materials become treasures only through the application of heat, hammer, and human will. This card speaks to the alchemical truth that we are both the blacksmith and the metal—simultaneously the one who wields the tools and the one being shaped by life's fires. It reminds us that true strength comes not from avoiding the forge but from enduring it, and that our greatest works are often born in conditions of intense pressure, heat, and focused determination.

## Render Prompt

```
A muscular blacksmith brings a heavy iron hammer down in mid-strike onto a glowing orange-hot bar of metal held with long tongs on a black iron anvil, a burst of sparks flying outward from the point of impact. The blacksmith stands in three-quarter view facing the viewer at the center, wearing a scarred leather apron, bare forearms marked with old burn scars, face lit from below by the glowing metal, calm and focused. Behind the blacksmith a great arched stone forge hearth roars with flames. To the right a small wooden bench holds a finished sword and a key. Plain flagstone floor in the lower part of the scene. Intense, purposeful creation.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE FORGE" at the bottom.

A muscular figure stands at the center of the card before a roaring stone forge, their face strongly illuminated by the orange and crimson flames dancing inside the hearth. The blacksmith holds a glowing white-hot piece of metal on a massive black iron anvil with heavy iron tongs in one hand, while the other hand raises a weighty hammer above their head, frozen at the apex of the mid-strike. Sparks cascade outward like golden rain, suspended in mid-air across the scene, each tiny spark catching the firelight.

The blacksmith wears a thick leather apron scarred with countless old burn marks and years of labor. Their bare muscular arms show both present strength and faint old scars — testaments to lessons learned through pain. Their expression is one of focused concentration.

Behind the forge, iron tools hang in perfect order on a wooden wall: hammers of various sizes, tongs, chisels, and files, each worn smooth by countless hands. To the left of the anvil, a wooden bucket of water steams where hot metal has been quenched; its surface still ripples in concentric circles. To the right, on a sturdy wooden table, completed works rest side by side: a straight steel sword, an ornate brass key, a horseshoe, and a delicate iron rose with petals as thin as paper — the full range from practical to beautiful.

Through an arched stone doorway in the background, cool blue dawn breaks over distant mountain peaks, its cool light contrasting sharply with the forge's warm orange-red glow. A large leather-and-wood bellows hangs beside the forge. Scattered ruby-red coals glow on the stone floor. Smoke rises from the hearth in slow spirals toward the rafters.

Atmosphere: intense heat, focused concentration, purposeful creation.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE FORGE" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 435889 · tarot_flux_final_00066_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00066_.png`
- Seed: 435889
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the gold star at the top of <image1>. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [380, 0, 660, 200], seed 1, output `tarot_qwen21_edit_00013_.png`, 2026-09-24T15:58:53+02:00)
- Repair: Paint over everything drawn on the dark grey wall to the right of the stone arch in <image1>: the star with a face, the squiggles, the keyhole shape and the white dots, so this part of the wall is plain dark grey with faint vertical streaks like the rest of the wall. Keep the stone arch and the metal vase below exactly as they are. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [758, 570, 900, 805], seed 3, output `tarot_qwen21_edit_00126_.png`, tone-matched, 2026-10-24T17:46:21+02:00)
- Repair: Replace the strange hoop-and-key shaped object hanging on the left wall of <image1> with a pair of long iron blacksmith's tongs hanging from a peg, drawn in the same woodcut style with black ink outlines, with the whole tongs visible down to the ends of their handles. Also remove the small white dot on the wall to its right. Fill around them with the same dark grey wall. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [60, 600, 285, 950], seed 1, output `tarot_qwen21_edit_00123_.png`, tone-matched, 2026-10-24T17:42:49+02:00)
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00066_.png, matched to the attached image by pixel comparison (mean difference 1.2 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00072_.png at 17.8). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00066_.png",
  "seed": 435889,
  "title": "The Forge",
  "scene": "A muscular blacksmith brings a heavy iron hammer down in mid-strike onto a glowing orange-hot bar of metal held with long tongs on a black iron anvil, a burst of sparks flying outward from the point of impact. The blacksmith stands in three-quarter view facing the viewer at the center, wearing a scarred leather apron, bare forearms marked with old burn scars, face lit from below by the glowing metal, calm and focused. Behind the blacksmith a great arched stone forge hearth roars with flames. To the right a small wooden bench holds a finished sword and a key. Plain flagstone floor in the lower part of the scene. Intense, purposeful creation.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA muscular blacksmith brings a heavy iron hammer down in mid-strike onto a glowing orange-hot bar of metal held with long tongs on a black iron anvil, a burst of sparks flying outward from the point of impact. The blacksmith stands in three-quarter view facing the viewer at the center, wearing a scarred leather apron, bare forearms marked with old burn scars, face lit from below by the glowing metal, calm and focused. Behind the blacksmith a great arched stone forge hearth roars with flames. To the right a small wooden bench holds a finished sword and a key. Plain flagstone floor in the lower part of the scene. Intense, purposeful creation.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA muscular blacksmith brings a heavy iron hammer down in mid-strike onto a glowing orange-hot bar of metal held with long tongs on a black iron anvil, a burst of sparks flying outward from the point of impact. The blacksmith stands in three-quarter view facing the viewer at the center, wearing a scarred leather apron, bare forearms marked with old burn scars, face lit from below by the glowing metal, calm and focused. Behind the blacksmith a great arched stone forge hearth roars with flames. To the right a small wooden bench holds a finished sword and a key. Plain flagstone floor in the lower part of the scene. Intense, purposeful creation.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 435889,
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
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00066_.png, matched to the attached image by pixel comparison (mean difference 1.2 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00072_.png at 17.8). Render date unknown.",
  "repairs": [
    {
      "edited": "2026-09-24T15:58:53+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00013_.png",
      "seed": 1,
      "instruction": "Remove the gold star at the top of <image1>. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        380,
        0,
        660,
        200
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
            "image": "tarot_edit_src_9549a989.png"
          },
          "is_changed": [
            "35420b58cd39ca3c29debe702fc4fb2a2e2690db3dca745740f4845961f777b6"
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
            "prompt": "Remove the gold star at the top of <image1>. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T17:46:21+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00126_.png",
      "seed": 3,
      "instruction": "Paint over everything drawn on the dark grey wall to the right of the stone arch in <image1>: the star with a face, the squiggles, the keyhole shape and the white dots, so this part of the wall is plain dark grey with faint vertical streaks like the rest of the wall. Keep the stone arch and the metal vase below exactly as they are. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        758,
        570,
        900,
        805
      ],
      "feather": 10,
      "tone_match": true,
      "tone_offset": [
        2.7,
        5.8,
        4.7
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
            "image": "tarot_src_4ddcffe9.png"
          },
          "is_changed": [
            "6b3fbf15fa0787eb7ff3ededed3063625bf8d8af7707de81e6eae19769ff582b"
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
            "prompt": "Paint over everything drawn on the dark grey wall to the right of the stone arch in <image1>: the star with a face, the squiggles, the keyhole shape and the white dots, so this part of the wall is plain dark grey with faint vertical streaks like the rest of the wall. Keep the stone arch and the metal vase below exactly as they are. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
    },
    {
      "edited": "2026-10-24T17:42:49+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00123_.png",
      "seed": 1,
      "instruction": "Replace the strange hoop-and-key shaped object hanging on the left wall of <image1> with a pair of long iron blacksmith's tongs hanging from a peg, drawn in the same woodcut style with black ink outlines, with the whole tongs visible down to the ends of their handles. Also remove the small white dot on the wall to its right. Fill around them with the same dark grey wall. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        60,
        600,
        285,
        950
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        0.4,
        1.0,
        -0.2
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
            "image": "tarot_src_21b32975.png"
          },
          "is_changed": [
            "6b3fbf15fa0787eb7ff3ededed3063625bf8d8af7707de81e6eae19769ff582b"
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
            "prompt": "Replace the strange hoop-and-key shaped object hanging on the left wall of <image1> with a pair of long iron blacksmith's tongs hanging from a peg, drawn in the same woodcut style with black ink outlines, with the whole tongs visible down to the ends of their handles. Also remove the small white dot on the wall to its right. Fill around them with the same dark grey wall. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
    }
  ]
}
```

</details>
