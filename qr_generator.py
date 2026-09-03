from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

import qrcode
from qrcode.constants import ERROR_CORRECT_M

# Default target used by the assignment when no URL is supplied.
DEFAULT_URL = "https://www.bioxsystems.com/"
DEFAULT_OUTPUT = "qrcode.png"

# Schemes we consider valid for a web address.
VALID_SCHEMES = ("http", "https")


def isValidUrl(url: str) -> bool:
    """Return True if `url` looks like a well-formed http/https address.

    A valid URL needs both a supported scheme (http/https) and a network
    location (the domain), e.g. "https://www.bioxsystems.com/".
    """
    parsed = urlparse(url.strip())
    return parsed.scheme in VALID_SCHEMES and bool(parsed.netloc)


def generateQrCode(url: str, outputPath: Path, box_size: int = 10, border: int = 4) -> Path:
    """Encode `url` as a QR code and save it as a PNG image.

    Args:
        url: The web address to encode.
        outputPath: File path where the PNG image is written.
        box_size: Pixel size of each individual QR "module" (square).
        border: Width of the quiet zone, in modules (4 is the spec minimum).

    Returns:
        The path of the image that was written.

    Raises:
        ValueError: If `url` is not a valid http/https address.
    """
    if not isValidUrl(url):
        raise ValueError(f"'{url}' is not a valid http/https URL.")

    # version=None lets the library pick the smallest symbol size that fits.
    # ERROR_CORRECT_M recovers roughly 15% of damaged/obscured data, a good
    # balance between resilience and symbol size for printed URLs.
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url.strip())
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    # Make sure the destination directory exists before writing.
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    image.save(outputPath)
    return outputPath


def parseArguments(argv: list[str] | None = None) -> argparse.Namespace:
    """Define and parse the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate a QR code image from a URL."
    )
    parser.add_argument(
        "url",
        nargs="?",
        help=f"URL to encode (default: prompt, or {DEFAULT_URL}).",
    )
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output PNG file path (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "-s", "--box-size",
        type=int,
        default=10,
        help="Pixel size of each QR module (default: 10).",
    )
    return parser.parse_args(argv)


def promptForUrl() -> str:
    """Ask the user for a URL, falling back to the assignment default."""
    entered = input(f"Enter a URL [{DEFAULT_URL}]: ").strip()
    return entered or DEFAULT_URL


def main(argv: list[str] | None = None) -> int:
    """Program entry point. Returns a shell exit code (0 = success)."""
    args = parseArguments(argv)

    # Use the command-line URL when given; otherwise ask the user for one.
    url = args.url if args.url else promptForUrl()

    try:
        saved_to = generateQrCode(url, Path(args.output), args.box_size)
    except ValueError as error:
        # Invalid input: report clearly and exit non-zero.
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        # Disk/permission problems while saving the image.
        print(f"Error: could not save image - {error}", file=sys.stderr)
        return 1

    print(f"QR code for {url}")
    print(f"Saved to: {saved_to.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
