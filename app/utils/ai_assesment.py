import warnings
import numpy as np
import pandas as pd
import joblib
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


class AiAssesment:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

        self.score_mapping = {"a": 1.25, "b": 1.5, "c": 1.75, "d": 1.0}

        self.learning_paths = [
            "Web Development",
            "Mobile Development",
            "Data & AI",
            "Product & UX",
        ]

    def predict(self, jawaban: dict):
        input_vector = []
        missing = []

        for i in range(1, 16):
            ans = jawaban.get(f"Q{i}")
            if not ans:
                missing.append(i)
            else:
                input_vector.append(self.score_mapping.get(ans.lower(), 0))

        if missing:
            raise ValueError(
                f"Jawaban soal nomor {', '.join(map(str, missing))} belum diisi!"
            )

        input_vector = np.array(input_vector).reshape(1, -1)
        if hasattr(self.model, "feature_names_in_"):
            df_input = pd.DataFrame(input_vector, columns=self.model.feature_names_in_)
        else:
            df_input = pd.DataFrame(input_vector)

        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(df_input)[0]
        else:
            pred = self.model.predict(df_input)[0]
            probs = np.zeros(len(self.learning_paths))
            probs[int(pred)] = 1.0

        top_indices = probs.argsort()[::-1][:3]
        tiga_terbaik = [
            {"path": self.learning_paths[idx], "prob": f"{probs[idx]*100:.2f}%"}
            for idx in top_indices
        ]

        return tiga_terbaik
