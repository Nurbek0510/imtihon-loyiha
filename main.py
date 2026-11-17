from funksiyalar import (
    bazaga_ulanish,
    vazifa_qoshish,
    vazifalarni_korish,
    vazifa_qidirish
)


def main():
    db = bazaga_ulanish()
    print("MySQL bazasiga ulandi.")

    while True:
        print("\n===== VAZIFALAR RO‘YXATI =====")
        print("1. Vazifa qo‘shish")
        print("2. Vazifalarni ko‘rish")
        print("3. Vazifa qidirish")
        print("0. Chiqish")

        tanlov = input("Tanlang: ").strip()

        if tanlov == "1":
            vazifa_qoshish(db)
        elif tanlov == "2":
            vazifalarni_korish(db)
        elif tanlov == "3":
            vazifa_qidirish(db)
        elif tanlov == "0":
            break
        else:
            print("Noto‘g‘ri tanlov. 1, 2, 3 yoki 0 ni kiriting.")

    db.close()
    print("Dastur yakunlandi.")


if __name__ == "__main__":
    main()