# Hotel Recommendation System

This project implements a hotel recommendation system using Streamlit, a Python library for building interactive web applications. The recommendation system analyzes hotel descriptions and suggests the most relevant hotels based on user input.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/NANITH777/Hotel_Recommendation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hotel-recommendation-system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run hotel.py
    ```

2. Access the application in your web browser at [http://localhost:8502](http://localhost:8502).

3. Enter the location (e.g., Italy, UK, Netherlands) and a brief description of your trip (e.g., "I am going on a business trip").

4. Click the "Get Recommendations" button to view hotel recommendations based on your input.

5. To reset the input fields and recommendations, click the "Reset" button.

## Files

- `hotel.py`: Python script containing the Streamlit application code.
- `Hotel_Reviews.csv`: Dataset containing hotel reviews data.
- `README.md`: Documentation file providing instructions and information about the project.
- `Requirements.txt`: Requirements

## Libraries Used

- `nltk`: Natural Language Toolkit for text processing tasks such as tokenization and lemmatization.
- `pandas`: Data manipulation and analysis library for working with tabular data.
- `numpy`: Numerical computing library for handling arrays and mathematical operations.
- `streamlit`: Web application framework for creating interactive data apps.

## Functionality

- The application preprocesses hotel descriptions and calculates similarity scores based on user input.
- It recommends the top 10 hotels with the highest similarity scores and average ratings.
- Users can reset the input fields to start a new search.

  # Interface with Streamlit

<img width="381" alt="reset" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/01df39e4-2cdb-4d20-aac8-4d8527383468">
<img width="404" alt="rec_result" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/e114229c-0101-4bdc-ae8d-0e5ec2d273ae">
<img width="368" alt="Recommendation" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/bb30edff-9ca6-412d-974a-f327df96246e">
<img width="361" alt="Result" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/e9998ea8-fa23-4e9b-9868-a2e2a1124e5e">
<img width="379" alt="Hotel_findingR" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/4920c082-9c40-4b9e-a257-99358000ac4b">
<img width="391" alt="Hotel_IT_1" src="https://github.com/NANITH777/Hotel_Recommendation/assets/109669139/d1cc2b04-6b64-4a7e-a00e-975bbe780ccc">
