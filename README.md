# Student Performance Prediction

A Streamlit app for predicting student grade class using a trained Gaussian Naive Bayes model.

## Files

- `app.py` - Streamlit UI and prediction app
- `gaussian.pkl` - trained GaussianNB model
- `scaler_.pkl` - fitted StandardScaler
- `studentsperformance.ipynb` - notebook used for exploration and training
- `requirements.txt` - Python dependencies

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

- Windows PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Windows CMD:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

## Notes

- The model expects numeric feature values matching the training data.
- `ParentalEducation` and `ParentalSupport` use categories `0..4`.
- `tutoring`, `extra`, `sports`, `music`, and `volunteer` are binary `0/1` features.
