import pandas as pd
import pytest

from src.model_pipeline import load_data, train_models


def test_load_data_requires_label_column(tmp_path):
    test_file = tmp_path / "missing_label.csv"
    pd.DataFrame({"feature_1": [1, 2], "feature_2": [3, 4]}).to_csv(
        test_file, index=False
    )

    with pytest.raises(ValueError, match="Required label column"):
        load_data(test_file)


def test_load_data_rejects_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    pd.DataFrame(columns=["feature_1", "label"]).to_csv(test_file, index=False)

    with pytest.raises(ValueError, match="Input dataset is empty"):
        load_data(test_file)


def test_train_models_returns_metrics():
    data = pd.DataFrame(
        {
            "feature_1": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            "feature_2": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            "feature_3": [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
            "label": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        }
    )

    results = train_models(data, n_components=2, test_size=0.25)

    assert set(results) == {
        "Random Forest",
        "Support Vector Machine",
        "XGBoost",
    }
    for metrics in results.values():
        assert 0.0 <= metrics["auc"] <= 1.0
        assert 0.0 <= metrics["accuracy"] <= 1.0
        assert "classification_report" in metrics
