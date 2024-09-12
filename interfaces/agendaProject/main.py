from db.database import CreateDataBaseSQLite
from view import AgendaView

if __name__ == '__main__':
    _db = CreateDataBaseSQLite()
    _db.run_script()

    view = AgendaView()
    view.run_view()