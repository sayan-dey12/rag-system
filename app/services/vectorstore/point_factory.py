from app.services.vectorstore.point_builder import PointBuilder


class PointBuilderFactory:

    _builder: PointBuilder | None = None

    @classmethod
    def get_builder(cls) -> PointBuilder:

        if cls._builder is None:
            cls._builder = PointBuilder()

        return cls._builder