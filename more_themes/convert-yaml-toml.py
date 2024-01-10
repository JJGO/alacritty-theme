from pathlib import Path
import yaml
import toml


def convert_yaml_to_toml(src: Path) -> Path:
    dst = src.with_suffix(".toml")

    data = yaml.safe_load(src.open("r"))

    data["colors"].pop("author", None)
    data["colors"].pop("name", None)

    with dst.open("w") as f:
        toml.dump(data, f)

    return dst


if __name__ == "__main__":
    import typer

    typer.run(convert_yaml_to_toml)

