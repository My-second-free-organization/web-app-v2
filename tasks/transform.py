import pandas as pd

def transform_metrics(**kwargs):
    df = pd.read_parquet("/tmp/workflow_data.parquet")
    metrics = df.groupby("workflow_id").agg(total_executions=("id", "count"), avg_duration=("duration_seconds", "mean"), error_count=("status", lambda x: (x == "FAILED").sum())).reset_index()
    metrics.to_parquet("/tmp/workflow_metrics.parquet")
    return len(metrics)
