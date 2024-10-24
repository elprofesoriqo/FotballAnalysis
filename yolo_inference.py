from ultralytics import YOLO


model = YOLO('yolov8x')


results = model.predict('input_videos/name.mp4', save=True)
for box in results[0].boxes:
    print(box)