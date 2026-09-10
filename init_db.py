import sqlite3

conn = sqlite3.connect("review.db")
cursor = conn.cursor()

with open("schema.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

cursor.execute("INSERT INTO subjects (name) VALUES (?)",("이산수학",))
subject_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO materials (subject_id, title, content, date) VALUES (?, ?, ?, ?)", (subject_id, "3주차 정리 - 그래프 이론","오일러 경로, 해밀턴 경로 정리", "2026-09-10")
)
material_id = cursor.lastrowid

cursor.execute("INSERT INTO originals (material_id, label, content) VALUES (?, ?, ?)",
    (material_id, "강의자료", "그래프 이론 슬라이드 요약..."))
cursor.execute("INSERT INTO originals (material_id, label, content) VALUES (?, ?, ?)",
    (material_id, "녹음", "쾨니히스베르크 다리 문제를 예시로..."))

conn.commit()
conn.close()
print("DB 생성 완료")