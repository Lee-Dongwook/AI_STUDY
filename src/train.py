import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from src.model import SklearnModel

def main():

    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names) # type: ignore
    y = pd.Series(iris.target) # type: ignore

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = SklearnModel()
    model.train(X_train, y_train)

    acc = model.evaluate(X_test, y_test)
    print(f"✅ 모델 정확도: {acc:.2f}")

if __name__ == "__main__":
    main()