from pydantic import BaseModel

class PredictionInput(BaseModel):
    recorded_time: str
    direction_ref: int
    published_line_name: str
    next_stop_point_name: str