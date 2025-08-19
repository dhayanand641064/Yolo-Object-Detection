from ultralytics import YOLO

# Load the model only once
model = YOLO("yolov11_custom.pt")

image_path = "1.jpeg"
    
# Run prediction and get results
results = model(image_path)

    # Display number of detections
for r in results:
    print("Number of boxes detected:", len(r.boxes))

    # Predict and save the output with details
model.predict(
        source=image_path,
        show=True,
        save=True,
        conf=0.25,
        save_txt=True,
        save_conf=True,
        save_crop=True
)