---
title: "The Hollow Crown"
concept: "Empty authority, freedom through release"
key_terms: ["crown", "hollow", "authority", "sovereignty", "relinquishment", "abdication"]
created: "2026-04-20"
seed: 640312
image_status: "present"
prompt_status: "original"
image: "card_the-hollow-crown.png"
clip: "the-hollow-crown_code_v4.mp4"
joplin_note: "a2a0783f4bab402dbd825c6864de014f"
---

# The Hollow Crown

*An original tarot card in the Rider-Waite tradition*

![The Hollow Crown](/media/card_the-hollow-crown.png)

## Visual Description

### Composition
In the foreground a five-pointed crown sits upright on a plain wooden table, seen from above so its empty inside shows, a heap of red cloth tied with a blue band lying beside it as if just set down. Behind the table, a dark stone room opens onto a plain doorway, its heavy door swung wide. A figure seen from behind has just crossed the threshold into a wide green field, walking toward a single bare tree. The table and crown sit low and close; the figure is small and distant, so the eye travels from what was carried to the one who has stopped carrying it.

### Symbolism
The crown is finely wrought and still whole: set down, not broken. Its hollow inside is the card's point: the power was a shape around nothing. The red cloth of office lies bunched in a heap rather than folded away. The figure wears a plain ochre travelling coat with no insignia. The open door and the threshold mark a crossing made by choice, and the bare tree promises a season that has not yet begun.

### Atmosphere

Early morning. Pale, clean light fills the doorway before the sky has taken on colour. The room is cool and dark and the field is bright. The tone is relief rather than grief, and the stride is unhurried.

## Archetypal Essence

The Hollow Crown represents the archetype of authority relinquished — power that is given back rather than lost or taken. This card speaks to the moment of recognizing that a role has become heavier than whatever it was meant to protect, and choosing to step out of it not in failure but in clarity. It honors the sovereignty that knows itself well enough to unmake itself, the leadership that understands its own proper ending. The Hollow Crown teaches that some freedoms are only available on the far side of a threshold you once believed you could not cross.

## Render Prompt

```
A plain bronze crown with five points rests on a simple wooden table in the foreground, its empty hollow inside clearly visible, a folded oxblood-red robe laid beside it. Beyond the table, a figure in a plain undyed linen tunic, seen from behind, walks out through an open doorway into a wide green field in pale early dawn light, having just set the crown down. A single bare tree stands in the field. The room is cool and still, its walls plain stone. Plain wooden floorboards in the lower part of the scene. Quiet relief, a burden set down.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE HOLLOW CROWN" at the bottom.

A bronze crown with five balanced points rests on a simple wooden table — no head, no figure, no throne. The crown's inner circumference catches the light, revealing perfect emptiness within. Each of the five points is set with a small unpolished river stone in place of a jewel. Beside the crown, a pair of worn hands visible only to the wrists at the right edge of the frame lay down a folded robe in matching bronze and deep oxblood red velvet, its inside cream, its outer velvet worn at the collar and cuffs from long carrying.

A single heavy ornate key lies next to the crown, as if just set down. On the table's surface a faint ring of dust shows where the crown used to sit, slightly offset from where it now rests. On the far wall, a window stands open to a field at dawn; a plain linen curtain moves gently inward on the wind. Through the window, a bare-branched tree is just catching the first dawn light, with a single sparrow in its lower branches.

The earliest moment of morning: cool, still room; pale, clean light not yet turned gold; the emotional tone is quiet relief rather than grief. No throne, no guards, no court — only the hands, the crown, and the opening field.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE HOLLOW CROWN" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 640312 · tarot_flux_final_00090_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: None · ComfyUI 0.35.0 or earlier · output `tarot_flux_final_00090_.png`
- Seed: 640312
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Replace the wooden floorboards outside the doorway, under the walking figure's feet, with the same green grassy field that lies behind him, so the figure walks on grass. Keep the figure, his legs and shoes exactly the same. (box [350, 985, 772, 1122], seed 3, output `tarot_qwen21_edit_00154_.png`, tone-matched, 2026-10-24T18:49:34+02:00)
- Repair: Remove the small brass door handle floating in the dark gap to the right of the open door's edge. Fill its place with the same plain black shadow. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [915, 740, 1015, 865], seed 3, output `tarot_qwen21_edit_00157_.png`, tone-matched, 2026-10-24T18:53:22+02:00)
- Note: Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00090_.png, matched to the attached image by pixel comparison (mean difference 1.1 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00088_.png at 62.1). Render date unknown.

```json
{
  "rendered": null,
  "comfyui_version": "0.35.0 or earlier",
  "comfy_file": "tarot_flux_final_00090_.png",
  "seed": 640312,
  "title": "The Hollow Crown",
  "scene": "A plain bronze crown with five points rests on a simple wooden table in the foreground, its empty hollow inside clearly visible, a folded oxblood-red robe laid beside it. Beyond the table, a figure in a plain undyed linen tunic, seen from behind, walks out through an open doorway into a wide green field in pale early dawn light, having just set the crown down. A single bare tree stands in the field. The room is cool and still, its walls plain stone. Plain wooden floorboards in the lower part of the scene. Quiet relief, a burden set down.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA plain bronze crown with five points rests on a simple wooden table in the foreground, its empty hollow inside clearly visible, a folded oxblood-red robe laid beside it. Beyond the table, a figure in a plain undyed linen tunic, seen from behind, walks out through an open doorway into a wide green field in pale early dawn light, having just set the crown down. A single bare tree stands in the field. The room is cool and still, its walls plain stone. Plain wooden floorboards in the lower part of the scene. Quiet relief, a burden set down.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA plain bronze crown with five points rests on a simple wooden table in the foreground, its empty hollow inside clearly visible, a folded oxblood-red robe laid beside it. Beyond the table, a figure in a plain undyed linen tunic, seen from behind, walks out through an open doorway into a wide green field in pale early dawn light, having just set the crown down. A single bare tree stands in the field. The room is cool and still, its walls plain stone. Plain wooden floorboards in the lower part of the scene. Quiet relief, a burden set down.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 640312,
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
  "note": "Backfilled 2026-09-24 from the ComfyUI output tarot_flux_final_00090_.png, matched to the attached image by pixel comparison (mean difference 1.1 on 0-255 after re-framing with these frame flags; next-best tarot_flux_final_00088_.png at 62.1). Render date unknown.",
  "repairs": [
    {
      "edited": "2026-10-24T18:49:34+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00154_.png",
      "seed": 3,
      "instruction": "Replace the wooden floorboards outside the doorway, under the walking figure's feet, with the same green grassy field that lies behind him, so the figure walks on grass. Keep the figure, his legs and shoes exactly the same.",
      "box": [
        350,
        985,
        772,
        1122
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        37.4,
        15.2,
        38.5
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
            "image": "tarot_src_747ca8b7.png"
          },
          "is_changed": [
            "47ca4ebee6b92ed103e79345bccaf99014ba245da7fb58c8cc1749ab1779cad7"
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
            "prompt": "Replace the wooden floorboards outside the doorway, under the walking figure's feet, with the same green grassy field that lies behind him, so the figure walks on grass. Keep the figure, his legs and shoes exactly the same.",
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
      "edited": "2026-10-24T18:53:22+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00157_.png",
      "seed": 3,
      "instruction": "Remove the small brass door handle floating in the dark gap to the right of the open door's edge. Fill its place with the same plain black shadow. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        915,
        740,
        1015,
        865
      ],
      "feather": 6,
      "tone_match": true,
      "tone_offset": [
        1.7,
        1.5,
        0.3
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
            "image": "tarot_src_8a17b9ef.png"
          },
          "is_changed": [
            "47ca4ebee6b92ed103e79345bccaf99014ba245da7fb58c8cc1749ab1779cad7"
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
            "prompt": "Remove the small brass door handle floating in the dark gap to the right of the open door's edge. Fill its place with the same plain black shadow. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
  ]
}
```

</details>
