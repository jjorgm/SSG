import sys

from copystatic import copy_static
from generatepage import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_static("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")

if __name__ == "__main__":
    main()
