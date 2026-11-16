from pathlib import Path

from ultralytics import YOLO


def ex1():
    project_dir = Path(__file__).resolve().parents[2]
    input_dir = project_dir / "examples"
    output_dir = project_dir / "dist"
    output_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO(project_dir / "yolo26n.pt")

    for file in ("ex1.jpg", "ex2.jpg"):
        input_path = input_dir / file
        output_path = output_dir / file

        results = model(input_path)
        if not results:
            raise RuntimeError(
                f"No prediction result for {input_path}; check that it is a readable image."
            )

        results[0].save(filename=str(output_path))


if __name__ == "__main__":
    ex1()
