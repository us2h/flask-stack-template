def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
