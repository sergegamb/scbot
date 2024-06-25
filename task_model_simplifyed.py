from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str
    id: str | int

    def representation(self):
        return {
            "id": self.id,
            "title": self.title
        }
