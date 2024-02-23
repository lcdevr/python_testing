import pandas as pd
import csv
import selectolax

class FootballDataCsv:
    '''
    
    '''
    
    def __init__(self, filename, league):
        self.filename = filename
        self.league = league
    
    #creates dataframe from
    def __create_dataframe(self):
        df = pd.read_csv(self.filename)
        return df
    
    def append_team_dim(self):
        df = self.create_dataframe()
        teams = pd.unique(df[['HomeTeam', 'AwayTeam']].values.ravel('K'))
        return teams
    
    def open_model_file(self, model):
        modelfiles = {
            'leagues' : r'data\fbdata\model\leagues.csv',
            'teams' : r'data\fbdata\model\teams.csv'
        }
        model_df = pd.read_csv(modelfiles[model], encoding='utf-8')
        print(model_df)
    



#def main():
#    league = 'E0'
#    test = FootballDataCsv(rf'data\fbdata\raw\{league}.csv', league)
#    test.open_model_file('leagues')

def main():
    pass
    
    
if __name__ == '__main__':
    main()