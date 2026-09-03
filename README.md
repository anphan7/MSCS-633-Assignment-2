# QR Code Generator (MSCS-633 - Assignment 2)

A small Python application that generates a QR (quick-response) code image
from a URL entered by the user. Built for the Biox Systems site
(https://www.bioxsystems.com/), but it will encode any valid http/https URL.

## Requirements

- Python 3.9 or newer
- Packages listed in `requirements.txt` (`qrcode` and `pillow`)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Pass the URL as an argument:

```bash
python qr_generator.py https://www.bioxsystems.com/
```

Or run with no arguments and type the URL at the prompt (press Enter to accept
the default Biox Systems URL):

```bash
python qr_generator.py
```

### Options

| Option | Description | Default |
| --- | --- | --- |
| `url` | The URL to encode (positional, optional) | prompts the user |
| `-o`, `--output` | Path of the PNG file to write | `qrcode.png` |
| `-s`, `--box-size` | Pixel size of each QR module | `10` |

## Example output

```
$ python qr_generator.py https://www.bioxsystems.com/
QR code for https://www.bioxsystems.com/
Saved to: .../Assignment_2/biox_qr.png
```


## Files

| File | Purpose |
| --- | --- |
| `qr_generator.py` | Application source code |
| `requirements.txt` | Manifest of package dependencies |

## Notes on implementation

- Input is validated with `urllib.parse.urlparse`; only `http` and `https`
  addresses with a domain are accepted.
- Error correction level **M** is used, which recovers roughly 15% of a
  damaged or partially obscured symbol.
- `version=None` with `fit=True` lets the library choose the smallest QR
  symbol size that fits the data.
