import pynecone as pc
from app.components import navbar, sidebar
from app.notes import notes_timeline

class State(pc.State):
    """The app state."""
    patient_id: int = 0
    patient_info: list[dict[str, str]] = [
        { 'title' : 'Age', 'value' : '31', },
        { 'title' : 'Sex', 'value' : 'Male', },
        { 'title' : 'Race', 'value' : 'White', },
        { 'title' : 'Insurance', 'value' : 'Medicaid', },
    ]
    patient_notes: list[dict[str, str]] = [
        { 'date' : '2021-01-01', 'content' : 'Patient is doing well.', 'type' : 'Procedure Note', },
        { 'date' : '2022-01-01', 'content' : 'Patient is not doing well.', 'type' : 'Procedure Note', },
        { 'date' : '2023-01-01', 'content' : 'Patient is having a hard time.', 'type' : 'Progress Note', },
        { 'date' : '2024', 'content' : 'Something here.', 'type' : 'Procedure Note', },
    ]

    def set_patient_info(self, patient_info: list[dict[str,str]]):
        self.patient_info = patient_info
    def set_patient_id(self, patient_id: int):
        self.patient_id = patient_id
    
    def refresh(self):
        print(self.patient_id)

def chart_viewer(state: pc.State):
    return pc.box(
        notes_timeline(state),
        flex_grow=1,
        min_width=0, # needed to prevent width overflow with flexbox
    )

def index() -> pc.Component:
    return pc.box(
        pc.vstack(
            navbar(State),
            pc.flex(
                sidebar(State),
                chart_viewer(State),
                width="100%",
                max_width="1440px",
                padding="0 4em",
            )
        ),
        width="100%",
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
