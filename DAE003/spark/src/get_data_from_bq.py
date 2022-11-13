from dotenv import load_dotenv
import json
import db_dtypes
from google.cloud import bigquery

load_dotenv()

client = bigquery.Client()

query = """
SELECT districtID 
FROM `dea-proj.dea_proj_data.openrice_restaurants` 
where districtName = "大坑"

"""

query_job = client.query(query)
df = query_job.to_dataframe()
# for row in query_job:
#     print(row.districtID)
print(df.iloc[0].districtID)
