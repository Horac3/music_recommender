# Update the Flask app code

from flask import Flask, render_template, request
import random

app = Flask(__name__)

class MusicRecommender:
    def __init__(self):
        self.music_database = {
            'Pop': ['Song1', 'Song2', 'Song3'],
            'Rock': ['Song4', 'Song5', 'Song6'],
            'Hip Hop': ['Song7', 'Song8', 'Song9']
        }
        self.user_feedback = {}

    def recommend_music(self, selected_genre):
        genre_songs = self.music_database[selected_genre]

        # Filter out songs the user has already provided feedback on
        available_songs = [song for song in genre_songs if song not in self.user_feedback.get(request.remote_addr, [])]

        if not available_songs:
            print("You've provided feedback on all available songs in this genre. Recommending a random song.")
            recommended_song = random.choice(genre_songs)
        else:
            recommended_song = random.choice(available_songs)

        return recommended_song

    def record_feedback(self, selected_genre, feedback):
        self.user_feedback.setdefault(request.remote_addr, []).append(selected_genre)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genre = request.form['genre']
    feedback = request.form['feedback']

    music_recommender.record_feedback(selected_genre, feedback)
    recommended_song = music_recommender.recommend_music(selected_genre)

    return render_template('recommendation.html', recommended_song=recommended_song)

if __name__ == '__main__':
    music_recommender = MusicRecommender()
    app.run(debug=True)
