from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    stuId: int


class CreateStudent(StudentBase):
    pass

class ShowStudent(StudentBase):
    pass


class Participant(BaseModel):
    pid: int
    stuId: int
    activity: str


class Activity(BaseModel):
    activity: str
    cost: int


