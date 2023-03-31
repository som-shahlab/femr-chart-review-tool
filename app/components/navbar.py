import pynecone as pc
import app.utils as utils

def navbar(state: pc.State):
    return pc.box(
        pc.center(
            pc.heading("Chart Review", font_size=utils.FONT_SIZE_MEDIUM),
            background='lightblue',
            height='1.2em',
        ),
        pc.center(
            pc.input(
                placeholder="Patient ID",
                on_blur=state.set_patient_id,
                width='300px',
                height='2em',
                font_size=utils.FONT_SIZE_MEDIUM,
            ),
            pc.button("Submit", on_click=state.refresh, height='2em', color_scheme='green', margin_left='1em'),
            width="100%",
            padding="0.2em 4em",
            max_width="1440px",
        ),
        width="100%",
        top="0px",
        z_index="5",
        background="white",
        border_bottom="0.1em lightgrey solid",
    )