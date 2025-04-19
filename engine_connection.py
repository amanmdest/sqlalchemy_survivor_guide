from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:passtest@localhost:3306/cinema')
conn = engine.connect()
# response = conn.exec_driver_sql('SELECT * FROM filmes;')

query = text('SELECT * FROM filmes;')

response = conn.execute(query)
# response = engine.execute(query) 
# AttributeError: 'Engine' object has no attribute 'execute'

print(response) 
# <sqlalchemy.engine.cursor.CursorResult object at 0x7fe1047a3150>


for row in response:
    print(row)
    print(row.titulo)


# with engine.connect() as conn:
#     result = conn.execute(stmt)

# result = session.execute(stmt)