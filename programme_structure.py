from typing import List, Optional
from pydantic import BaseModel

class Performer(BaseModel):
    performer_name: str
    performer_instrument: str

class Piece(BaseModel):
    piece_name: str
    piece_year_start: Optional[int] = None
    piece_year_end: Optional[int] = None
    composer_name: Optional[str] = None
    composer_year_birth: Optional[int] = None
    composer_year_death: Optional[int] = None
    arranger_name: Optional[str] = None
    opus_number: Optional[str] = None
    item_number: Optional[str] = None
    movements: Optional[List[str]] = None
    performers: List[Performer]

class Concert(BaseModel):
    concert_name: str
    date: str
    start_time: str
    end_time: Optional[str] = None
    list_of_pieces: List[Piece]
