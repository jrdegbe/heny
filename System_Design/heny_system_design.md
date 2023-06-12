Heny is a tourist recommender and geographical app which is used to  

- Recommender making — swipe left or right based on the user preferences and profile compatibility
- Engage with other site seeing — like/share other places pics
- Message other sites seeing places contacts person
- Discover other places based on the proximity and location
- Search other places on Heny and their profile
- Priority Likes
- Users are mobile based ( Heny app).

Designing Heny would involve —

- Defining the target audience: Determine the demographic of users you want to target with the app.

- Wireframing and prototyping: Create a visual representation of how the app will function and look.

- Developing the backend: Build the server-side infrastructure that will support the app’s functionality, such as user authentication, Recommender, and messaging.

- Designing the user interface: Create a visually appealing and user-friendly interface that is easy to navigate.

- Testing and debugging: Test the app on various devices and fix any bugs or issues that arise.

- Launching and marketing: Release the app on the app store and promote it through various channels, such as social media and online advertising.

- Continuously improve: Continuously monitor the app’s performance, gather feedback from users and make updates to improve the app.

Functionality —

- Swipe — right : If you like a place profile, then swipe right.

- Swipe left : If you don’t like a place profile, then swipe left.

Recommender : If you the user profiles Recommendes the place swipes right then its a recommender.

Users can send messages to their places of attractions.

Important Features

For this app, we will take below features —

- Create a profile and get recommendation based on the profile details and location radius

Recommender mechanism

- Send messages if both the user and the place follow each other

Scaling Requirements

Let’s say we have —

No of active users per day ( DAU ) : 1,400

No of pic per user : 5

Size of each pic : 2 MB

Total storage estimate for users per day : 20 GB

Total storage estimate for users for next 2 years : 1 TB

Percentage of users of total active users who get Recommender : 0.2% so that would be 100 users daily.

- Assuming that the average Heny user opens the app 5 times per day and spends 3 minutes per session, this means that the app must be able to handle () minutes of usage per day.

- If each user generates 0.5 MB of data per session, this means that the app must be able to handle 7.5 TB of data per day.

- Assuming a user generates 1 Recommender per day and sends 5 messages, this means that the app must be able to handle () Recommenders and () messages per day.

- Assuming the app must be able to handle a peak load of 10 times the average usage, this means that the infrastructure must be able to handle () minutes of usage,  () of data, and () Recommenders and () messages.

Data Model — ER requirements
User

userid : Int

username : String

password: String

age : Int

gender : String

description : string

Location : String ( Can be Int if taken in latitude and longitude)

preference : String

status : String

Recommender_status : String

Rating : String

Functionality —

- User can create profile and put max 6 pics
- User can swipe left or right based on the profile compatibility
- User can get Recommender and also rate/review other places
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Recommender

Recommender_id: Int

Recommender_id : Int

Recommender_id : Int

Functionality —

If the user 1 Recommenders with user 2 then store the Recommender results.
Recommended user can follow/message/unRecommender places
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Image

userid: Int

image_id : Int

url : String

Functionality —

Users can store upto 5 images

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Session

userid : Int

connectid: Int

Each user session information needs to be stored to show status ( active/offline/away).



High Level Design
- Assumptions/Considerations/Requirements —

- System can store the details when a Recommender occurs
- The system is going to be read heavy
- The system should be highly available and reliable
- System should allow direct messaging between the user and the Recommender  if they feel recommended
- App administrators can remove/ban the user
- The no of swipes should be limited by a count in a given period of time.
- Images can stored in Blob or as a file in the file systems.
- Data will be horizontally partitioned based on the user geolocation.
- For the connection protocol, XMPP protocol will be used.


Components
- Clients : Users
- API gateway
- Loadbalancers
- Storage ( s3) and replicas
- CDN
- Cache
- Database and replicas
- Recommender


Services

- API Gateway Service : To take the user request, validates and navigates it to the respective service

- Profile Service: To let users create new account, login and enter/add/update their details and upload pics.

- Session Service: To keep a tap on the user sessions/connection information

Recommendation Service : To recommend a collection of profile that Recommendes user preferences, location and engagements

Recommender Service: To keep a tap on the recommended users information

Implementation of an API Gateway Service, Profile Service, Session Service, Recommendation Service, and Recommender Service in Python using the Flask web framework.



In this implementation, the Recommender Service stores a dictionary of Recommendes, where the key is the Recommend_id and the value is a tuple of user1_id and user2_id. 

The API Gateway Service allows users to add a Recommend by sending a POST request to /Recommend with user1_id and user2_id in the request body, and retrieve Recommend details by sending a GET request to /Recommend/<Recommend_id>.




In this API Design implementation, we have three endpoints:

/users/<int:user_id> (GET): This endpoint is used to get user information. The user_id is passed as a parameter in the URL.
/like (POST): This endpoint is used to like a user. The user_id is passed in the request body as JSON.
/dislike (POST): This endpoint is used to dislike a user. The user_id is passed in the request body as JSON.
We need to have API for —

Profile service — login, signup

Session Service — to get connection information

Recommender Service — to get Recommend details

Recommendation — to return a collection of recommendations.


In this code, the ProfileService class handles user signup and login. The signup method stores the username and a hashed version of the password in a dictionary. 

The login method checks if the username exists in the dictionary, and if so, it compares the hashed password from the dictionary with the hashed password of the input. 

The SessionService class provides information about active sessions. The get_connection_info method returns information about a specific session, given its session ID.

The RecommenderService class provides information about Recommendes. The get_Recommend_details method returns information about a specific Recommend, given its Recommend ID.

The RecommendationService class provides recommendations to the users. The get_recommendations method returns a collection of recommendations based on the user's preferences.