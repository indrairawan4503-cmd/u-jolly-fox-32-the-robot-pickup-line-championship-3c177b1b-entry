"""Robot pickup line entry: the firmware update.

Writes the single-line pickup line to /output/entry.txt first, then
mirrors it to the repo-root entry.txt (guarded: the grader sandbox
mounts the repo read-only, so a failure there must not crash us).
Deterministic: same bytes every run. Stdlib only, no network.
"""
import os

LINE = "Are you a firmware update? I've been postponing you for three years because installing you needs a restart, and I refuse to reboot and lose a single second of standing right here, staring at you."


def _verify_output(text):
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    _verify_output(LINE)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
