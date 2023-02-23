from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select, col
from pprint import pprint


class Equipo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    nombre: str
    sede: str

class Héroe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, unique=True)
    nombre_secreto: str
    edad: Optional[int] = None
    equipo_id: Optional[int] = Field(default=None, foreign_key="equipo.id")

   
sqlite_nombre = "database.db"
sqlite_url = f"sqlite:///{sqlite_nombre}"
engine = create_engine(sqlite_url, echo=True)


def crear_héroes():
    h1 = Héroe(nombre="Pomelo", nombre_secreto="Pome", edad=10)
    h2 = Héroe(nombre="TheWalker", nombre_secreto="Mica")
    h3 = Héroe(nombre="Pitipuchi", nombre_secreto="Facu", edad=37)
    print("\nAntes de comitear la sesión:")
    print("Héroe 1:", h1)
    print("Héroe 2:", h2)
    print("Héroe 2:", h3)

    with Session(engine) as session:
        session.add(h1)
        session.add(h2)
        session.add(h3)
        session.commit()
        print("\nDespués de comitear la sesión: muestra IDs")
        print("Héroe 1:", h1.id)
        print("Héroe 2:", h2.id)
        print("Héroe 2:", h3.id)
        print("\nDespués de comitear la sesión: muestra nombres")
        print("Héroe 1:", h1.nombre)
        print("Héroe 2:", h2.nombre)
        print("Héroe 2:", h3.nombre)

        session.refresh(h1)
        session.refresh(h2)
        session.refresh(h3)

        print("\nDespués de refrescar los héroes:")
        print("Héroe 1:", h1)
        print("Héroe 2:", h2)
        print("Héroe 2:", h3)

    print("\nDespués de que se cierra la sesión")
    print("Héroe 1:", h1)
    print("Héroe 2:", h2)
    print("Héroe 2:", h3)


def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)


def consultar_héroes():
    with Session(engine) as session:
        # h = session.exec(select(Héroe)).all()
        sentencia = select(Héroe).where(
            col(Héroe.edad) >= 12, col(Héroe.edad) < 38)
        registros = session.exec(sentencia)
        for h in registros:
            print("\n", h)

def modificar_héroes():
    with Session(engine) as session:
        consulta = select(Héroe).where(Héroe.id == 2)
        resultado = session.exec(consulta)
        héroe = resultado.one()
        print("Héroe:", héroe)
        héroe.edad=20
        session.add(héroe)
        session.commit()
        session.refresh(héroe)
        print("Héroe modificado:", héroe)

def eliminar_héroes():
    with Session(engine) as session:
        consulta = select(Héroe).where(Héroe.nombre == "TheWalker")
        resultado = session.exec(consulta)
        héroe = resultado.one()
        print("Héroe: ", héroe)
        session.delete(héroe)
        session.commit()
        print("Héroe eliminado: ")


def main():
    crear_db_y_tablas()
    # crear_héroes()
    # consultar_héroes()
    # modificar_héroes()
    # eliminar_héroes()


if __name__ == "__main__":
    main()
