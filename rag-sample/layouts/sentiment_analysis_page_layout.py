# Page styling with gradient and modern design
# The following CSS styles are for the sentiment analysis page
# They include gradient backgrounds, modern input and button styles, and sentiment result styling


# Function to initialize sentiment page styles
def initialize_sentiment_page_styles() -> str:
    return """
    <style>
    html, body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
        background: rgba(255, 255, 255, 0.97);
        border-radius: 24px;
        margin: 2rem auto;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    div[data-testid="stHeader"] {
        color: #667eea !important;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin-bottom: 0.5rem !important;
    }
    div[data-testid="stSubheader"] {
        color: #764ba2 !important;
        font-size: 1.2rem !important;
        text-align: center !important;
        margin-bottom: 2.5rem !important;
    }
    .stTextInput > label {
        color: #0f1419 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
    .stTextInput > div > div > input {
        border: 2px solid #667eea !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 12px 24px !important;
        border: none !important;
        border-radius: 10px !important;
        cursor: pointer !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4) !important;
    }
    .sentiment-positive {
        background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.2);
    }
    .sentiment-negative {
        background: linear-gradient(135deg, #f87171 0%, #dc2626 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(220, 38, 38, 0.2);
    }
    .sentiment-label {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .confidence-score {
        font-size: 2rem;
        font-weight: 900;
        margin-top: 10px;
    }
    .confidence-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-top: 5px;
    }
    .input-example {
        background: #f3f4f6;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 0.9rem;
        color: #666;
        border-left: 4px solid #667eea;
    }
    </style>
    """


# Function to style the example div for sentiment analysis page
def sentiment_analysis_example_div_styles() -> str:
    return """
    <div class="input-example">💡
    <strong>Tip:</strong> 
    Enter any comment, sentence, or text to analyze its sentiment and confidence score.
    </div>
    """


# positive sentiment layout template variable
# This variable holds the HTML layout for displaying positive sentiment results
def positive_sentiment_layout(score) -> str:
    return (
        f'<div class="sentiment-positive">'
        f'<div class="sentiment-label">✨ POSITIVE SENTIMENT</div>'
        f'<div class="confidence-label">Your text expresses positive emotion</div>'
        f'<div class="confidence-score">{score*100:.2f}%</div>'
        f'<div class="confidence-label">Confidence Score</div>'
        f"</div>"
    )


# negative sentiment layout template variable
# This variable holds the HTML layout for displaying negative sentiment results
def negative_sentiment_layout(score) -> str:
    return (
        f'<div class="sentiment-negative">'
        f'<div class="sentiment-label">⚠️ NEGATIVE SENTIMENT</div>'
        f'<div class="confidence-label">Your text expresses negative emotion</div>'
        f'<div class="confidence-score">{score*100:.2f}%</div>'
        f'<div class="confidence-label">Confidence Score</div>'
        f"</div>"
    )
