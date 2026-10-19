---
title: "The Witness"
concept: "Awareness, bearing testimony"
key_terms: ["witness", "observer", "watcher"]
created: "2025-12-24"
seed: 663885082
image_status: "present"
prompt_status: "original"
image: "card_the-witness.png"
clip: "the-witness_code_v1.mp4"
joplin_note: "f195f911d574416c919fc5b9d115ea3f"
---

# The Witness

*An original tarot card in the Rider-Waite tradition*

![The Witness](/media/card_the-witness.png)

## Visual Description

### Composition
An old man in a grey woollen habit with a rope belt sits on a low stone bench beneath a great tree at the edge of a clearing, hands resting in his lap, watching. Before him a red fox stands in the grass, and further off a stag grazes beside a still pool. An owl sits on a high branch above him, as still as he is. A few dry leaves drift down through the air. Bare trees frame the scene, and beyond them low hills stretch toward the horizon.

### Symbolism
The seated man is pure attention: present, unmoving, taking everything in without interfering. The fox and the stag go about their lives unafraid, because he does not grasp at them. The owl repeats his watchfulness from above, wisdom that sees in silence. The still pool reflects without distortion, as clear awareness does. The falling leaves are time passing while the witness remains.

### Atmosphere
Sunset: a large pale sun low over the hills, the sky glowing amber and orange through the bare branches. Long warm light lies across the grass. The mood is calm, attentive and timeless.

## Archetypal Essence

The Witness represents the profound human capacity for conscious awareness - the ability to observe our own experience even as we live it. This is the archetype of mindful presence, the part of us that can watch our thoughts and emotions without being swept away by them. It teaches the paradox that sometimes the most powerful action is the simple act of truly seeing, that bearing witness to truth - whether beautiful or terrible - is itself a form of participation that changes what is witnessed. The Witness reminds us that we are not merely our thoughts, feelings, or circumstances, but also the awareness that perceives them. This card speaks to the sacred responsibility of seeing clearly, of honoring what is real, and of the transformative power of attention given freely and without agenda. It is the still point in the turning world, the consciousness that makes all experience possible.

## Render Prompt

```
An old man in a grey woollen habit with a rope belt sits perfectly still on a low stone bench at the edge of a woodland clearing, hands folded in his lap, eyes open, watching. Before him a red fox trots across the grass and a deer grazes beside a still pool that mirrors the sky. Behind him an ancient oak spreads wide branches, and an owl perched on a low bough watches with the same stillness. A few leaves drift down through the air. Warm amber sunset light glows low between the trees, the sky still bright gold fading to soft blue overhead, long shadows across the grass. Calm, attentive, timeless mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE WITNESS" at the bottom.

A silent figure sits at the center of the card on a simple stone bench at the edge of a clearing, perfectly still, their hands resting gently and symmetrically in their lap. Their eyes are open and clear, taking in everything without grasping. The figure wears flowing robes of deep indigo that blend softly into the twilight sky behind them, making them seem both present and quietly transparent — there but not interfering. In their lap sits an open book with blank cream-colored pages, suggesting that true witnessing requires no recording, no commentary, only presence.

Around the figure, life unfolds in concentric rings moving outward. In the innermost ring nearest the Witness, flowers bloom and wilt within the same frame — tight buds on one side of the same stem, full blooms in the middle, fallen petals on the other side — showing the full cycle of growth and decay in accelerated time. In the next ring out, animals move through their daily patterns: a red fox hunts, a brown deer grazes, small birds build nests and tend their young on branches. In the outermost ring, small human figures appear like translucent shadows or memories, engaged in moments of joy, sorrow, conflict, and reconciliation — the drama of existence playing around a still center.

Above the Witness's head, a clear crystal prism catches the light and refracts it into subtle rainbow patterns across the air, showing how pure awareness can reveal hidden dimensions without distorting what is observed. At the figure's feet, a still circular pool of water reflects the entire scene with perfect clarity; in their reflection in the pool, their eyes appear asymmetrical — one looking outward at the world, one looking inward at themselves.

Behind the Witness, an ancient tree stands with deep roots visible through transparent earth. In the tree's upper branches, a large owl watches with equal stillness. Small details indicate time passing: a few leaves falling slowly, clouds drifting, shadows lengthening — yet the Witness remains unchanged, eternal in the moment.

Atmosphere: serene, spacious, the still point in the turning world.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE WITNESS" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 663885082 · tarot_flux_final_00537_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T08:56:31+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00537_.png`
- Seed: 663885082
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the eyeglasses from the old man's face in <image1>. Show his bare eye and the skin of his temple and cheek where the glasses were, drawn in the same style. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [612, 830, 712, 910], seed 2, output `tarot_qwen21_edit_00025_.png`, 2026-10-01T14:30:19+02:00)

```json
{
  "rendered": "2026-10-01T08:56:31+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00537_.png",
  "seed": 663885082,
  "title": "The Witness",
  "scene": "An old man in a grey woollen habit with a rope belt sits perfectly still on a low stone bench at the edge of a woodland clearing, hands folded in his lap, eyes open, watching. Before him a red fox trots across the grass and a deer grazes beside a still pool that mirrors the sky. Behind him an ancient oak spreads wide branches, and an owl perched on a low bough watches with the same stillness. A few leaves drift down through the air. Warm amber sunset light glows low between the trees, the sky still bright gold fading to soft blue overhead, long shadows across the grass. Calm, attentive, timeless mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old man in a grey woollen habit with a rope belt sits perfectly still on a low stone bench at the edge of a woodland clearing, hands folded in his lap, eyes open, watching. Before him a red fox trots across the grass and a deer grazes beside a still pool that mirrors the sky. Behind him an ancient oak spreads wide branches, and an owl perched on a low bough watches with the same stillness. A few leaves drift down through the air. Warm amber sunset light glows low between the trees, the sky still bright gold fading to soft blue overhead, long shadows across the grass. Calm, attentive, timeless mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nAn old man in a grey woollen habit with a rope belt sits perfectly still on a low stone bench at the edge of a woodland clearing, hands folded in his lap, eyes open, watching. Before him a red fox trots across the grass and a deer grazes beside a still pool that mirrors the sky. Behind him an ancient oak spreads wide branches, and an owl perched on a low bough watches with the same stillness. A few leaves drift down through the air. Warm amber sunset light glows low between the trees, the sky still bright gold fading to soft blue overhead, long shadows across the grass. Calm, attentive, timeless mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 663885082,
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
      "edited": "2026-10-01T14:30:19+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00025_.png",
      "seed": 2,
      "instruction": "Remove the eyeglasses from the old man's face in <image1>. Show his bare eye and the skin of his temple and cheek where the glasses were, drawn in the same style. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        612,
        830,
        712,
        910
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
            "image": "tarot_src_2e7aa570.png"
          },
          "is_changed": [
            "007d1a5ac21f55b64c895c735cd71b9f9227f26858dce87e02bd1ad5e4a516aa"
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
            "prompt": "Remove the eyeglasses from the old man's face in <image1>. Show his bare eye and the skin of his temple and cheek where the glasses were, drawn in the same style. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
