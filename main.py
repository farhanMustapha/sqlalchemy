from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

engine=create_engine('sqlite:///exemple.db', echo=True) #echo=True permet de voir les requetes de sql executer en arriere plan 

class User(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    age=Column(Integer)

Base.metadata.create_all(engine) #permet de creer les tqbles dans la base de donnee

Session=sessionmaker(bind=engine) # session allow us to make crud operation
session=Session()



def creat_user():
    nam=input("taper le nom : ")
    ag=input("tapez l'age : ")
    new_user=User(name=nam,age=ag) # lors de la creation we must put name of column= value 
    session.add(new_user) # we have an other unction session.add_all(name_of_object)
    session.commit()
 
creat_user() # call of function when we click on button 

users=session.query(User).all()
users.reverse()
print("------------- recu client -------------------")
for x in users:
    print("--------------------------------")
    print(f" {x.id} | {x.name} | {x.age} ")

print("merci pour votre visite ")

