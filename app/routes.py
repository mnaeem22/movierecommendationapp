from flask import Blueprint, render_template, request, current_app
from .services import TMDBService

bp = Blueprint('main', __name__)
tmdb_service = None

@bp.before_app_request
def create_tmdb_service():
    global tmdb_service
    api_key = current_app.config.get('TMDB_API_KEY')
    if not api_key:
        raise RuntimeError("TMDB_API_KEY is missing in the configuration.")
    tmdb_service = TMDBService(api_key)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_title = request.form.get('movie_title')
        movies = bp.tmdb_service.search_movie(movie_title)  # Use service from blueprint
        return render_template('index.html', movies=movies)
    return render_template('index.html')

@bp.route('/recommendations/<int:movie_id>')
def recommendations(movie_id):
    recommendations = bp.tmdb_service.get_movie_recommendations(movie_id)
    return render_template('recommendations.html', recommendations=recommendations)
