from apps import create_app

cms_app = create_app()

if __name__ == '__main__':
    from apps.models import db

    with cms_app.app_context():
        db.create_all()
    print(cms_app.url_map)
    cms_app.run()
