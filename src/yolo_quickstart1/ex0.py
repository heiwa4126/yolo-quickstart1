from ultralytics import YOLO


def ex0():
    model = YOLO("yolo26n.pt")  # load a pretrained YOLO26n detection model
    results = model(
        "https://ultralytics.com/images/bus.jpg", save=True
    )  # predict and save the annotated image
    return results


if __name__ == "__main__":
    ex0()
