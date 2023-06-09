import pynecone as pc

config = pc.Config(
    app_name="app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3000,
    frontend_packages=[
        'react-event-timeline',
    ]
)
