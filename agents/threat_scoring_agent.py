import numpy as np
from sklearn.linear_model import LogisticRegression

class ThreatScoringAgent:
    def __init__(self):
        # Fake training data (features: [reputation, severity, frequency])
        X_train = np.array([
            [0.1, 0.2, 0.1],
            [0.3, 0.4, 0.3],
            [0.7, 0.8, 0.6],
            [0.9, 1.0, 0.9],
        ])
        y_train = ["Low", "Medium", "High", "High"]
        self.model = LogisticRegression(max_iter=200)
        self.model.fit(X_train, y_train)

    def run(self, input_data, context):
        features = np.array([
            input_data.get("reputation", 0),
            input_data.get("severity", 0),
            input_data.get("frequency", 0)
        ]).reshape(1, -1)
        prediction = self.model.predict(features)[0]
        return {"threat_score": prediction, "features": features.tolist()}
