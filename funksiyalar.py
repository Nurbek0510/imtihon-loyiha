import mysql.connector


def bazaga_ulanish():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="threnlyy",
        database="vazifalar_bazasi"
    )


def vazifa_qoshish(db):
    nomi = input("Vazifa nomi: ").strip()

    if not nomi:
        print("Vazifa nomi bo‘sh bo‘lmasligi kerak.")
        return

    izoh = input("Izoh (ixtiyoriy): ").strip()
    muddat = input("Muddat (YYYY-MM-DD, bo‘sh qoldirish mumkin): ").strip()

    if not izoh:
        izoh = None
    if not muddat:
        muddat = None

    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO tasks (title, description, deadline)
        VALUES (%s, %s, %s)
        """,
        (nomi, izoh, muddat)
    )
    db.commit()
    cursor.close()

    print("Vazifa muvaffaqiyatli qo‘shildi.")


def vazifalarni_korish(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT id, title, description, status, deadline
        FROM tasks
        ORDER BY id
    """)

    vazifalar = cursor.fetchall()
    cursor.close()

    if not vazifalar:
        print("Hozircha vazifalar yo‘q.")
        return

    for vazifa in vazifalar:
        id, nomi, izoh, holat, muddat = vazifa
        print(f"\nRaqam: {id}")
        print(f"Vazifa: {nomi}")
        print(f"Izoh: {izoh or '-'}")
        print(f"Holat: {holat}")
        print(f"Muddat: {muddat or '-'}")


def vazifa_qidirish(db):
    so_z = input("Qidiriladigan vazifa nomini yozing: ").strip()

    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id, title, description, status, deadline
        FROM tasks
        WHERE title LIKE %s
        ORDER BY id
        """,
        (f"%{so_z}%",)
    )

    natijalar = cursor.fetchall()
    cursor.close()

    if not natijalar:
        print("Bunday vazifa topilmadi.")
        return

    for vazifa in natijalar:
        id, nomi, izoh, holat, muddat = vazifa
        print(f"\nRaqam: {id}")
        print(f"Vazifa: {nomi}")
        print(f"Izoh: {izoh or '-'}")
        print(f"Holat: {holat}")
        print(f"Muddat: {muddat or '-'}")