from datetime import datetime, timedelta

from sqlalchemy.sql.expression import distinct
from app.models.payment import Payment
from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserHash):
    try:
        content = models.User(
            email=user.email,
            password=user.password,
            phone_number=None,
            firstname=None,
            lastname=None,
            card_number=None,
            exp_date=None,
            security_code=None,
            next_billing=None,
            plan_id=None
        )
        db.add(content)
        db.commit()
        db.refresh(content)
        return True
    except:
        return False


def get_user_password(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return schemas.UserHash(email=user.email, password=user.password)
    return None


def get_user_from_token(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return schemas.UserId(email=user.email, id_account=user.id_account, next_billing=user.next_billing)
    return None


def get_user_payment(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return Payment(
            email=user.email,
            phone_number=user.phone_number,
            firstname=user.firstname,
            lastname=user.lastname,
            card_number=user.card_number,
            exp_date=user.exp_date,
            security_code=user.security_code,
            next_billing=user.next_billing,
            plan_id=user.plan_id
        )
    return None


def set_user_payment(db: Session, email: str, payment: Payment):
    try:
        db.query(models.User).filter(models.User.email == email).update(
            {
                models.User.phone_number: payment.phone_number,
                models.User.card_number: payment.card_number,
                models.User.firstname: payment.firstname,
                models.User.lastname: payment.lastname,
                models.User.exp_date: payment.exp_date,
                models.User.security_code: payment.security_code,
                models.User.plan_id: payment.plan_id,
                models.User.next_billing: datetime.now().date(
                ) + timedelta(days=30) if payment.plan_id else payment.next_billing
            }, synchronize_session=False)
        db.commit()
        return True
    except:
        return False


def get_user_viewer(db: Session, id_account: int):
    viewer = db.query(models.Viewer).filter(
        models.Viewer.id_account == id_account)
    viewer_list = []
    if viewer.count() != 0:
        for i in viewer:
            viewer_list.append(schemas.Viewer(
                id_viewer=i.id_viewer,
                pin_number=i.pin_number,
                name=i.name,
                is_kid=i.is_kid
            ))
        return viewer_list
    else:
        _ = add_user_viewer(db, id_account, schemas.Viewer(
            name='You', is_kid=False))
        viewer_list = get_user_viewer(db, id_account)
    return viewer_list


def add_user_viewer(db: Session, id_account: int, viewer: schemas.Viewer):
    try:
        content = models.Viewer(
            pin_number=viewer.pin_number if viewer.pin_number else None,
            id_account=id_account,
            name=viewer.name,
            is_kid=viewer.is_kid
        )
        db.add(content)
        db.commit()
        db.refresh(content)
        return viewer
    except:
        return False


def delete_user_viewer(db: Session, viewer: int):
    v = db.query(models.Viewer).filter(
        models.Viewer.id_viewer == viewer).delete()
    db.commit()
    return v


def delete_user_viewer_all(db: Session, user_id: int):
    v = db.query(models.Viewer).filter(
        models.Viewer.id_account == user_id).delete()
    db.commit()
    return v


def update_user_viewer(db: Session, viewer: schemas.Viewer):
    try:
        db.query(models.Viewer).filter(models.Viewer.id_viewer == viewer.id_viewer).update(
            {
                models.Viewer.name: viewer.name,
                models.Viewer.is_kid: viewer.is_kid,
                models.Viewer.pin_number: viewer.pin_number
            }
        )
        db.commit()
        return True
    except:
        return False


def delete_user_db(db: Session, user_id: int):
    v = db.query(models.User).filter(
        models.User.id_account == user_id).delete()
    db.commit()
    return v


def change_password_user(db: Session, pwd: str, email: str):
    try:
        db.query(models.User).filter(models.User.email == email).update(
            {
                models.User.password: pwd
            }
        )
        db.commit()
        return True
    except:
        return False


def get_movie_actors(db: Session, movie_id: int):
    command = """
        SELECT mov.id_movie , mov.name , cas.name as "cast"
	    FROM public.movie_and_series mov
	    JOIN public.casting casti
	    ON casti.id_movie = mov.id_movie
	    JOIN public.cast cas
	    ON casti.id_casting = cas.id_casting 
        WHERE mov.id_movie = {};
    """.format(movie_id)
    actors = db.execute(command)
    return [i[2] for i in actors]


def get_movie_directors(db: Session, movie_id: int):
    command = """
        SELECT mov.id_movie , mov.name , di.name as "director"
	    FROM public.movie_and_series mov
	    JOIN public.director_movie dim
	    ON dim.id_movie = mov.id_movie
	    JOIN public.director di
	    ON di.id_director = dim.id_director
        WHERE mov.id_movie = {};
    """.format(movie_id)
    directors = db.execute(command)
    return [i[2] for i in directors]


def get_movie_detail_db(db: Session, movie_id: int):
    v = db.query(models.Movie_and_series).filter(
        models.Movie_and_series.id_movie == movie_id).first()
    rate = v.rate
    name = v.name
    w = db.query(models.Season).filter(
        models.Season.id_movie == movie_id).first()
    description = w.description
    year = w.year
    n_episode = w.n_episode
    n_season = db.query(models.Season).filter(
        models.Season.id_movie == movie_id).count()
    return rate, name, description, year, n_episode, n_season


def get_movie_genres(db: Session, movie_id: int):
    command = """
        SELECT mov.id_movie , mov.name ,gr.name as "Genres"
	    FROM public.movie_and_series mov
	    JOIN public.genres_movie grm
	    ON grm.id_movie = mov.id_movie
	    JOIN public.genres gr
	    ON grm.id_genres = gr.id_genres
        WHERE mov.id_movie = {};
    """.format(movie_id)
    directors = db.execute(command)
    return [i[2] for i in directors]


def get_actor_movie(db: Session, actor: str):
    command = """
        select cas.id_casting, cas.name, casti.id_movie, mov.name
        from public.cast cas
        join public.casting casti
        on casti.id_casting = cas.id_casting
        join public.movie_and_series mov
        on mov.id_movie = casti.id_movie
        where lower(cas.name) = lower('{}');
    """.format(actor)
    movies = db.execute(command)
    d = dict()
    for i in movies:
        d[int(i[2])] = i[3]
    return d


def get_movie_episode_db(db: Session, movie_id: int):
    command = """
        SELECT mov.id_movie,se.name,Ep.episode_name,Ep.no_episode,Ep.description
	    FROM public.movie_and_series mov
	    JOIN public.Season Se
	    ON Se.id_movie = mov.id_movie
	    JOIN public.Episode Ep
	    ON Ep.id_season = se.id_season
	    where mov.id_movie = {}
	;
    """.format(movie_id)
    episodes = db.execute(command)
    episode_list = []
    for i in episodes:
        episode_list.append(schemas.Episode(
            name=i[2],
            no_episode=i[3],
            description=i[4]
        ))
    return episode_list


def get_staff_password(db: Session, email: str):
    staff = db.query(models.Staff).filter(models.Staff.email == email).first()
    if staff:
        return schemas.UserHash(email=staff.email, password=staff.password)
    return None
