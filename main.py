from API import controller
from API.app import sql


if __name__ == "__main__":
    sql.init_db()
    controller.launch()
