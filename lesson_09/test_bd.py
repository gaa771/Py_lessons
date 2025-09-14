from sqlalchemy import create_engine, text

db = create_engine("postgresql://postgres:123@localhost:5432/QA")


# Поиск студента с максимальным id
def get_max_id():
    connection = db.connect()
    sql_statement = text("SELECT MAX(\"user_id\") FROM student")
    result = connection.execute(sql_statement)
    max_id = result.scalar()
    connection.close()
    return max_id


# Добавление новой записи о студенте
def test_insert_student():
    connection = db.connect()
    transaction = connection.begin()

    new_id = get_max_id() + 1
    sql = text("INSERT INTO student(\"user_id\") VALUES (:new_id)")
    connection.execute(sql, {"new_id": new_id})

    sql_statement = text(
        "SELECT * FROM student WHERE user_id = :select_user_id")
    result = connection.execute(sql_statement, {"select_user_id": new_id})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["user_id"] == new_id

    transaction.commit()
    connection.close()


# Обновление информации о студенте (level)
def test_update_student():
    connection = db.connect()
    transaction = connection.begin()

    new_id = get_max_id()
    sql = text("UPDATE student SET level = :lev WHERE user_id = :id")
    connection.execute(sql, {"lev": 'Pre-Intermediate', "id": new_id})

    sql_statement = text(
        "SELECT * FROM student WHERE user_id = :select_user_id")
    result = connection.execute(sql_statement, {"select_user_id": new_id})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["level"] == 'Pre-Intermediate'

    transaction.commit()
    connection.close()


# Удаление записи о студенте
def test_delete_student():
    connection = db.connect()
    transaction = connection.begin()

    new_id = get_max_id()
    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {"id": new_id})

    sql_statement = text(
        "SELECT * FROM student WHERE user_id = :select_user_id")
    result = connection.execute(sql_statement, {"select_user_id": new_id})
    rows = result.mappings().all()
    assert len(rows) == 0

    transaction.commit()
    connection.close()
