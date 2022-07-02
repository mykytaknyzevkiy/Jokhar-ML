from db.JokharDB import jokharDB
from db.model.MoveEntity import MoveEntity
from tinydb import Query

_table = jokharDB.table('move_history')


def insert(self: MoveEntity):
    _table.insert(self.toJson())


def listGps():
    def mapJsonToMoveHistory(json):
        return MoveEntity.createFromJson(json)

    return list(map(mapJsonToMoveHistory, _table.search(Query().isGps == True)))
