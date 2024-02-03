from ...utils.utils import selDB, insDB
from ..models.clientModel import Client
class Client:
    def getAll():
        query = "select * from clients;"
        clients = selDB(query)
        return clients

    def createClient(client: Client):
        query = "insert into clients(name, birthday_date, gender, health_problem_name, health_problem_grade, created_at, updated_at) "
        query += "values(%s, %s, %s, %s, %s, %s, %s) "
        values = (
                    client.name, 
                    client.birthday_date, 
                    client.gender, 
                    client.health_problem_name, 
                    client.health_problem_grade, 
                    client.created_at, 
                    client.updated_at
                )
        clientCreated = insDB(query, values)
        return clientCreated

    def updateClient(): pass

    def deleteClient(): pass

    def highestRiskClient(): pass