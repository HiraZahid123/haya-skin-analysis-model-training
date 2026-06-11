# Model Training Guide

## Prerequisites
- Google account (for Colab)
- Roboflow account (free) — roboflow.com
- GPU runtime in Colab (T4 is free)

## Step 1 — Get Roboflow API Key
1. Go to roboflow.com → sign up (free)
2. Go to Settings → API Keys → copy your key

## Step 2 — Download Dataset (local, optional)
```bash
python download_dataset.py --api-key YOUR_KEY
```

## Step 3 — Train on Google Colab
1. Open train.ipynb in Google Colab
2. Runtime → Change runtime type → T4 GPU
3. Paste your Roboflow API key in Cell 1
4. Runtime → Run all
5. Wait 2-4 hours

## Step 4 — Get the trained model
After training completes, the model is saved at:
```
runs/detect/haya_skin_v1/weights/best.pt
```
Download it and place at:
```
backend/app/models/skin_model.pt
```

## Step 5 — Restart the backend
The YOLO service auto-loads the model on first request.
Check: GET /health → model_loaded should be true

## What the model detects
- Acne / pimples (class: acne)
- Pigmentation / dark spots (class: pigmentation)

## Evaluating accuracy
After training, check these metrics in the Colab output:
- mAP50 > 0.60 = good
- mAP50 > 0.75 = excellent
- If below 0.50: add more data or train more epochs

## Version log
| Version | Date | Dataset | mAP50 | Notes |
|---------|------|---------|-------|-------|
| v1 | TBD | TBD | TBD | First training run |
