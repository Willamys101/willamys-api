from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuração CORS para permitir o frontend da Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://willamysbetanalyzer.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exemplo de modelo de entrada
class MatchData(BaseModel):
    home_team_goals: int
    away_team_goals: int
    home_shots: int
    away_shots: int
    home_possession: float
    away_possession: float

# Exemplo de rota para previsão
@app.post("/predict")
async def predict(data: MatchData):
    return [
        {
            "match": "Time A vs Time B",
            "market": "Ambos Marcam",
            "prediction": "Sim",
            "confidence": 88,
            "type": "histórico"
        },
        {
            "match": "Time A vs Time B",
            "market": "Mais de 2.5 Gols",
            "prediction": "Sim",
            "confidence": 92,
            "type": "histórico"
        }
    ]

# Exemplo de rota para odds ao vivo
@app.get("/odds/live")
async def get_live_odds():
    return {
        "response": [
            {
                "teams": {
                    "home": {"name": "Time A"},
                    "away": {"name": "Time B"}
                },
                "league": {"name": "Liga X"},
                "bookmakers": [
                    {
                        "bets": [
                            {
                                "name": "Resultado Final",
                                "values": [
                                    {"value": "Casa", "odd": "1.80"},
                                    {"value": "Empate", "odd": "3.50"},
                                    {"value": "Fora", "odd": "4.20"}
                                ]
                            },
                            {
                                "name": "Mais de 2.5 Gols",
                                "values": [
                                    {"value": "Sim", "odd": "1.90"},
                                    {"value": "Não", "odd": "2.00"}
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }