import dlt
from nba_api.stats.static import teams, players


@dlt.source
def nba_data():

    @dlt.resource(primary_key="id", write_disposition="merge")
    def nba_teams():
        teams_list = teams.get_teams()
        yield from teams_list

    @dlt.resource(primary_key="id", write_disposition="merge")
    def nba_players():
        players_list = players.get_players()
        yield from players_list

    return nba_teams, nba_players

# Set pipeline name, destination, and dataset name
pl = dlt.pipeline(destination="duckdb", dataset_name="nba_dataset")

# Run the pipeline with data and table name
load_info = pl.run(nba_data)
print(load_info)
