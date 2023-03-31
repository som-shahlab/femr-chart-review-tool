from pcconfig import config
import pynecone as pc

FONT_SIZE_XS = '0.65em'
FONT_SIZE_SMALL = '0.85em'
FONT_SIZE_MEDIUM = '1em'
FONT_SIZE_LARGE = '1.2em'
FONT_SIZE_XL = '1.5em'

def change_em_value(current_em: str, delta: float) -> str:
    """Change the em value of a font size."""
    return f'{float(current_em[:-2]) + delta}em'