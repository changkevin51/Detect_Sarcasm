# Import necessary libraries
import streamlit as st
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to analyze sentiment
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

# Streamlit app setup
st.title("Sentiment Analysis App")
st.write("Enter a sentence or paragraph, and this app will analyze its sentiment.")

# User input
user_input = st.text_area("Enter your text here:")

# Analyze button
if st.button("Analyze"):
    if user_input:
        sentiment_scores = analyze_sentiment(user_input)
        compound = sentiment_scores['compound']
        
        # Interpretation of compound score with image and background color
        st.subheader("Interpretation")
        if compound >= 0.25:
            st.success("The sentiment is **Positive**!")
            img_path = f"positive{random.randint(1, 5)}.jpg"
        elif 0.05 <= compound < 0.25:
            st.info("The sentiment is **Slightly Positive**.")
            img_path = f"positive{random.randint(1, 5)}.jpg"
        elif -0.25 <= compound < -0.05:
            st.warning("The sentiment is **Slightly Negative**.")
            img_path = f"negative{random.randint(1, 5)}.jpg"
        elif compound <= -0.25:
            st.error("The sentiment is **Negative**.")
            img_path = f"negative{random.randint(1, 5)}.jpg"
        else:
            st.warning("The sentiment is **Neutral**.")
            img_path = f"neutral{random.randint(1, 5)}.jpg"

            
        # Display image based on sentiment
        st.image(img_path, use_container_width=True)
        st.write("")
        # Custom slider for compound score
        st.subheader("Compound Score Representation")
        slider_html = f"""
        <div style="width: 100%; background-color: lightgray; padding: 5px; border-radius: 5px; position: relative;">
            <div style="width: 100%; display: flex; justify-content: space-between; font-size: 0.8em; color: #333;">
                <span>Very Negative</span>
                <span>Neutral</span>
                <span>Very Positive</span>
            </div>
            <div style="height: 20px; width: 100%; background-color: lightgray; position: relative; margin-top: 5px; border-radius: 10px;">
                <div style="height: 100%; width: 10px; background-color: #4CAF50; position: absolute; left: {50 + (compound * 50)}%; border-radius: 5px;"></div>
            </div>
        </div>
        """
        st.markdown(slider_html, unsafe_allow_html=True)

        # Display sentiment scores at the bottom
        st.write("")
        st.write("")
        st.subheader("Sentiment Scores")
        st.write(f"**Positive Score**: {sentiment_scores['pos']}")
        st.write(f"**Neutral Score**: {sentiment_scores['neu']}")
        st.write(f"**Negative Score**: {sentiment_scores['neg']}")
        st.write(f"**Compound Score**: {sentiment_scores['compound']}")

    else:
        st.write("Please enter some text to analyze.")


for i in range(5):
    st.write("")
# CSS for footer styling
footer_style = """
<style>
.footer {
    flex-shrink: 0;
    color: #999999;
    text-align: center;
    margin-top: 2em;
    font-size: 0.8em;
}
</style>
"""

# Add footer content
st.markdown(footer_style, unsafe_allow_html=True)
st.markdown('<div class="footer">This app uses VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze sentiments.</div>', unsafe_allow_html=True)
st.write("")
st.markdown('<div class="footer">A project by Kevin Chang</div>', unsafe_allow_html=True)

