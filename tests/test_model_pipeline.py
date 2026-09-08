import numpy as np
import pandas as pd
import pytest

from src.model_pipeline import load_data, train_models


def make_demo_data():
    return pd.DataFrame(
        {
            "feature_1": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            "feature_2": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            "feature_3": [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
            "label": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        }
    )


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


def test_load_data_rejects_missing_features(tmp_path):
    test_file = tmp_path / "missing.csv"
    data = make_demo_data()
    data.loc[0, "feature_1"] = np.nan
    data.to_csv(test_file, index=False)

    with pytest.raises(ValueError, match="missing values"):
        load_data(test_file)


def test_load_data_rejects_non_numeric_features(tmp_path):
    test_file = tmp_path / "text_feature.csv"
    data = make_demo_data()
    data["feature_1"] = ["a"] * len(data)
    data.to_csv(test_file, index=False)

    with pytest.raises(ValueError, match="must be numeric"):
        load_data(test_file)


def test_train_models_rejects_non_binary_labels():
    data = make_demo_data()
    data.loc[0, "label"] = 2

    with pytest.raises(ValueError, match="binary labels"):
        train_models(data)


def test_train_models_rejects_too_many_cv_splits():
    with pytest.raises(ValueError, match="smallest class size"):
        train_models(make_demo_data(), cv_splits=7)


def test_train_models_returns_holdout_and_cv_metrics():
    results = train_models(
        make_demo_data(),
        n_components=2,
        test_size=0.25,
        cv_splits=3,
        cv_repeats=2,
    )

    assert set(results) == {
        "Random Forest",
        "Support Vector Machine",
        "XGBoost",
    }
    for metrics in results.values():
        assert 0.0 <= metrics["auc"] <= 1.0
        assert 0.0 <= metrics["accuracy"] <= 1.0
        assert 0.0 <= metrics["cv_auc_mean"] <= 1.0
        assert metrics["cv_auc_std"] >= 0.0
        assert 0.0 <= metrics["cv_accuracy_mean"] <= 1.0
        assert metrics["cv_accuracy_std"] >= 0.0
        assert metrics["cv_folds"] == 6
        assert "classification_report" in metrics
