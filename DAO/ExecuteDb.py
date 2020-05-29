class ExecuteDb:
    def Execute():
        import DbFactury
        sqlite = DbFactury.DbFactury.DataBase('SQLite').CreateConnector('ola.db').Connect();
        cursor = sqlite.cursor()

# criando a tabela (schema)
        cursor.execute("""
        CREATE TABLE clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                cpf     VARCHAR(11) NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                cidade TEXT,
                uf VARCHAR(2) NOT NULL,
                criado_em DATE NOT NULL
        );
        """)

        print('Tabela criada com sucesso.')

        
if __name__ == '__main__':
    ExecuteDb.Execute()

