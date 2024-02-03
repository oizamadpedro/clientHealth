from ...utils.utils import selDB, insDB
class Client:
    def getAll():
        query = "select * from clients;"
        clients = selDB(query)
        return clients

    def createClient(): pass

    def updateClient(): pass

    def deleteClient(): pass

    def highestRiskClient(): pass