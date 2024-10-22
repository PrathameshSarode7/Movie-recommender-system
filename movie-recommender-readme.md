# Movie Recommender System

A sophisticated web application built with Streamlit that recommends movies based on user selection using content-based filtering and The Movie Database (TMDB) API.
!IMPORTANT!!!!! Basically setup streamlit and api
## 🎬 Features

- Interactive movie selection from a comprehensive database
- Content-based movie recommendations
- Real-time movie poster fetching from TMDB
- Stylish user interface with customized background
- Responsive grid layout for movie recommendations
- Hover effects on movie posters
- Loading spinner during recommendation processing

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn (for cosine similarity)
- TMDB API
- Pickle (for model persistence)
- Requests (for API calls)
- Base64 (for background image encoding)

## 📋 Prerequisites

Before running this application, make sure you have the following:

- Python 3.x installed
- TMDB API key
- Required Python packages installed
- Pre-trained model files (`movies_tmdb.pkl` and `cosine_sim.pkl`)
- Background image file (`arrangement-cinema-elements-red-background-with-copy-space.jpg`)

## 🔧 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd movie-recommender-system
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your TMDB API key in the code or as an environment variable

## 🚀 Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Select a movie from the dropdown menu

4. Click the "Recommend" button to get similar movie recommendations

## 💾 Data Files

The system requires two pickle files:
- `movies_tmdb.pkl`: Contains the movie database with features
- `cosine_sim.pkl`: Contains the pre-computed cosine similarity matrix

## 🎨 Customization

You can customize the application by:
- Modifying the CSS styles in the `add_bg_from_local` function
- Changing the background image
- Adjusting the number of recommendations displayed
- Modifying the layout configuration

## 📝 Notes

- The application uses TMDB's API to fetch movie posters
- A placeholder image is displayed if a movie poster is unavailable
- The recommendations are displayed in a grid layout with a maximum of 5 movies per row
- The system uses cosine similarity for content-based filtering

## 🔑 API Key

To use this application, you need to:
1. Sign up for a TMDB account
2. Get your API key from [TMDB website](https://www.themoviedb.org/settings/api)
3. Replace the API key in the code or set it as an environment variable

## 📈 Future Improvements

- Add user authentication
- Implement collaborative filtering
- Add movie details on hover
- Include movie ratings and reviews
- Add search functionality with autocomplete
- Implement genre-based filtering

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
