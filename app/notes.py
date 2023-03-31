import pynecone as pc
import app.utils as utils
from app.components import card

class Timeline(pc.Component):
    library = "react-event-timeline"
    tag = "Timeline"
    lineColor: pc.Var[str]

class TimelineEvent(pc.Component):
    library = "react-event-timeline"
    tag = "TimelineEvent"
    title: pc.Var[str]
    subtitle: pc.Var[str]
    createdAt: pc.Var[str]

def _note(info: dict):
    return TimelineEvent.create(
        pc.text(info['content']),
        createdAt=info['date'],
        title=info['type'],
    )

def notes_timeline(state: pc.State):
    notes: list[dict[str, str]] = state.patient_notes
    return card(
        pc.box(
            Timeline.create(
                pc.foreach(notes, _note),
                lineColor="black",
            ),
            max_height="calc(100vh - 150px)",
            overflow="auto",
        ),
        title='Notes Timeline',
        width="100%",
    )
