import dlt
from nba_api.stats.static import teams

@dlt.source
def nba_data():

    @dlt.resource()
    def nba_teams():
        teams_list = teams.get_teams()
        yield from teams_list

    return nba_teams

# Set pipeline name, destination, and dataset name
pl = dlt.pipeline(destination="duckdb")

# Run the pipeline with data and table name
load_info = pl.run(nba_data, write_disposition="replace")
print(load_info)
