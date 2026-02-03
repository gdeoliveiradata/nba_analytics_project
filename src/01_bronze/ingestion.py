import dlt
import time
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo


@dlt.source
def nba_data():

    @dlt.resource(primary_key="id", write_disposition="merge")
    def nba_teams():
        teams_list = teams.get_teams()
        yield from teams_list

    @dlt.resource(primary_key="id", write_disposition="merge")
    def nba_active_players():
        players_list = players.get_active_players()
        yield from players_list

    @dlt.transformer(data_from=nba_active_players)
    def nba_player_headline_stats(player):
        player_id = player["id"]
        time.sleep(0.6)
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()["PlayerHeadlineStats"]
        yield player_info

    return nba_teams, nba_active_players, nba_player_headline_stats

# Set pipeline name, destination, and dataset name
pl = dlt.pipeline(destination="duckdb", dataset_name="nba_dataset")

# Run the pipeline with data and table name
load_info = pl.run(nba_data())
print(load_info)
