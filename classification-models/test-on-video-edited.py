import cv2
import numpy as np
import yaml
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_detect_path: str, conf_threshold: float = 0.4, imgsz: int = 640):
        self.model = YOLO(model_detect_path)
        self.conf_threshold = conf_threshold
        self.imgsz = imgsz

    def detect(self, frame):
        detections = self.model(frame, imgsz=self.imgsz)[0]
        return [det for det in detections.boxes.data.tolist() if det[4]>self.conf_threshold]
    
class ObjectClassifier:
    def __init__(self, shape_class_path: str, ext_color_path: str, int_color_path: str, imgsz: int = 320):
        self.models = {
            'shape': YOLO(shape_class_path),
            'ext-color': YOLO(ext_color_path),
            'int-color': YOLO(int_color_path)
        }
        self.imgsz = imgsz

    def classify(self, cropped_object):
        predictions = {}
        for model_name, model in self.models.items():
            pred = model(cropped_object, imgsz = self.imgsz)[0]
            names = pred.names
            probs = pred.probs.data.tolist()
            prediction_text = names[np.argmax(probs)]
            predictions[model_name] = prediction_text

        classification_text = f"{predictions['shape']}, {predictions['ext-color']}, {predictions['int-color']}"
        return classification_text
    
class VideoProcessor:
    def __init__(self, detector: ObjectDetector, classifier: ObjectClassifier, colors: list = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        self.detector = detector
        self.classifier = classifier
        self.colors = colors

    def process_video(self, video_path, output_path):
        cap = cv2.VideoCapture(video_path)

        ret, frame = cap.read()

        H, W, _ = frame.shape

        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

        while True:
            ret, frame = cap.read()
            if not ret: 
                break

            detections = self.detector.detect(frame)
            for det in detections:
                x1, y1, x2, y2, conf, class_id = det
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), self.colors[0], 2)
                cropped_object = frame[int(y1):int(y2), int(x1):int(x2)]
                classification_text = self.classifier.classify(cropped_object)
                cv2.putText(frame, classification_text, (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.colors[1], 2, cv2.LINE_AA)
            
            out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    
yaml_path = '.../'

with open(yaml_path, 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Parsing for Video
video_path = data.get('video_path')
output_path = data.get('output_path')
colors = data.get('colors')

# Parsing for Object Detection
detection = data.get('detection')
model_detect_path = detection.get('model_detect_path')
detection_conf_theshold = detection.get('conf_threshold')
detection_imgsz = detection.get('imgsz')

# Parsing for Object Classifier
classification = data.get('classification')
shape_class_path = classification.get('shape_class_path')
ext_color_path = classification.get('ext_color_path')
int_color_path = classification.get('int_color_path')
classification_imgsz = classification.get('imgsz')


detector = ObjectDetector(model_detect_path, imgsz=detection_imgsz)
classifier = ObjectClassifier(shape_class_path, ext_color_path, int_color_path, imgsz=classification_imgsz)
video_processor = VideoProcessor(detector, classifier, colors)

video_processor.process_video(video_path, output_path)
