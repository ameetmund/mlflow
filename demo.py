import os
import mlflow


def evaluate_metric(param1, param2):
    metric = param1**2 + param2**2
    return metric


def main(p1, p2):
    with mlflow.start_run():
        mlflow.log_param("param1", p1)
        mlflow.log_param("param2", p2)

        metric = evaluate_metric(param1=p1, param2=p2)
        mlflow.log_metric("someMetric", metric)


if __name__ == "__main__":
    main(6, 10)
