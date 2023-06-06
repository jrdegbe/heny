import streamlit as st

# Sidebar to select user
user_index = st.sidebar.selectbox('Select User', range(num_profiles), index=0)

# Display user profile
st.write('User Profile:')
st.write(df.loc[user_index])

# Get recommendations for the selected user
recommendations = get_recommendations(user_index)

# Display recommendations
st.write('Recommendations:')
for recommendation in recommendations:
    st.write(df.loc[recommendation])
