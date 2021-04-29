from sqlalchemy import Column, Integer, String,Numeric,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'user'

    id_account = Column(Integer, primary_key=True,
                        nullable=False, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    card_number = Column(String)
    exp_date = Column(String)
    security_code = Column(String)
    next_billing = Column(String)
    plan_id = Column(String,ForeignKey('Plan.plan_id'), nullable = False)
    children = relationship("Billing","Viewer")
class Billing(Base):
    __tablename__ = 'billing'

    billing_date = Column(String , nullable = False)
    billing_id = Column(String, primary_key=True ,nullable = False )
    id_account =	Column(Integer, ForeignKey('User.id_account'), nullable = False ) 

class Cast(Base):
    __tablename__ = 'cast'
    id_casting = Column(Integer, primary_key=True ,nullable = False )
    name = Column(String , nullable = False)
    children = relationship("Casting")

class Casting(Base):
    __tablename__ = 'casting'
    id_casting =	Column(Integer,ForeignKey('Cast.id_movie') , nullable = False,primary_key=True)
    id_movie	= Column(Integer ,ForeignKey('Movie_and_series.id_movie'), nullable = False,primary_key=True)
    children = relationship("Movie_and_series","Cast")
class Director(Base):
    __tablename__ = 'director'
    id_director	= Column(Integer , nullable = False,primary_key=True)
    name =	Column(String , nullable = False)
    children = relationship("Director_movie")

class Director_movie(Base):
    __tablename__ = 'director_movie'
    id_movie	=Column(Integer,ForeignKey('Movie_and_series.id_movie') , nullable = False,primary_key=True)
    id_director	=Column(Integer ,ForeignKey('Director.id_director'), nullable = False,primary_key=True)

class Episode(Base):
    __tablename__ = 'episode'
    id_episode = Column(Integer, nullable = False,primary_key=True)
    id_season = Column(Integer,ForeignKey('Season.id_season'))
    episode_name = Column(String)
    no_episode = Column(Integer, nullable = False)
    n_views = Column(Integer, nullable = False)
    description = Column(String)
    children = relationship("Episode_tag","Soundtrack","Subtitle")

class Episode_tag(Base):
    __tablename__ = 'episode_tag'
    id_episode = Column(Integer,ForeignKey('Episode.id_episode'), nullable = False,primary_key=True)
    id_tag =	 Column(Integer, nullable = False,primary_key=True)
    children = relationship("Tag")

class Genres(Base):
    __tablename__ = 'Genres'
    id_genres	=Column(Integer, nullable = False,primary_key=True)
    name	=Column(String, nullable = False)
    children = relationship("Genres_movie")

class Genres_movie(Base):
    __tablename__ = 'genres_movie'
    id_movie = Column(Integer, ForeignKey('Movie_and_series.id_movie'),nullable = False,primary_key=True)
    id_genres	= Column(Integer, ForeignKey('Genres.id_genres'),nullable = False,primary_key=True)

class History(Base):
    __tablename__ = 'history'
    id_viewer	=Column(Integer, nullable = False,primary_key=True)
    id_movie = Column(Integer,ForeignKey('Movie_and_series.id_movie'), primary_key=True ,  nullable = False)
    date	= Column(String, nullable = False,primary_key=True)
    stop_time 	= Column(String)

class Movie_and_series(Base):
    __tablename__ = 'movie_and_series'
    id_movie	= Column(Integer, nullable = False,primary_key=True)
    name =	Column(String, nullable = False)
    rate =	Column(Integer, nullable = False)
    is_series =	Column(Integer, nullable = False)
    children = relationship("History","My_list","Casting","Genres_movie","Director_movie","Season","Staff_history_movie")

class My_list(Base):
    __tablename__ = 'my_list'
    id_movie =	Column(Integer,ForeignKey('Movie_and_series.id_movie'),nullable = False,primary_key=True)
    id_viewer= 	Column(Integer,ForeignKey('Viewer.id_viewer'),nullable = False,primary_key=True)

class Plan(Base):
    __tablename__ = 'plan'
    plan_id =	Column(Integer, nullable = False,primary_key=True)
    name	= Column(String, nullable = False)
    price	= Column(Numeric, nullable = False)
    n_monitor	= Column(Integer, nullable = False)
    phone	= Column(Integer, nullable = False)
    web =	Column(Integer, nullable = False)
    television	= Column(Integer, nullable = False)
    resolution	= Column(String, nullable = False)
    children = relationship("User")

class Season(Base):
    __tablename__ = 'Season'
    id_movie	= Column(Integer,ForeignKey('Movie_and_series.id_movie'), nullable = False)
    id_season	= Column(Integer, nullable = False,primary_key=True)
    name	= Column(String)
    n_episode	= Column(Integer)
    year	= Column(Integer)
    children = relationship("Episode")

class Soundtrack(Base):
    id_soundtrack	= Column(Integer, nullable = False,primary_key=True)
    language	= Column(String, nullable = False,primary_key=True)
    id_episode	= Column(Integer,ForeignKey('Episode.id_episode'), nullable = False,primary_key=True)

class Staff(Base):
    id_staff	= Column(Integer, nullable = False ,primary_key=True,autoincrement=True)
    first_name	= Column(String, nullable = False)
    last_name	= Column(String, nullable = False)
    email	= Column(String, nullable = False)
    password	= Column(String, nullable = False)
    salary	= Column(Integer, nullable = False)
    children = relationship("Staff_history_movie","Staff_history_soundtrack","Staff_history_subtitle")

class Staff_history_movie(Base):
    id_seq	= Column(Integer, nullable = False,primary_key=True)
    id_movie	= Column(Integer, ForeignKey('Movie_and_series.id_movie'),nullable = False)
    id_staff	= Column(Integer,ForeignKey('Staff.id_staff'), nullable = False)
    date	= Column(String)
    start_date	= Column(String)
    expiration_date	= Column(String)
    comment	= Column(String)

class Staff_history_soundtrack(Base):
    id_seq	= Column(Integer, nullable = False,primary_key=True,autoincrement=True)
    id_staff	= Column(Integer,ForeignKey('Staff.id_staff'), nullable = False)
    start_date	= Column(String)
    date	= Column(String)

class Staff_history_subtitle(Base):
    id_seq	= Column(Integer, nullable = False,primary_key=True)
    id_staff = Column(Integer,ForeignKey('Staff.id_staff'), nullable = False)
    start_date	= Column(String)
    date	= Column(String)

class Subtitle(Base):
    id_sub	= Column(Integer, nullable = False,primary_key=True)
    language	= Column(String,nullable = False,primary_key=True)
    id_episode	= Column(Integer,ForeignKey('Episode.id_episode'), nullable = False,primary_key=True)
    file	= Column(String)

class Tag(Base):
    id_seq = Column(Integer,primary_key = True, nullable = False,autoincrement=True)
    id_tag	= Column(Integer,children = relationship("Episode_tag.id_tag"), nullable = False)
    name	= Column(String ,unique=True)

class Viewer(Base):
    id_viewer	= Column(Integer, nullable = False,primary_key=True,autoincrement=True)
    id_account	= Column(Integer,ForeignKey('parent.id'), nullable = False)
    pin_number	= Column(Integer)
    name	= Column(String)
    is_kid	= Column(Integer, nullable = False)
    children = relationship("My_list")
