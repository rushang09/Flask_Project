# create_db.py
from app import create_app, db
from app.models import Item  # Explicitly import your model

# Create the app and the database
app = create_app()

with app.app_context():
    # Create all the tables defined in models.py
    db.create_all()
    print("Tables created successfully!")

