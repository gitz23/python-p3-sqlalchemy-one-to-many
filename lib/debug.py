#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()

#tests
#A Review Belongs to a Game
# Access the first review instance in the database
# review = session.query(Review).first()
# review
# => Review(id=1, score=7, game_id=1)

# Get the game_id foreign key for the review instance
# review.game_id
# => 1
# Find a specific game instance using an ID
# session.query(Game).filter_by(id=review.game_id).first()
# => Game(id=1, title=Jacob Floyd, platform=wii u)
#review.game
# => Game(id=1, title=Jacob Floyd, platform=wii u)

#A Game Has Many Reviews
# game = session.query(Game).first()
# game
# # => Game(id=1, title=Jacob Floyd, platform=wii u)

# reviews = session.query(Review).filter_by(game_id=game.id)
# [review for review in reviews]
# # => [Review(id=1, score=7, id=1), Review(id=2, score=7, id=1), Review(id=3, score=8, id=1)]

# game.reviews
# => [Review(id=1, score=7, game_id=1), Review(id=2, score=7, game_id=1), Review(id=3, score=8, game_id=1)]