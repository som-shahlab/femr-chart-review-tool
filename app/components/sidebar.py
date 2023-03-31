import pynecone as pc
import app.utils as utils
from app.components import card

def _patient_info_attribute(info: dict):
    return pc.hstack(
        pc.text(info['title'] + ":", font_weight='bold'),
        pc.text(info['value'], margin_bottom='0.5em'),
    )

def sidebar(state: pc.State):
    patient_info: list[dict[str,str]] = state.patient_info
    return card(
        pc.box(
            pc.foreach(patient_info, _patient_info_attribute),
        ),
        title='Patient Info',
        width='300px',
        flex_shrink=0,
    )