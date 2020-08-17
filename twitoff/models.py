"""SQLAlchemy models and utility functions for TwitOff."""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet text and data."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for text + links
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '-Tweet {}-'.format(self.text)


def insert_example_users():
    """Example data to play with."""
    austen = User(id=1, name='austen')
    austen_tweet = Tweet(id=1, text='Lambda is cool!', user_id=1)
    elon = User(id=2, name='elonmusk')
    elon_tweet = Tweet(id=2, text='SpaceX is cool!', user_id=2)
    elon_tweet2 = Tweet(
        id=6, text='The Model S will now come with ejection seats.', user_id=2)
    fred = User(id=3, name='fred')
    fred_tweet = Tweet(id=3, text='SpaceX and Lambda are cool!', user_id=3)
    fred_tweet2 = Tweet(
        id=4, text='How much wood would a woodchuck chuck?', user_id=3)
    fred_tweet3 = Tweet(
        id=5, text='The meaning of life and everything is 42.', user_id=3)
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.add(fred)
    DB.session.commit()
    DB.session.add(austen_tweet)
    DB.session.add(fred_tweet)
    DB.session.add(fred_tweet2)
    DB.session.add(fred_tweet3)
    DB.session.add(elon_tweet)
    DB.session.add(elon_tweet2)
    DB.session.commit()
