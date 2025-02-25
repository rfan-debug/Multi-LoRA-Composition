export CUDA_VISIBLE_DEVICES=0

python compose_lora.py \
    --method composite \
    --compos_num 2 \
    --save_path output_fixed \
    --lora_scale 0.8 \
    --image_style reality \
    --denoise_steps 100 \
    --cfg_scale 7 \
    --height 512 \
    --width 512 \
