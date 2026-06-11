"""
Downloads skin condition datasets from Roboflow Universe.
Run AFTER getting your free Roboflow API key from roboflow.com

Usage:
    python download_dataset.py --api-key YOUR_KEY
"""
import argparse
import os

def download(api_key: str):
    try:
        from roboflow import Roboflow
    except ImportError:
        print("Installing roboflow...")
        os.system("pip install roboflow")
        from roboflow import Roboflow

    rf = Roboflow(api_key=api_key)

    datasets_to_try = [
        # Try these in order — pick whichever has the most images
        ("roboflow-universe-projects", "acne-detection-nzmkp", 1),
        ("roboflow-universe-projects", "skin-disease-detection-3mfhd", 1),
        ("roboflow-universe-projects", "acne-vulgaris-detection", 1),
    ]

    downloaded = False
    for workspace, project_name, version in datasets_to_try:
        try:
            print(f"Trying {workspace}/{project_name}...")
            project = rf.workspace(workspace).project(project_name)
            dataset = project.version(version).download("yolov8", location="dataset")
            print(f"Downloaded to ./dataset/")
            downloaded = True
            break
        except Exception as e:
            print(f"  Failed: {e}")
            continue

    if not downloaded:
        print("\nCould not auto-download. Manual steps:")
        print("1. Go to universe.roboflow.com")
        print("2. Search: 'acne detection face'")
        print("3. Click a dataset with 500+ images and Object Detection annotations")
        print("4. Export as YOLOv8 format to ./dataset/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    args = parser.parse_args()
    download(args.api_key)
