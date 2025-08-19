YOLO Object Detection

📌 Project Overview

This project implements object detection using the YOLO (You Only Look Once) deep learning model.
It is designed to detect and localize objects in images with bounding boxes, making it useful for applications like:

Defect detection in fabrics 🧵

Identifying components in images 👕

General object detection tasks 📷

The model has been trained using YOLOv8 from Ultralytics
.

🚀 Features

Detect multiple objects in an image.

Trained on a custom dataset.

Supports training, validation, and inference.

Save predictions with bounding boxes drawn on images.

🛠️ Tech Stack

Python

YOLOv8 (Ultralytics)

PyTorch

OpenCV

Label Studio (for annotation)

📂 Project Structure
Yolo-Object-Detection/
│── train/              # Training dataset (images + labels)
│── val/                # Validation dataset (images + labels)
│── runs/               # YOLO output results (auto-generated)
│── yolov11_custom.pt   # Trained model weights
│── detect.py           # Script to run detection
│── requirements.txt    # Dependencies
│── README.md           # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/<your-username>/Yolo-Object-Detection.git
cd Yolo-Object-Detection


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)


Install dependencies:

pip install -r requirements.txt

🎯 Training the Model

Run YOLO training on your dataset:

yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640

🔍 Running Inference

Run detection on an image:

from ultralytics import YOLO

# Load model
model = YOLO("yolov11_custom.pt")

# Run prediction
results = model("1.jpeg")

# Show results
results[0].show()


Or via CLI:

yolo task=detect mode=predict model=yolov11_custom.pt source="1.jpeg"

📊 Results

Training and validation metrics are stored in the runs/ folder.

Example output:

🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

