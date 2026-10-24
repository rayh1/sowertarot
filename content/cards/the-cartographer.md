---
title: "The Cartographer"
concept: "Navigation, planning journey"
key_terms: ["cartographer", "map", "chart"]
created: "2025-12-24"
seed: 524449389
image_status: "present"
prompt_status: "original"
image: "card_the-cartographer.png"
clip: "the-cartographer_code_v3.mp4"
joplin_note: "a4264b3376e94331bc7c0b9d1223ed89"
---

# The Cartographer

*An original tarot card in the Rider-Waite tradition*

![The Cartographer](/media/card_the-cartographer.png)

## Visual Description

### Composition
A cartographer sits on a low wooden bench at a small field table on a grassy hilltop, seen from behind and to the side. He wears a dark green hooded coat with a leather belt and a soft brown leather cap, and draws with a long black quill on a large sheet of parchment covered in rivers and coastlines. A brass compass lies on the corner of the map; a leather satchel rests in the grass at his feet. Below him the land opens out: golden fields and a small grey-roofed village on the left, a river winding past pine woods on the right into a valley of layered green mountains. A low orange sun hangs in the upper left; a single dark bird flies across the pale sky.

### Symbolism
The map is the work of making sense: the land below is real and wide, the parchment is his patient translation of it into something others can use. The river on the map echoes the river in the valley, the record answering the thing recorded. The compass is method and orientation; the quill is the act of committing knowledge to a lasting form. The packed satchel says the mapping is not finished at the table: he has walked this land and will walk on. The bird crossing toward the far mountains traces the next stretch of unknown country, the part not yet drawn.

### Atmosphere
Late afternoon, warm and still. Golden light lies over the fields and the far mountains fade into soft haze. The mood is focused and quietly content: the calm of careful, unhurried work in an open landscape.

## Archetypal Essence

The Cartographer represents the human need to make sense of our world, to transform the overwhelming unknown into navigable knowledge. This is the archetype of the systematic learner, the patient documenter, the one who creates tools for understanding that will outlast them. It speaks to our dual nature as both explorers and scholars - we must venture into uncertainty to gain knowledge, then return to translate that knowledge into forms others can use. The Cartographer reminds us that all understanding is partial and provisional, that today's blank spaces become tomorrow's detailed terrain, and that the most valuable maps are those that honestly show both what we know and what we have yet to learn. This card teaches that making meaning is itself a sacred act, and that the frameworks we create shape not just our understanding but our possibilities.

## Render Prompt

```
A cartographer in a dark green doublet and a brown leather cap sits at a small wooden field table on a grassy hilltop, drawing a map with a long quill; half the parchment shows drawn rivers and mountains, the other half is still bare. A brass compass rests on the corner of the table and a leather satchel lies at his feet. Below the hill on the left lie cultivated fields, a small village and a winding river in warm golden light; on the right, untamed forest and hills fade into silver mist. A single bird flies from the village side toward the misty wilderness. Late afternoon sun low on the left. Focused, quietly eager mood.
```

## DALL-E Prompt

```
Create a tarot card in the traditional Rider-Waite style with the title "THE CARTOGRAPHER" at the bottom.

A scholar sits at a worn wooden table strewn with maps, charts, and rolled scrolls. Their weathered hands hold a brass compass in one hand and an ink-dipped quill in the other, poised over work in progress. The figure's expression is one of deep concentration and quiet excitement — the look of someone who knows that each line drawn is both a record of what is and a guide for what will be.

Before the scholar lies an unfinished map: half of it rendered in meticulous detail with mountains, winding rivers, and dark forests in rich earth tones of umber, sienna, and forest green; the other half remains blank cream-colored parchment, awaiting discovery.

Behind the figure, a large leaded-glass window reveals a vast landscape split down the middle. On the left, familiar cultivated lands — clear paths, small settlements, patchwork fields — are bathed in warm golden light. On the right, unexplored wilderness extends into distance, shrouded in mysterious silver mist, its contours suggested but not resolved. Through the window, a bird flies from the known lands toward the unknown, tracing an invisible path. Above the cartographer's head, constellations are faintly visible in the upper corners of the window, suggesting navigation by both earthly and celestial means.

The cartographer's desk holds instruments of measurement: a brass astrolabe, a sextant, rolled charts bound with red ribbon, a stoppered jar of dark ink, and a single tall candle burning with a steady flame. On the wall behind hang previous maps in wooden frames, each showing progression and increasing accuracy — a visual history of learning. A leather satchel rests by the scholar's feet, packed and ready for the next journey. The floor is scattered with crumpled parchments, the trial and error of the mapping process.

Atmosphere: warm, studious, patient — the scholar's workshop at the edge of the world.

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "THE CARTOGRAPHER" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

## Render Record

<details>
<summary>Seed 524449389 · tarot_flux_final_00423_.png — full render recipe</summary>

Written by `attach_image.py` with the image above. It holds everything needed to re-render that image without the ComfyUI output file — `render_card.py --from-note "<title>"` does all of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title <title> <frame_flags>`; for each entry in `repairs`, first run its `workflow` on the unframed art and keep the result only inside `box` (soft edge `feather`), as `edit_card.py` does. The model files named below must exist in ComfyUI.

- Rendered: 2026-10-01T02:13:46+02:00 · ComfyUI 0.37.0 · output `tarot_flux_final_00423_.png`
- Seed: 524449389
- Models: `flux1-dev-fp8.safetensors`, `4x-UltraSharp.pth`, `sowtarot_woodcut-v1.safetensors` (LoRA, strength 1.0), `qwen_image_2.1_int8_convrot.safetensors`, `qwen3vl_8b_int8_convrot.safetensors`, `qwen_image_2.1_vae_bf16.safetensors`
- Frame flags: `--art-crop 0.035 --paper 216,199,158 --ink 26,22,18 --margin-frac 0.020 --border-frac 0.008 --banner-frac 0.085`
- Repair: Remove the black curly ornament and frame lines in the top right corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [840, 0, 1024, 190], seed 2, output `tarot_qwen21_edit_00019_.png`, 2026-10-01T11:29:59+02:00)
- Repair: Remove the black curly ornament and frame lines in the top left corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same. (box [0, 0, 155, 160], seed 1, output `tarot_qwen21_edit_00021_.png`, 2026-10-01T11:54:44+02:00)

```json
{
  "rendered": "2026-10-01T02:13:46+02:00",
  "comfyui_version": "0.37.0",
  "comfy_file": "tarot_flux_final_00423_.png",
  "seed": 524449389,
  "title": "The Cartographer",
  "scene": "A cartographer in a dark green doublet and a brown leather cap sits at a small wooden field table on a grassy hilltop, drawing a map with a long quill; half the parchment shows drawn rivers and mountains, the other half is still bare. A brass compass rests on the corner of the table and a leather satchel lies at his feet. Below the hill on the left lie cultivated fields, a small village and a winding river in warm golden light; on the right, untamed forest and hills fade into silver mist. A single bird flies from the village side toward the misty wilderness. Late afternoon sun low on the left. Focused, quietly eager mood.",
  "prompt": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA cartographer in a dark green doublet and a brown leather cap sits at a small wooden field table on a grassy hilltop, drawing a map with a long quill; half the parchment shows drawn rivers and mountains, the other half is still bare. A brass compass rests on the corner of the table and a leather satchel lies at his feet. Below the hill on the left lie cultivated fields, a small village and a winding river in warm golden light; on the right, untamed forest and hills fade into silver mist. A single bird flies from the village side toward the misty wilderness. Late afternoon sun low on the left. Focused, quietly eager mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "text": "wdctarot. A hand-drawn illustration in the style of Pamela Colman Smith and early-twentieth-century esoteric book-plate art, rendered as a bold woodcut / linocut print: heavy black ink outlines on every form, dense cross-hatching and hatched shading, high tonal contrast, strong graphic linework, flat screen-printed color fills, and an aged-paper grain. Muted earthy palette: slate blue-grey, ochre and umber, sage green, aged cream, with a single warm gold accent on the focal symbol. Symbolic, archetypal, calm and reverent storybook mood. A single full-bleed scene that fills the whole image, flat 2D illustration, no photorealism, no 3D render, no modern objects.\n\nA cartographer in a dark green doublet and a brown leather cap sits at a small wooden field table on a grassy hilltop, drawing a map with a long quill; half the parchment shows drawn rivers and mountains, the other half is still bare. A brass compass rests on the corner of the table and a leather satchel lies at his feet. Below the hill on the left lie cultivated fields, a small village and a winding river in warm golden light; on the right, untamed forest and hills fade into silver mist. A single bird flies from the village side toward the misty wilderness. Late afternoon sun low on the left. Focused, quietly eager mood.\n\nComposition fills the whole frame. No text, no lettering, no title, no border, no banner, no card frame, no signature, no page numbers.",
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
        "seed": 524449389,
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
      "edited": "2026-10-01T11:29:59+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00019_.png",
      "seed": 2,
      "instruction": "Remove the black curly ornament and frame lines in the top right corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        840,
        0,
        1024,
        190
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
            "image": "tarot_src_13f63981.png"
          },
          "is_changed": [
            "e07fc3abf168ea7b0edc8e2d79056a3829f58a749234d8195b4fc8922e2e83b6"
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
            "prompt": "Remove the black curly ornament and frame lines in the top right corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
      "edited": "2026-10-01T11:54:44+02:00",
      "comfyui_version": "0.37.0",
      "comfy_file": "tarot_qwen21_edit_00021_.png",
      "seed": 1,
      "instruction": "Remove the black curly ornament and frame lines in the top left corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same.",
      "box": [
        0,
        0,
        155,
        160
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
            "image": "tarot_src_0e1630d9.png"
          },
          "is_changed": [
            "20534148f4dcbd86db8a74a025f44d1efd47d3df376046f9c0b8e6232294148a"
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
            "prompt": "Remove the black curly ornament and frame lines in the top left corner of <image1>. Fill their place with the same pale yellow sky with soft clouds. Keep everything else, including the woodcut linework and hatching, exactly the same.",
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
