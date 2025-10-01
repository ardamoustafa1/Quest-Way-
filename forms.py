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
    content = TextAreaField('Your Review', validators=[DataRequired()], 
                          widget=TextArea(), render_kw={"rows": 6, "placeholder": "Share your experience in detail..."})
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    country = SelectField('Country', choices=[
        ('', 'Select a country'),
        ('Turkey', 'Turkey'),
        ('Germany', 'Germany'),
        ('Austria', 'Austria'),
        ('Belgium', 'Belgium'),
        ('Bulgaria', 'Bulgaria'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Estonia', 'Estonia'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Greece', 'Greece'),
        ('Italy', 'Italy'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Romania', 'Romania'),
        ('Slovenia', 'Slovenia'),
        ('Netherlands', 'Netherlands'),
        ('Ireland', 'Ireland'),
        ('Spain', 'Spain')
    ], validators=[DataRequired()])
    place_name = SelectField('Name', choices=[('', 'Select a place')], validators=[DataRequired()])
    place_type = SelectField('Type', choices=[
        ('famous_places', 'Famous Places'),
        ('top_hotels', 'Top Hotels'),
        ('top_restaurants', 'Top Restaurants'),
        ('famous_dishes', 'Famous Dishes'),
        ('transport', 'Transport')
    ], validators=[DataRequired()])
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
        ('Turkey', 'Turkey'),
        ('Germany', 'Germany'),
        ('Austria', 'Austria'),
        ('Belgium', 'Belgium'),
        ('Bulgaria', 'Bulgaria'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Estonia', 'Estonia'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Greece', 'Greece'),
        ('Italy', 'Italy'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Romania', 'Romania'),
        ('Slovenia', 'Slovenia'),
        ('Netherlands', 'Netherlands'),
        ('Ireland', 'Ireland'),
        ('Spain', 'Spain')
    ], validators=[Optional()])
    place_type = SelectField('Place Type', choices=[
        ('', 'All Types'),
        ('famous_places', 'Famous Places'),
        ('top_hotels', 'Top Hotels'),
        ('top_restaurants', 'Top Restaurants'),
        ('famous_dishes', 'Famous Dishes'),
        ('transport', 'Transport')
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
