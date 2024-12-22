import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import roc_auc_score, classification_report
import joblib

# Load enhanced data
file_path = r'C:\Users\Swapnil\Desktop\Peer_to_peer\enhanced_dummy_mentor_ranking_data.csv'
data = pd.read_csv(file_path)

# Select features and target
features = [
    'mentee_skill_level', 'mentor_skill_level', 'teaching_style_match',
    'mentor_rating', 'engagement_score', 'availability_overlap', 'match_score'
]
X = data[features]
y = data['selected']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LightGBM model with optimal parameters
params = {
    'num_leaves': 64,
    'learning_rate': 0.05,
    'n_estimators': 300,
    'min_child_samples': 30,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'reg_alpha': 0.1,
    'reg_lambda': 0.1
}
model = LGBMClassifier(**params, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC Score: {roc_auc:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Cross-validation
cv_scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
print(f"Average Cross-Validation ROC-AUC: {cv_scores.mean():.4f}")

# Save the trained model to a file
model_file_path = "lightgbm_model.pkl"
joblib.dump(model, model_file_path)
print(f"Model saved at {model_file_path}")