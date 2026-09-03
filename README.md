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
Saved to: .../Assignment_2/qrcode.png
```


## Files

| File | Purpose |
| --- | --- |
| `qr_generator.py` | Application source code |
| `requirements.txt` | Manifest of package dependencies |
