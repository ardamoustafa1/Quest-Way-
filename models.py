from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Create db instance here
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    profile_picture = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    reviews = db.relationship('Review', backref='author', lazy=True)
    wishlist_items = db.relationship('WishlistItem', backref='user', lazy=True)
    itineraries = db.relationship('Itinerary', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    place_name = db.Column(db.String(200), nullable=True)
    place_type = db.Column(db.String(50), nullable=True)  # hotel, restaurant, attraction, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Additional fields for enhanced reviews
    helpful_count = db.Column(db.Integer, default=0)
    images = db.Column(db.JSON, nullable=True)  # Store image URLs as JSON array
    verified_visit = db.Column(db.Boolean, default=False)
    
    # Relationships
    user = db.relationship('User', backref='user_reviews', lazy=True)
    
    def __repr__(self):
        return f'<Review {self.title}>'

class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_name = db.Column(db.String(200), nullable=False)
    place_type = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WishlistItem {self.place_name}>'

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    is_public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    itinerary_items = db.relationship('ItineraryItem', backref='itinerary', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Itinerary {self.title}>'

class ItineraryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    time_slot = db.Column(db.String(50), nullable=True)  # morning, afternoon, evening
    place_name = db.Column(db.String(200), nullable=False)
    place_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    estimated_duration = db.Column(db.Integer, nullable=True)  # in minutes
    cost_estimate = db.Column(db.Float, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    order_index = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<ItineraryItem {self.place_name}>'

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature_high = db.Column(db.Float, nullable=True)
    temperature_low = db.Column(db.Float, nullable=True)
    weather_condition = db.Column(db.String(100), nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    wind_speed = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WeatherData {self.city} - {self.date}>'

class CurrencyRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_currency = db.Column(db.String(3), nullable=False)
    to_currency = db.Column(db.String(3), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<CurrencyRate {self.from_currency} to {self.to_currency}>'
