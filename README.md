# 🌾 AgriCrop – Smart Crop Recommendation System

🔗 **Live Demo:** https://agricrop.onrender.com

A simple machine learning web app that recommends the most suitable crop based on soil nutrients and pH.

## Features
- Predicts the best crop from Nitrogen (N), Phosphorus (P), Potassium (K), and soil pH
- Shows the model's confidence (%) for each prediction
- Clean, responsive web interface
- Lightweight Flask backend

## Tech Stack
| Layer | Technology |
|-------|-----------|
| ML Model | Scikit-learn (Random Forest Classifier) |
| Backend | Flask (Python) |
| Frontend | HTML, CSS |
| Model Storage | Joblib |

## Project Structure
```
AgriCrop/
├── templates/
│   └── index.html        # Frontend form and result display
├── app.py                # Flask server
├── train_model.py        # Creates dataset, trains and saves the model
├── requirements.txt      # Python dependencies
└── README.md
```

## How It Works
1. `train_model.py` generates a synthetic dataset, trains a Random Forest, and saves it as `crop_model.pkl`.
2. `app.py` loads the saved model once when the server starts.
3. The user enters N, P, K, and pH in the form.
4. The form sends a POST request to `/predict`, which converts the inputs to numbers and runs the model.
5. The recommended crop and confidence are shown on the same page.

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AgriCrop.git
cd AgriCrop
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python train_model.py
```

### 5. Run the app
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser.

## Sample Input
| N | P | K | pH | Expected Crop |
|---|---|---|----|---------------|
| 80 | 45 | 40 | 5.8 | Rice |
| 25 | 65 | 30 | 6.5 | Groundnut |
| 120 | 45 | 20 | 7.0 | Cotton |

## Limitations
- The dataset is synthetic, so this is a proof of concept, not a real agronomic tool.
- Only four soil features are used; real recommendations also depend on climate and rainfall.

## Future Improvements
- Train on a real dataset (Kaggle Crop Recommendation)
- Add temperature, humidity, and rainfall as inputs
- Add input range validation
- Deploy online (Render or similar)

## Author
**C Venkateswari** – [GitHub](https://github.com/<venkateswarichatrapathi>)