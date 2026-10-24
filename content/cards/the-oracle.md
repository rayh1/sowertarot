---
title: "The Oracle"
concept: "Sacred silence, inner knowing that returns rather than foretells"
key_terms: ["oracle", "seer", "diviner", "prophecy", "foresight", "inner knowing"]
created: "2026-04-23"
seed: 314159
image_status: "present"
prompt_status: "original"
image: "card_the-oracle.png"
clip: "the-oracle_code_v3.mp4"
joplin_note: "4f5261195a5246d59e0896846b516063"
---

# The Oracle

*An original tarot card in the Rider-Waite tradition*

![The Oracle](/media/card_the-oracle.png)

## Visual Description

### Composition

A seated figure sits at the center of the card on a simple stone dais, framed between two tall stone columns draped with climbing golden ivy. Her eyes are closed, her face turned slightly downward, posture still and inward. A delicate golden diadem crosses her brow, set with a single white gem at the center — the third eye, open in the realm of intuition. A turquoise stone hangs on a pendant at her chest. Her clasped hands hold a glowing crystal orb in her lap; beneath them a rolled scroll inscribed in an ancient, unreadable hand lies across her knees.

### Symbolism

The deep red robe signals rooted spiritual vitality — power drawn from within rather than performed outward. The twin stone columns evoke a threshold between worlds, an architectural echo of the liminal. The climbing vines soften stone with time: wisdom entwined with living patience. The turquoise stone at her heart is specifically a stone of inner seeing. The crystal orb in her hands is the brightest light in the scene — the figure herself does not glow; her knowing does. The closed eyes insist that this seer does not look *out* to find truth. The unreadable scroll suggests that answers arrive not as legible prophecy but as presence. Between the columns the open night sky shows a few early stars, a reminder that cosmic order and inner knowing meet at the moment the day lets go.

### Atmosphere

An open stone dais under a deep teal night sky. The orb glows pale in her hands; the dark trees behind the dais fade into blue shadow. The air is hushed and reverent. The emotional tone is neither dramatic nor withheld — it is the stillness of a listener who has been here a long time and is in no hurry.

## Archetypal Essence

The Oracle represents the archetype of inner knowing — the capacity to perceive truth through stillness rather than effort. She does not foretell the future; she returns to the seeker what the seeker has forgotten. This card speaks to the wisdom that lives beneath daily thought, accessible only when we quiet enough to hear it. The Oracle teaches that divination is less prophecy than remembrance: the answers we seek are already present within us, and the work is to become still enough that what was always there becomes audible again.

## Render Prompt

```
A seated woman at the center on a simple stone dais, framed between two tall stone columns draped with climbing ivy. Her eyes are closed and her face turned slightly downward, still and listening inward. She wears a deep red robe pooling around her feet. A delicate golden diadem crosses her brow, set at its center with a single turquoise gem, a third eye. In her lap her right hand cradles a single glowing crystal orb, the scene's only light source, its pale light falling on her face and hands while the rest of the dim temple chamber recedes into deep indigo shadow. Her left hand holds a partially unrolled scroll across her thigh, its writing ancient and unreadable. Between the tops of the two columns a narrow sliver of twilight sky shows two or three faint early stars. The climbing vines catch a thin glow along their edges. No other figures are present. Reverent, hushed, inward twilight stillness.
```

## Render Record

<details>
<summary>Seed 314159 · tarot_flux_final_00035_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00035_.png`
- Seed: 314159
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the thin hanging line with the small pendulum at the top center of <image1>. Fill its place with the same dark night sky. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [470, 36, 560, 270], seed 1, output `tarot_qwen21_edit_00014_.png`, 2026-09-24T16:00:00+02:00)
- Repair: Change the three small white teardrop-shaped specks in the dark teal sky into small four-pointed white stars, like the other four-pointed stars in the sky. Fill around them with the same dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [370, 85, 650, 360], seed 2, output `tarot_qwen21_edit_00166_.png`, tone-matched, 2026-10-24T22:04:03+02:00)
- Repair: Remove the small white ball on a thin pin in the dark teal sky. Fill its place with the same plain dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [555, 625, 690, 760], seed 2, output `tarot_qwen21_edit_00169_.png`, tone-matched, 2026-10-24T22:06:53+02:00)
- Repair: Remove the small white tin can with the gold label standing on the stone floor. Fill its place with the same pale stone floor tiles and their dark joint lines. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [672, 1545, 812, 1722], seed 1, output `tarot_qwen21_edit_00171_.png`, tone-matched, 2026-10-24T22:08:54+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [182, 869, 218, 905], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [195, 1118, 231, 1154], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [852, 252, 888, 288], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [848, 486, 884, 522], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [922, 687, 958, 723], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [861, 829, 897, 865], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [860, 1182, 896, 1218], seed 1, output `tarot_qwen21_edit_00180_.png`, tone-matched, 2026-10-24T22:20:34+02:00)
- Repair: Replace the golden vessel held in her hands with a small round glowing crystal orb resting in her clasped hands in her lap. The orb is clear pale crystal with a soft white inner light, drawn with black ink outlines, and its pale glow falls softly on her hands. Keep her hands, her red robe, the turquoise pendant and the scroll. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [405, 1112, 640, 1322], seed 2, output `tarot_qwen21_edit_00163_.png`, tone-matched, 2026-10-24T22:01:18+02:00)
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00035_.png, matched to the attached image by pixel comparison (mean difference 1.4 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00096_.png at 2.7). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00035_.png",
  "seed": 314159,
  "title": "The Oracle",
  "scene": "A seated woman at the center on a simple stone dais, framed between two tall stone columns draped with climbing ivy. Her eyes are closed and her face turned slightly downward, still and listening inward. She wears a deep red robe pooling around her feet. A delicate golden diadem crosses her brow, set at its center with a single turquoise gem, a third eye. In her lap her right hand cradles a single glowing crystal orb, the scene's only light source, its pale light falling on her face and hands while the rest of the dim temple chamber recedes into deep indigo shadow. Her left hand holds a partially unrolled scroll across her thigh, its writing ancient and unreadable. Between the tops of the two columns a narrow sliver of twilight sky shows two or three faint early stars. The climbing vines catch a thin glow along their edges. No other figures are present. Reverent, hushed, inward twilight stillness.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA seated woman at the center on a simple stone dais, framed between two tall stone columns draped with climbing ivy. Her eyes are closed and her face turned slightly downward, still and listening inward. She wears a deep red robe pooling around her feet. A delicate golden diadem crosses her brow, set at its center with a single turquoise gem, a third eye. In her lap her right hand cradles a single glowing crystal orb, the scene's only light source, its pale light falling on her face and hands while the rest of the dim temple chamber recedes into deep indigo shadow. Her left hand holds a partially unrolled scroll across her thigh, its writing ancient and unreadable. Between the tops of the two columns a narrow sliver of twilight sky shows two or three faint early stars. The climbing vines catch a thin glow along their edges. No other figures are present. Reverent, hushed, inward twilight stillness.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA seated woman at the center on a simple stone dais, framed between two tall stone columns draped with climbing ivy. Her eyes are closed and her face turned slightly downward, still and listening inward. She wears a deep red robe pooling around her feet. A delicate golden diadem crosses her brow, set at its center with a single turquoise gem, a third eye. In her lap her right hand cradles a single glowing crystal orb, the scene's only light source, its pale light falling on her face and hands while the rest of the dim temple chamber recedes into deep indigo shadow. Her left hand holds a partially unrolled scroll across her thigh, its writing ancient and unreadable. Between the tops of the two columns a narrow sliver of twilight sky shows two or three faint early stars. The climbing vines catch a thin glow along their edges. No other figures are present. Reverent, hushed, inward twilight stillness.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 314159,
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
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00035_.png, matched to the attached image by pixel comparison (mean difference 1.4 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00096_.png at 2.7). Render date unknown.",
  "repairs": [
    {
      "edited": "2026-09-24T16:00:00+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00014_.png",
      "seed": 1,
      "instruction": "Remove the thin hanging line with the small pendulum at the top center of <image1>. Fill its place with the same dark night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        470,
        36,
        560,
        270
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
            "image": "tarot_edit_src_23a7056b.png"
          },
          "is_changed": [
            "c935b4268975aa0f7ab1a85b770ed3b4733cfbb6207a514e4f52205557b093c3"
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
            "prompt": "Remove the thin hanging line with the small pendulum at the top center of <image1>. Fill its place with the same dark night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:04:03+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00166_.png",
      "seed": 2,
      "instruction": "Change the three small white teardrop-shaped specks in the dark teal sky into small four-pointed white stars, like the other four-pointed stars in the sky. Fill around them with the same dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        370,
        85,
        650,
        360
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        6.5,
        2.6,
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
            "image": "tarot_src_dc76c57f.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Change the three small white teardrop-shaped specks in the dark teal sky into small four-pointed white stars, like the other four-pointed stars in the sky. Fill around them with the same dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
    },
    {
      "edited": "2026-10-24T22:06:53+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00169_.png",
      "seed": 2,
      "instruction": "Remove the small white ball on a thin pin in the dark teal sky. Fill its place with the same plain dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        555,
        625,
        690,
        760
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        6.7,
        4.5,
        4.0
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
            "image": "tarot_src_1d2c4df8.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small white ball on a thin pin in the dark teal sky. Fill its place with the same plain dark teal night sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
    },
    {
      "edited": "2026-10-24T22:08:54+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00171_.png",
      "seed": 1,
      "instruction": "Remove the small white tin can with the gold label standing on the stone floor. Fill its place with the same pale stone floor tiles and their dark joint lines. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        672,
        1545,
        812,
        1722
      ],
      "feather": 8,
      "tone_match": true,
      "tone_offset": [
        1.7,
        2.0,
        -0.9
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
            "image": "tarot_src_873dba96.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small white tin can with the gold label standing on the stone floor. Fill its place with the same pale stone floor tiles and their dark joint lines. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        182,
        869,
        218,
        905
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        0.0,
        1.9,
        -9.8
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        195,
        1118,
        231,
        1154
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        -26.9,
        -20.7,
        -20.7
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        852,
        252,
        888,
        288
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        -5.4,
        -4.5,
        -14.7
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        848,
        486,
        884,
        522
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        -28.9,
        -32.9,
        -51.2
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        922,
        687,
        958,
        723
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        8.9,
        4.8,
        -10.5
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        861,
        829,
        897,
        865
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        -17.8,
        -24.0,
        -44.8
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:20:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00180_.png",
      "seed": 1,
      "instruction": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        860,
        1182,
        896,
        1218
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        -9.7,
        -10.2,
        -18.5
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
            "image": "tarot_src_94289cb1.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Remove the small round gold dots that float on the two grey stone columns, apart from the ivy. Fill their places with the same pale grey stone and its vertical black hatching. Keep the golden ivy leaves and stems. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-24T22:01:18+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00163_.png",
      "seed": 2,
      "instruction": "Replace the golden vessel held in her hands with a small round glowing crystal orb resting in her clasped hands in her lap. The orb is clear pale crystal with a soft white inner light, drawn with black ink outlines, and its pale glow falls softly on her hands. Keep her hands, her red robe, the turquoise pendant and the scroll. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        405,
        1112,
        640,
        1322
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        5.4,
        -2.9,
        -1.4
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
            "image": "tarot_src_fd96a342.png"
          },
          "is_changed": [
            "9df10ec0cc2ed92ccd2296cb0868e24f2a8fe256f1e7a6b4ee0b180c47231771"
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
            "prompt": "Replace the golden vessel held in her hands with a small round glowing crystal orb resting in her clasped hands in her lap. The orb is clear pale crystal with a soft white inner light, drawn with black ink outlines, and its pale glow falls softly on her hands. Keep her hands, her red robe, the turquoise pendant and the scroll. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
