#!/bin/bash

python run_diffqrcoder.py \
    --prompt "A healthy berry muffin" \
    --qrcode_path "qrcodes/qr_code_from_url.png" \
    --qrcode_module_size 20 \
    --controlnet_conditioning_scale 1.05 \
    --scanning_robust_guidance_scale 50 \
    --perceptual_guidance_scale 20 \
    --output_path "outputs/muffin_qrcode.png"
