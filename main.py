import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()  # objeto mensageiro

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
INSERT OR IGNORE INTO contas_bancarias (titular, saldo, cpf)
VALUES (?, ?, ?)
""", ("gustavo", 10000000000, "054542323"))

cursor.execute("SELECT titular, saldo FROM contas_bancarias")
contas = cursor.fetchall()

for conta in contas:
    titular, saldo = conta

    print(f"""
    titular: {titular}
    saldo: {saldo}
    """)
cursor.execute("DELETE FROM contas_bancarias WHERE id = 2")

conexao.commit()
conexao.close()
