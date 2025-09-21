from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, IntegerField, DateField, BooleanField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[Length(max=50)])
    last_name = StringField('Last Name', validators=[Length(max=50)])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=6, message='Password must be at least 6 characters long')
    ])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(), 
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators=[DataRequired(), Length(max=200)])
    content = TextAreaField('Your Review', validators=[DataRequired()], 
                          widget=TextArea(), render_kw={"rows": 5})
    rating = SelectField('Rating', choices=[
        (5, '⭐⭐⭐⭐⭐ Excellent'),
        (4, '⭐⭐⭐⭐ Very Good'),
        (3, '⭐⭐⭐ Good'),
        (2, '⭐⭐ Fair'),
        (1, '⭐ Poor')
    ], validators=[DataRequired()], coerce=int)
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[Optional()])
    place_name = StringField('Place Name', validators=[Optional()])
    place_type = SelectField('Place Type', choices=[
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('attraction', 'Tourist Attraction'),
        ('transport', 'Transportation'),
        ('shopping', 'Shopping'),
        ('other', 'Other')
    ], validators=[Optional()])
    verified_visit = BooleanField('I actually visited this place')
    submit = SubmitField('Submit Review')

class WishlistForm(FlaskForm):
    place_name = StringField('Place Name', validators=[DataRequired(), Length(max=200)])
    place_type = SelectField('Place Type', choices=[
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('attraction', 'Tourist Attraction'),
        ('transport', 'Transportation'),
        ('shopping', 'Shopping'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()], 
                              widget=TextArea(), render_kw={"rows": 3})
    submit = SubmitField('Add to Wishlist')

class ItineraryForm(FlaskForm):
    title = StringField('Trip Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[Optional()], 
                              widget=TextArea(), render_kw={"rows": 3})
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[Optional()])
    start_date = DateField('Start Date', validators=[Optional()])
    end_date = DateField('End Date', validators=[Optional()])
    is_public = BooleanField('Make this itinerary public')
    submit = SubmitField('Create Itinerary')

class ItineraryItemForm(FlaskForm):
    day_number = IntegerField('Day Number', validators=[DataRequired(), NumberRange(min=1)])
    time_slot = SelectField('Time Slot', choices=[
        ('morning', 'Morning (6AM-12PM)'),
        ('afternoon', 'Afternoon (12PM-6PM)'),
        ('evening', 'Evening (6PM-12AM)'),
        ('night', 'Night (12AM-6AM)')
    ], validators=[Optional()])
    place_name = StringField('Place Name', validators=[DataRequired(), Length(max=200)])
    place_type = SelectField('Place Type', choices=[
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('attraction', 'Tourist Attraction'),
        ('transport', 'Transportation'),
        ('shopping', 'Shopping'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()], 
                              widget=TextArea(), render_kw={"rows": 2})
    address = StringField('Address', validators=[Optional(), Length(max=300)])
    estimated_duration = IntegerField('Duration (minutes)', validators=[Optional(), NumberRange(min=1)])
    cost_estimate = StringField('Estimated Cost', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()], 
                        widget=TextArea(), render_kw={"rows": 2})
    submit = SubmitField('Add Item')

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[Optional()])
    country = SelectField('Country', choices=[
        ('', 'All Countries'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Spain', 'Spain'),
        ('Germany', 'Germany'),
        ('United Kingdom', 'United Kingdom'),
        ('Japan', 'Japan'),
        ('Turkey', 'Turkey'),
        ('Greece', 'Greece'),
        ('Portugal', 'Portugal'),
        ('Netherlands', 'Netherlands'),
        ('Switzerland', 'Switzerland'),
        ('Austria', 'Austria'),
        ('Belgium', 'Belgium'),
        ('Czech Republic', 'Czech Republic'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Croatia', 'Croatia'),
        ('Norway', 'Norway'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Finland', 'Finland'),
        ('Iceland', 'Iceland'),
        ('Ireland', 'Ireland'),
        ('United States', 'United States'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Brazil', 'Brazil'),
        ('Argentina', 'Argentina'),
        ('Chile', 'Chile'),
        ('Mexico', 'Mexico'),
        ('India', 'India'),
        ('China', 'China'),
        ('Thailand', 'Thailand'),
        ('Vietnam', 'Vietnam'),
        ('Indonesia', 'Indonesia'),
        ('Malaysia', 'Malaysia'),
        ('Singapore', 'Singapore'),
        ('South Korea', 'South Korea'),
        ('Philippines', 'Philippines'),
        ('South Africa', 'South Africa'),
        ('Egypt', 'Egypt'),
        ('Morocco', 'Morocco'),
        ('Israel', 'Israel'),
        ('Jordan', 'Jordan'),
        ('UAE', 'United Arab Emirates'),
        ('Qatar', 'Qatar'),
        ('Saudi Arabia', 'Saudi Arabia')
    ], validators=[Optional()])
    place_type = SelectField('Place Type', choices=[
        ('', 'All Types'),
        ('hotel', 'Hotels'),
        ('restaurant', 'Restaurants'),
        ('attraction', 'Attractions'),
        ('transport', 'Transportation'),
        ('shopping', 'Shopping'),
        ('beach', 'Beaches'),
        ('mountain', 'Mountains'),
        ('city', 'Cities'),
        ('nature', 'Nature'),
        ('culture', 'Cultural Sites'),
        ('adventure', 'Adventure'),
        ('nightlife', 'Nightlife'),
        ('family', 'Family Friendly')
    ], validators=[Optional()])
    rating_min = SelectField('Minimum Rating', choices=[
        (0, 'Any Rating'),
        (1, '1+ Stars'),
        (2, '2+ Stars'),
        (3, '3+ Stars'),
        (4, '4+ Stars'),
        (5, '5 Stars Only')
    ], validators=[Optional()], coerce=int, default=0)
    submit = SubmitField('Search')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired()], 
                          widget=TextArea(), render_kw={"rows": 5})
    submit = SubmitField('Send Message')
