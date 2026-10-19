---
title: "The Horizon"
concept: "Possibility, distant future"
key_terms: ["horizon", "skyline", "edge"]
created: "2025-12-24"
seed: 21143281
image_status: "present"
prompt_status: "original"
image: "card_the-horizon.png"
clip: "the-horizon_code_v2.mp4"
joplin_note: "b5e641caf3f3418aa73d8d5d06987a95"
---

# The Horizon

*An original tarot card in the Rider-Waite tradition*

![The Horizon](/media/card_the-horizon.png)

## Visual Description

### Composition
A young woman in a long sky-blue hooded cloak stands on a grassy ridge with her back to us, gazing out at a vast golden plain that stretches to a flat horizon. A round orange sun rests on the horizon line. Four dark birds fly high on the right, and a single bright four-pointed evening star shines in the upper left. Pale boulders lie in the amber grass at her feet, and a rocky outcrop rises on the right.

### Symbolism
The horizon is the boundary of what can be seen: the place where the known meets the unknown and keeps moving as we approach it. The setting sun resting on it is an ending that also promises a return. The evening star is the first light of what comes next. Her stillness and the open land before her are longing and possibility, the sense of a life larger than the present view.

### Atmosphere
Sunset, the sky shading from deep violet overhead to warm gold at the horizon. The mood is still, longing and open.

## Archetypal Essence

The Horizon represents the eternal boundary between the known and the unknown, the perpetual edge that moves as we move, forever ahead and forever present. This is the archetype of aspiration itself - the force that pulls us forward not because we will arrive, but because the reaching defines us. It teaches that the horizon is not a place but a relationship, not a destination but a direction. The Horizon reminds us that we are always exactly as far from our ultimate becoming as we have ever been, and that this is not defeat but the very nature of growth - we expand not by reaching the edge, but by recognizing that the edge expands with us.

## Render Prompt

```
A young woman in a sky-blue woollen cloak stands on a grassy ridge with her back to us, gazing out at a vast open plain that stretches to a distant flat horizon. The setting sun rests on the horizon line, round and deep orange, and three dark birds fly low along it. Amber grass and a few scattered boulders fill the ridge around her feet. Above, the sky shades from warm gold at the horizon to deep violet overhead, where a single bright evening star has appeared. Her cloak lifts slightly in the wind. Still, longing, open mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE HORIZON" at the bottom.

The card is dominated by a vast horizon line that divides the image precisely in half. Below the horizon, rolling hills of amber and wheat-colored grass stretch to the edge of sight; above it, an infinite sky shifts in gradient from pale dawn blue at the horizon to deep twilight purple at the top of the card.

A solitary figure stands just left of center, slightly forward, with their back to the viewer. Their arms hang relaxed at their sides and their posture is still, gazing steadily toward the horizon. They wear a traveler's cloak that shifts color from earthen brown at the hem to sky blue at the shoulders, as if they are gradually becoming part of both realms.

The horizon line itself shimmers with a faint inner light, neither fully solid nor fully ethereal — suggested rather than drawn. On the left side of the horizon, the sun is setting in brilliant oranges and reds; on the right side, small stars are beginning to emerge in the darkening sky — both events occurring simultaneously along the same line.

Three birds fly along the horizon line itself, their silhouettes caught precisely between earth and sky, wings neither rising nor falling. At the figure's feet, a faint footpath begins but quickly fades into the grass, suggesting that no clear route exists from here. In the sky, wispy clouds form shapes that almost resemble letters or symbols yet remain just out of legibility. Near the horizon, the amber grass appears to merge seamlessly with the sky, making the exact boundary impossible to name. A single white flower grows at the figure's feet, its petals pointing outward toward the horizon.

Atmosphere: vast, quiet, aspirational — the forever-edge that recedes as you approach it.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE HORIZON" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 21143281 · tarot_flux_final_00611_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T14:55:02+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00611_.png`
- Seed: 21143281
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Add a single bright four-pointed golden evening star in the empty upper left part of the sky in <image1>, small and drawn with crisp black outlines like the other shapes. Keep the sky gradient around it. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [120, 60, 460, 320], seed 2, output `tarot_qwen21_edit_00028_.png`, 2026-10-02T01:41:02+02:00)

```json
{
  "rendered": "2026-10-01T14:55:02+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00611_.png",
  "seed": 21143281,
  "title": "The Horizon",
  "scene": "A young woman in a sky-blue woollen cloak stands on a grassy ridge with her back to us, gazing out at a vast open plain that stretches to a distant flat horizon. The setting sun rests on the horizon line, round and deep orange, and three dark birds fly low along it. Amber grass and a few scattered boulders fill the ridge around her feet. Above, the sky shades from warm gold at the horizon to deep violet overhead, where a single bright evening star has appeared. Her cloak lifts slightly in the wind. Still, longing, open mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a sky-blue woollen cloak stands on a grassy ridge with her back to us, gazing out at a vast open plain that stretches to a distant flat horizon. The setting sun rests on the horizon line, round and deep orange, and three dark birds fly low along it. Amber grass and a few scattered boulders fill the ridge around her feet. Above, the sky shades from warm gold at the horizon to deep violet overhead, where a single bright evening star has appeared. Her cloak lifts slightly in the wind. Still, longing, open mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young woman in a sky-blue woollen cloak stands on a grassy ridge with her back to us, gazing out at a vast open plain that stretches to a distant flat horizon. The setting sun rests on the horizon line, round and deep orange, and three dark birds fly low along it. Amber grass and a few scattered boulders fill the ridge around her feet. Above, the sky shades from warm gold at the horizon to deep violet overhead, where a single bright evening star has appeared. Her cloak lifts slightly in the wind. Still, longing, open mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 21143281,
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
      "edited": "2026-10-02T01:41:02+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00028_.png",
      "seed": 2,
      "instruction": "Add a single bright four-pointed golden evening star in the empty upper left part of the sky in <image1>, small and drawn with crisp black outlines like the other shapes. Keep the sky gradient around it. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        120,
        60,
        460,
        320
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
            "image": "tarot_src_721a031e.png"
          },
          "is_changed": [
            "cfb5776daf2444c1165289c00b79be3ff54430549407e97b6eef707f364cf93b"
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
            "prompt": "Add a single bright four-pointed golden evening star in the empty upper left part of the sky in <image1>, small and drawn with crisp black outlines like the other shapes. Keep the sky gradient around it. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
