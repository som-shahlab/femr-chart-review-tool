import pynecone as pc
import app.utils as utils

def card(contents, title: str = 'Title', color: str = 'lightgrey', **kwargs):
    return pc.box(
        pc.flex(
            pc.center(
                pc.heading(title, font_size=utils.FONT_SIZE_MEDIUM),
                background=color,
                height=utils.change_em_value(utils.FONT_SIZE_MEDIUM, +0.75),
                width='100%',
            ),
            pc.box(
                contents,
                padding="0.5em",
            ),
            direction='column',
        ),
        margin="0.5em",
        border="0.1em solid",
        border_radius="0.5em",
        border_color=color,
        **kwargs,
    )