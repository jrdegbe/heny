Step 2: Set Up the Python Environment
To begin, set up your Python environment by installing the necessary libraries. Open your command line or terminal and execute the following commands:

- pip install pandas numpy scikit-learn fastapi streamlit
- pip install python-dotenv

Run the requirements.txt. 
This file will help you manage the dependencies and ensure that the required libraries are installed correctly by running;
- pip install -r requirements.txt in your command line or terminal.

Step 3: Fetch Restaurant Data from Yelp API
Create a Python script, let's call it fetch_restaurant_data.py, to fetch restaurant data from the Yelp Fusion API. Here's an example code snippet using the requests library:
Remember to replace "YELP_API_KEY" with your actual Yelp API key. The fetch_restaurant_data function takes a location parameter and retrieves a list of restaurants for that location.


Step 7: Run the Application
To run the application, open two separate command line or terminal windows. 
In the first window, navigate to the directory containing app.py and run the following command to start the FastAPI server:

- uvicorn app:app --reload


In the second window, navigate to the directory containing streamlit_app.py and run the following command to start the Streamlit app:

- streamlit run streamlit_app.py
