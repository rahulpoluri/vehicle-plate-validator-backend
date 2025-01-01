from fastapi import HTTPException
from sqlalchemy import text

from application.db.connection import SessionLocal


class Mixin:
    @classmethod
    def get_session(cls):
        return SessionLocal()

    @classmethod
    def get_with_fuzzy_search(
        cls,
        search_key: str,
        levenshtein: int,
        page_size: int = 10,
        page_number: int = 0,
    ):
        limit = page_size
        offset = (page_number - 1) * page_size
        with cls.get_session() as session:
            # for creating fuxzystrmatch extension
            query_text1 = text("CREATE EXTENSION fuzzystrmatch;")
            # for searching with levenshtein distance
            query_text2 = text(
                "CREATE TEMP TABLE temp_table AS "
                "SELECT * FROM plates "
                "WHERE levenshtein(plate, :search_key) <= :levenshtein"
            )
            # for getting the data
            query_text3 = text(
                "SELECT * FROM temp_table " "Limit :limit OFFSET :offset"
            )
            # for getting the count of the total data
            query_text4 = text("SELECT COUNT(*) FROM temp_table")
            session.execute(query_text1)
            session.execute(
                query_text2,
                {"search_key": search_key, "levenshtein": levenshtein},
            )
            data = (
                session.execute(
                    query_text3, {"limit": limit, "offset": offset}
                )
                .mappings()
                .all()
            )
            total = session.execute(query_text4).scalar()
            return data, total

    @classmethod
    def get_all(cls):
        with cls.get_session() as session:
            return session.query(cls).all()

    @classmethod
    def put(cls, data):
        with cls.get_session() as session:
            session.add(data)
            session.commit()
            return data

    @classmethod
    def get_one_or_404(cls, **data):
        with cls.get_session() as session:
            response = session.query(cls).filter_by(**data).first()
            if response is None:
                raise HTTPException(status_code=404, detail="Not Found")
            return response

    def save(self):
        with self.get_session() as session:
            session.add(self)
            session.commit()
