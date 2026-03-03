import pandas as pd
from sqlalchemy import create_engine
import os

def load_to_warehouse(**kwargs):
    engine = create_engine(os.getenv("WAREHOUSE_DB_URL", "postgresql://localhost/flowforge_analytics"))
    df = pd.read_parquet("/tmp/workflow_metrics.parquet")
    df.to_sql("workflow_metrics", engine, if_exists="append", index=False)
    return len(df)
