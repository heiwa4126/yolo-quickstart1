from pathlib import Path

from ultralytics import YOLO


def ex1():
    project_dir = Path(__file__).resolve().parents[2]
    input_dir = project_dir / "examples"
    output_dir = project_dir / "dist"
    output_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO(project_dir / "yolo26n.pt")

    input_paths = [
        input_dir / file for file in ("ex1.jpg", "ex2.jpg", "ex3.jpg", "ex4.jpg")
    ]
    results = model(input_paths)

    if len(results) != len(input_paths):
        raise RuntimeError(
            f"Expected {len(input_paths)} prediction results, got {len(results)}."
        )

    for input_path, result in zip(input_paths, results, strict=True):
        result.save(filename=str(output_dir / input_path.name))


if __name__ == "__main__":
    ex1()
