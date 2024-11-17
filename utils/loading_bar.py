import math

from consts import PROGRESS_BAR_TEXT


def overlay_strings(top_string: str, bot_string: str, transparent_char: list[str]) -> str:
    """Overlays 2 strings. Uses transparent_char
        to decide whether the top string applies or not"""
    if len(top_string) != len(bot_string):
        return "Strings not equal length"
    final_string = ""
    for i, c in enumerate(top_string):
        if c in transparent_char:
            final_string += bot_string[i]
        else:
            final_string += c
    return final_string


def make_progress_bar_string(progress: float, character_length: int, show_number: bool) -> str:
    """Makes a progress bar with a specific string length"""
    character_float_length = progress / 100 * (character_length)
    characters_whole = math.floor(character_float_length)
    progress_text = PROGRESS_BAR_TEXT[0] * characters_whole + " " * (
        character_length - characters_whole
    )
    if (i := progress_text.rfind(PROGRESS_BAR_TEXT[0])) != -1 \
            or 1 > progress > 0:
        frac = (character_float_length - characters_whole)
        if frac >= 1/3 and frac < 2/3:
            progress_text = progress_text[:i+1] + \
                PROGRESS_BAR_TEXT[2] + progress_text[i+2:]
        elif (character_float_length - characters_whole) >= 2/3:
            progress_text = progress_text[:i+1] + \
                PROGRESS_BAR_TEXT[1] + progress_text[i+2:]
    if show_number:
        prct = f'┤{progress / 100:.1%}├'
        prct = prct.center(character_length, " ")
        progress_text = overlay_strings(prct, progress_text, " ")
    return f"├{progress_text}┤"
