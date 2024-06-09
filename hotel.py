import streamlit as st
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# Download necessary NLTK datasets
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
data_path = 'C:\\Users\\LENOVO\\Downloads\\Hotel_Reviews.csv'  # Update this path to your dataset location
data = pd.read_csv(data_path)

# Prepare the data
data['Hotel_Address'] = data['Hotel_Address'].str.replace("United Kingdom", "UK")
data["countries"] = data['Hotel_Address'].apply(lambda x: x.split(' ')[-1].lower())
data['Tags'] = data['Tags'].str.lower()
data = data.drop(['Additional_Number_of_Scoring', 'Review_Date', 'Reviewer_Nationality',
                  'Negative_Review', 'Review_Total_Negative_Word_Counts',
                  'Total_Number_of_Reviews', 'Positive_Review',
                  'Review_Total_Positive_Word_Counts',
                  'Total_Number_of_Reviews_Reviewer_Has_Given', 'Reviewer_Score',
                  'days_since_review', 'lat', 'lng'], axis=1)


# Recommendation function
def recommend_hotel2(location, description):
    # Convert the description to lowercase and tokenize
    description = description.lower()
    tokens = word_tokenize(description)

    # Load stop words and initialize lemmatizer
    stop_words = set(stopwords.words('english'))
    lemm = WordNetLemmatizer()

    # Remove stop words and lemmatize the description tokens
    filtered_tokens = {lemm.lemmatize(word) for word in tokens if word not in stop_words}

    # Filter the dataset by the specified location
    country_hotels = data[data['countries'] == location.lower()]
    country_hotels = country_hotels.reset_index(drop=True)

    # Calculate similarity for each hotel
    similarities = []
    for i, row in country_hotels.iterrows():
        hotel_tags = word_tokenize(row['Tags'])
        hotel_tokens = {lemm.lemmatize(word) for word in hotel_tags if word not in stop_words}
        similarity = len(hotel_tokens & filtered_tokens)
        similarities.append(similarity)

    # Add similarity scores to the dataframe
    country_hotels['similarity'] = similarities

    # Sort hotels by similarity and remove duplicates
    country_hotels = country_hotels.sort_values(by='similarity', ascending=False)
    country_hotels = country_hotels.drop_duplicates(subset='Hotel_Name', keep='first')

    # Sort hotels by average score
    country_hotels = country_hotels.sort_values(by='Average_Score', ascending=False).reset_index(drop=True)

    # Add a ranking column starting from 1
    country_hotels.insert(0, 'Rank', range(1, len(country_hotels) + 1))

    # Return top 10 recommendations
    return country_hotels[['Rank', 'Hotel_Name', 'Average_Score', 'Hotel_Address']].head(10)


# Streamlit user interface
st.title("Hotel Recommendation System")
st.write("Find the best hotel for your needs!")

# Initialize session state variables for the input fields
if 'location' not in st.session_state:
    st.session_state['location'] = ''
if 'description' not in st.session_state:
    st.session_state['description'] = ''

# User input
location = st.text_input("Enter the location (eg: Italy, UK,Spain):", st.session_state['location'])
description = st.text_area("Enter a brief description of your trip (e.g., I am going on a business trip):",
                           st.session_state['description'])

# Button to get recommendations
if st.button("Get Recommendations"):
    if location and description:
        # Update session state with current inputs
        st.session_state['location'] = location
        st.session_state['description'] = description

        st.write("Finding the best hotels for you...")
        recommendations = recommend_hotel2(location, description)

        st.write("Top 10 hotel recommendations:")
        st.table(recommendations)

        # Hide the available countries section when recommendations are displayed
        st.session_state['show_countries'] = False
    else:
        st.write("Please provide both location and description to get recommendations.")
else:
    # Show available countries when recommendations are not displayed
    st.session_state['show_countries'] = True

# Display available countries only if recommendations are not shown
if st.session_state['show_countries']:
    countries = [country.capitalize() for country in data['countries'].unique()]
    st.write("Available countries in the dataset:")
    st.write(countries)

# Button to reset the application
if st.button("Reset"):
    # Clear session state variables and reset the app
    st.session_state['location'] = " "
    st.session_state['description'] = " "
    st.session_state['show_countries'] = True
    st.experimental_rerun()
