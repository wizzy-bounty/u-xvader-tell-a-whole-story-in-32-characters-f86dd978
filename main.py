import os

NAME = "It Worked Until Dave Touched It"


def entry_path(out_dir: str) -> str:
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = entry_path(out_dir)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(NAME)


if __name__ == "__main__":
    main()
