import numpy as np
import joblib
import sys

from fastapi import FastAPI
from pydantic import BaseModel

class Answer(BaseModel):
    like_challenges: int # 1
    affinity_math: int # 2
    affinity_physics: int # 3
    affinity_chemistry: int # 4
    affinity_human_sci: int # 5
    affinity_biology_sci: int # 6
    affinity_eng: int # 7
    interest_new_results: int # 8
    like_mental_games: int # 9
    like_improve_opportunities: int # 10
    interest_how_thing_works: int # 11
    like_individual_work: int # 12
    how_many_creative: int # 13
    are_you_leader: int # 14
    how_many_concentration: int # 15
    are_you_autodidact: int # 16
    vocacional_orientation_inside: int # 17
    vocacional_orientation_outside: int # 18
    like_practical_usages: int # 19
    enjoy_older_people: int # 20
    how_many_organized: int # 21
    feel_parental_support: int # 22
    how_many_parental_support: int # 23
    like_teach: int #24
    like_dissarm: int #25
    experience_team_works: int # 26
    assimilate_text: int #27
    like_paint: int #28
    like_build: int #29
    like_read: int #30

app = FastAPI()
RF = joblib.load('Model.sav')

# Readable classes
readable_classes = [
    'Bioingeniería',
    'Ingeniería agroindustrial',
    'Ingeniería ambiental',
    'Ingeniería bioquímica',
    'Ingeniería civil',
    'Ingeniería Eléctrica',
    'Ingeniería electrónica',
    'Ingeniería energética',
    'Ingeniería Industrial',
    'Ingeniería Mecánica',
    'Ingeniería Química',
    'Ingeniería sanitaria',
    'Ingeniería de sistemas',
    'Ingeniería de telecomunicaciones'
    ]

@app.post("/")
def read_root(a: Answer):
    answers = [
        a.like_challenges,
        a.affinity_math,
        a.affinity_physics,
        a.affinity_chemistry,
        a.affinity_human_sci,
        a.affinity_biology_sci,
        a.affinity_eng,
        a.interest_new_results,
        a.like_mental_games,
        a.like_improve_opportunities,
        a.interest_how_thing_works,
        a.like_individual_work,
        a.how_many_creative,
        a.are_you_leader,
        a.how_many_concentration,
        a.are_you_autodidact,
        a.vocacional_orientation_inside,
        a.vocacional_orientation_outside,
        a.like_practical_usages,
        a.enjoy_older_people,
        a.how_many_organized,
        a.feel_parental_support,
        a.how_many_parental_support,
        a.like_teach,
        a.like_dissarm,
        a.experience_team_works,
        a.assimilate_text,
        a.like_paint,
        a.like_build,
        a.like_read
    ]
    result = RF.predict_proba([answers])
    human_readable = []

    for index in range(len(readable_classes)):
        human_readable.append({ 'name': readable_classes[index], 'percent': result[0][index] * 100 })

    return human_readable
