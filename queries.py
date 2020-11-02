User.query.filter_by(email = 'cats@gmail.com').one()

Movie.query.filter_by(title = 'Cape Fear').all()

User.query.filter_by(zipcode = '90703').all()

Rating.query.filter(Rating.score == 5).all()

Rating.query.filter((Rating.user_id == 6) & (Rating.movie_id == 7)).all()

Rating.query.filter(Rating.score > 3).all()