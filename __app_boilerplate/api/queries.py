from utils.queries import IQuery, IQuerySpec


class SomeQuery(IQuery):
    def query(self, spec: IQuerySpec) -> SomeDTO:
        pass
