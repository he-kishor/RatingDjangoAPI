# 🎬 Movie Rating API 
### Welcome to the Movie Rating API developed with Django! This API allows users to rate movies and manage their ratings seamlessly. Here's an overview of what this API offers:

## ✨ Features
User Tokenization: Utilizes Django's default User model for authentication and tokenization.
CRUD Operations: Users can perform Create, Read, Update, and Delete operations on their ratings.
Personalized Ratings: Each user can view and manage their movie ratings.
Predefined Movie Data: The movie database comes with a set of predefined movies for users to rate.

## 🚀 Getting Started
To get started with the Movie Rating API, follow the steps below:

Clone the repository:


## 🔐 Authentication
This API uses token-based authentication. Users must obtain a token by logging in with their credentials. The token must be included in the header of all requests that require authentication.

## 📚 Endpoints
Here are the main endpoints provided by the Movie Rating API:

Register User: /api/register/ - Create a new user account.
Login User: /api/login/ - Obtain an authentication token.
Rate a Movie: /api/rate/ - Create or update a movie rating.
View Ratings: /api/ratings/ - View all your movie ratings.
Movie List: /api/movies/ - View the list of predefined movies.

## 🛠️ Usage
### Register a new user
```
POST /api/register/
{
  "username": "your_username",
  "password": "your_password"
}
```
### Login and obtain a token
```
POST /api/login/
{
  "username": "your_username",
  "password": "your_password"
}
```
### Rate a movie

```
POST /api/rate/
Headers: { "Authorization": "Token your_token" }
{
  "movie_id": "movie_id",
  "rating": 5
}
```
### View all your ratings
```
GET /api/ratings/
Headers: { "Authorization": "Token your_token" }
```

## 🧑‍💻 Contributing
Feel free to open issues or submit pull requests if you find any bugs or want to contribute to the project.

### Enjoy using the Movie Rating API! 🍿🎥
