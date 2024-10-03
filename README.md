# Movie Recommendation System (Content-Based Filtering)

### Using Cosine Similarity
- Recommendation systems are taking over the world as so many websites and applications are using them as their fundamentals, some of which include famous companies like Amazon, Netflix, Youtube etc.
- One approach for recommendations systems is content based filtering, which is a method that predicts based on what you watch. Therefore it is basically a content-based filtering.
- For example lets say A watches a movie and he liked it. Now we will recommend another such movie to A.
- This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations.
  
### Machine Learning Model
1. **Cosine Similarity** is a metric, helpful in determining, how similar the data objects are irrespective of their size.
    - In cosine similarity, data objects in a dataset are treated as a vector.
    - The cosine similarity is beneficial because even if the two similar data objects are far apart by the Euclidean distance because of the size, they could still have a smaller angle between them. Smaller the angle, higher the similarity.
  
### Dataset Link 
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

### TMDB API Link
https://developer.themoviedb.org/reference/intro/getting-started

### Data Preprocessing
- All the data cleaning, preprocessing, model building, deploying etc. has been explained in the Jupyter Notebook uploaded above.

### How to Run Locally
1. Create a folder x and put all the below mentioned files in it.
    - Movie_recommender_main.py
    - top_movies.pkl
    - create another folder with the name *pages* and put all the below mentioned files in it.
        - Movie_recommender.py
        - Movie_recommender_genre.py
        - cosine_output.pkl
        - recommend_movies.pkl
        - top_movies.pkl

2. Run the *Movie_recommender_main.py* file on spyder and open anaconda prompt.
3. Type ```streamlit run 'c:\users\admin\jupyter notebooks\projects\Movie_recom\Movie_recommender_main.py'``` on the anaconda shell to host locally

### Outputs
### 1. Top Movies Based on Rating
**Note that we're getting top books based on rating using the weighted average formula.**

![image](https://github.com/user-attachments/assets/8c100b73-896f-45c9-bcf1-5709d999e587)
![image](https://github.com/user-attachments/assets/fa7b55e0-54d3-43e9-ae86-b5c8cdc3dcb0)


### 2. Movie Recommender on Similarity
![image](https://github.com/user-attachments/assets/0a1008a9-02f8-4637-a1d2-7b3684a4fb44)


### 3. Movie Suggester on Genre
![image](https://github.com/user-attachments/assets/9669b901-16a6-482c-989a-6caa53618a23)

  
