import dlt
import duckdb
from nba_api.stats.static import teams

""" 
@dlt.resource(write_disposition="replace")
def nba_teams():
    teams_list = teams.get_teams()
    yield from teams_list

# Set pipeline name, destination, and dataset name
pl = dlt.pipeline(destination="duckdb")

# Run the pipeline with data and table name
load_info = pl.run(nba_teams)
print(load_info)

pl.dataset().nba_teams.df()
 """
conn = duckdb.connect(f"dlt_dlt_ingestion.duckdb") 
conn.sql(f"SET search_path = 'dlt_dlt_ingestion'")
print(conn.sql("DESCRIBE").df())
