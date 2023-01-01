from habit_tracker.app import create_app


def run():
    app = create_app()
    app.run()


