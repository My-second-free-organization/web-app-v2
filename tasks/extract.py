import pandas as pd
from sqlalchemy import create_engine
import os

def extract_workflow_data(**kwargs):
    engine = create_engine(os.getenv("SOURCE_DB_URL", "postgresql://localhost/flowforge"))
    df = pd.read_sql("SELECT * FROM workflow_instances WHERE completed_at > NOW() - INTERVAL '1 hour'", engine)
    df.to_parquet("/tmp/workflow_data.parquet")
    return len(df)
