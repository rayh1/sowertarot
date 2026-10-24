---
title: "The Chrysalis"
concept: "Transformation, becoming"
key_terms: ["chrysalis", "cocoon", "metamorphosis"]
created: "2025-12-24"
seed: 90822747
image_status: "present"
prompt_status: "original"
image: "card_the-chrysalis.png"
clip: "the-chrysalis_code_v2.mp4"
joplin_note: "773eeccce3f24e74acaf230b4877b33e"
---

# The Chrysalis

*An original tarot card in the Rider-Waite tradition*

![The Chrysalis](/media/card_the-chrysalis.png)

## Visual Description

### Composition
A young girl in a plain blue-grey linen dress kneels in the grass beneath an old gnarled tree, looking up in wonder. From a low bare branch a pale green chrysalis flecked with gold hangs on a long silken thread; beside it hangs a spray of pink blossom. A few brown leaves drift down through the air past her. Tall grasses and leafy stalks grow around her, and a single small pink flower blooms in the grass.

### Symbolism
The chrysalis is transformation in progress: neither what was nor what will be, held still while the change happens inside. The falling leaves and the opening blossom side by side show an ending and a beginning at the same moment. The kneeling child is patience and wonder, watching without trying to hurry the change.

### Atmosphere
Soft dawn light, a sky shading from peach to pale cream. The mood is hushed and patient, full of quiet expectation.

## Archetypal Essence

The Chrysalis represents the profound mystery of radical transformation - the death that is not death, the waiting that is actually intense invisible work, the dissolution that precedes all true becoming. This is the archetype of metamorphosis in its most vulnerable and powerful form, teaching us that some changes cannot be rushed or observed, only trusted. It reminds us that the most important growth happens in darkness and stillness, and that what emerges is never simply a continuation of what went in, but something entirely new born from the essence of the old.

## Render Prompt

```
A young girl in a plain grey linen dress kneels in the grass beneath an old gnarled tree, looking up with wonder at a large golden-green chrysalis hanging from a low branch on a short silken thread. Clusters of pink blossom and fresh green leaves are opening along that branch right beside the chrysalis, while a few brown autumn leaves drift down through the air past her. A small cricket sits on a grass stem near her knee. Soft dawn sky shading from rose to pale gold. Hushed, patient mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE CHRYSALIS" at the bottom.

A luminous golden-green translucent chrysalis hangs at the center of the card from a gnarled branch that extends diagonally from upper-left to lower-right, suspended between earth and sky. Through the chrysalis's translucent shell, a shadowy form is faintly visible within — neither caterpillar nor butterfly, but something in between, curled in perfect stillness.

The world around the chrysalis exists in two simultaneous states, split down the vertical center: on the left side, autumn leaves fall through cool air and the branch appears bare, weathered, and grey; on the right side, spring blossoms burst forth on the same branch and fresh green leaves unfurl in warm light. The background sky shows a gradient moving from deep purple twilight on the left to rose-gold dawn on the right.

Delicate silver threads connect the chrysalis both to the branch above and downward to tree roots that are visible through transparent soil at the bottom of the card, suggesting the chrysalis is held by forces both seen and unseen.

Small creatures pause in their journeys to witness it: a small brown cricket sits perfectly still on a nearby leaf at mid-height, a field mouse looks up from the soil below, and a dragonfly with iridescent wings hovers at eye level with the chrysalis. Dewdrops cling to the chrysalis's surface, each tiny droplet reflecting a slightly different possible future. At the very bottom of the chrysalis, a single hairline crack — almost imperceptible — has just begun to appear in the shell.

Atmosphere: sacred threshold, breath held, the intense invisible work of becoming.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE CHRYSALIS" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 90822747 · tarot_flux_final_01184_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its `grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, no AI model). The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T22:54:53+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_01184_.png`
- Seed: 90822747
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Replace the brass weight hanging on the thin black thread in <image1>, together with the stiff pin and the bead below it, with a living butterfly chrysalis: a pale green pupa with faint gold dots, softly segmented, hanging from the end of the thin thread, with a rounded tip at the bottom and nothing below it. Draw it in the same woodcut style, with a black ink outline and fine hatching. Fill the place of the pin and bead with the same pale cream sky. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [555, 500, 755, 1040], seed 2, output `tarot_qwen21_edit_00083_.png`, tone-matched, 2026-10-24T15:50:12+02:00)

```json
{
  "rendered": "2026-10-01T22:54:53+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_01184_.png",
  "seed": 90822747,
  "title": "The Chrysalis",
  "scene": "A young girl in a plain grey linen dress kneels in the grass beneath an old gnarled tree, looking up with wonder at a large golden-green chrysalis hanging from a low branch on a short silken thread. Clusters of pink blossom and fresh green leaves are opening along that branch right beside the chrysalis, while a few brown autumn leaves drift down through the air past her. A small cricket sits on a grass stem near her knee. Soft dawn sky shading from rose to pale gold. Hushed, patient mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young girl in a plain grey linen dress kneels in the grass beneath an old gnarled tree, looking up with wonder at a large golden-green chrysalis hanging from a low branch on a short silken thread. Clusters of pink blossom and fresh green leaves are opening along that branch right beside the chrysalis, while a few brown autumn leaves drift down through the air past her. A small cricket sits on a grass stem near her knee. Soft dawn sky shading from rose to pale gold. Hushed, patient mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA young girl in a plain grey linen dress kneels in the grass beneath an old gnarled tree, looking up with wonder at a large golden-green chrysalis hanging from a low branch on a short silken thread. Clusters of pink blossom and fresh green leaves are opening along that branch right beside the chrysalis, while a few brown autumn leaves drift down through the air past her. A small cricket sits on a grass stem near her knee. Soft dawn sky shading from rose to pale gold. Hushed, patient mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 90822747,
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
      "edited": "2026-10-24T15:50:12+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00083_.png",
      "seed": 2,
      "instruction": "Replace the brass weight hanging on the thin black thread in <image1>, together with the stiff pin and the bead below it, with a living butterfly chrysalis: a pale green pupa with faint gold dots, softly segmented, hanging from the end of the thin thread, with a rounded tip at the bottom and nothing below it. Draw it in the same woodcut style, with a black ink outline and fine hatching. Fill the place of the pin and bead with the same pale cream sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        555,
        500,
        755,
        1040
      ],
      "feather": 24,
      "tone_match": true,
      "tone_offset": [
        1.5,
        2.5,
        -2.1
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
            "image": "tarot_src_197857f3.png"
          },
          "is_changed": [
            "dcc548bd9433cc522ad0ffb25fe083b92b68ca8723861f0959d2970bab53f979"
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
            "prompt": "Replace the brass weight hanging on the thin black thread in <image1>, together with the stiff pin and the bead below it, with a living butterfly chrysalis: a pale green pupa with faint gold dots, softly segmented, hanging from the end of the thin thread, with a rounded tip at the bottom and nothing below it. Draw it in the same woodcut style, with a black ink outline and fine hatching. Fill the place of the pin and bead with the same pale cream sky. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
