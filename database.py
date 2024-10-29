from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/db_project"

engine = create_engine(DATABASE_URL, echo=True)

#Função de dependencias para criar uma sessao no bbanco de dados.
def get_session():
    with Session(engine) as session:
        yield session

# Função para criar as tabelas no banco.
def create_tables():
    SQLModel.metadata.create_all(engine)