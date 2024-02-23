import pandas as pd
import requests
import selectolax
import bs4
from dataclasses import dataclass

@dataclass
class Match:
    Div : str
    Date : str
    Time : str
    HomeTeam : str
    AwayTeam : str
    FTHG : int
    FTAG : int
    HTHG : int
    HTAG : int
    Referee : str
    HS : int
    AS : int
    HST : int
    AST : int
    HF : int
    AF : int
    HC : int
    AC : int
    HY : int
    AY : int
    HR : int
    AR : int