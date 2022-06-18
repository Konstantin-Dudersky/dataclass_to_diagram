"""Тест."""

from konstantin_docs.main import generate_images


def main() -> None:
    """Точка входа."""
    generate_images(path_src="test/dia_src", path_dist="test/dia_dist")


if __name__ == "__main__":
    main()
