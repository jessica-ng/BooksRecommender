Instructions to run:

	Running the server:
		1. Navigate to the /server directory
		2. Install any required python modules using pip. flask, flask_cors, numpy, pandas, csv, scipy
		3. Run "python app.py" on the command line
		4. Now you have the python flask backend running. (When the backend is restarted some data is reset, e.g. login details)

	Running the front-end:
		1. Navigate to the /client directory
		2. Run "npm install" on the command line to install all essential packages
		3. Run "npm run serve" on the command line to start the front-end
		4. Using a web browser navigate to "http://localhost:8080/" to visit the recommendation system.
		5. You can sign up or login to a test account using "username : 1000" and "password : password".

Description of the recommendation system:
	User-flow:
		1. Sign up using the sign up tab or login using test account (username=1000, password=password)
		2. For the sign up option, you will be led to onboarding where you can enter some ratings to start creating 
		   recommendations based on the ratings. Or you can enter some ratings on your profile instead. But you must have 
		   submitted some ratings for there to be recommendations.
		3. You can see the recommendations on the "Recommendations" tab after you have signed in/ up.
	
	Dynamic user profile:
		1. The user can update their past ratings and submit new ratings, which will have an effect on their recommendations.

	Dataset:
		1. There are 3 csv files containing 10000 books and over 16000 ratings
		   which are loaded into the backend and merged depending on what data is required.
		2. Ratings are submitted directly to the new_ratings2.csv file, and can also be updated.
		3. "book_genres.csv" contains data of genres of each book in the dataset.

	Recommendation Algorithm:
		1. It is using matrix factorisation where all ratings in the dataset are used to generate a user's 
		   recommendations. On top of that the user's most rated genres are used to further filter out better recommendations.

