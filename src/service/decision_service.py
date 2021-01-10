import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import DecisionRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class DecisionService:

    def get_decision(self, decision_repository: DecisionRepository):
        decision = []
        data = decision_repository.get_decision_bd()
        for result in data:
            decision.append(
                {
                    'iddecision': result[0],
                    'nombre': result[1],
                }
            )
        return decision