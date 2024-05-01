import MainServer_pb2, MainServer_pb2_grpc
import grpc
import concurrent.futures
import Client
def run_server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    MainServer_pb2_grpc.add_MainServerServicer_to_server(MainServer(), server)
    server.add_insecure_port('0.0.0.0:50000')
    server.start()
    server.wait_for_termination()


class MainServer:

    def __init__(self):
        self.ClientList: Client.Client= []

    def GetClientFromToken(self, token):
        for client in self.ClientList:
            if client.



    def CreateAccount(self, request, context):
        token = ""
        return MainServer_pb2.AccountDataResponse(Token="")

    def SendMessage(self, request, context):
        status = 0
        return MainServer_pb2.MessageResponse(Status=status)

    def CheckMessage(self, request, context):
        return MainServer_pb2.CheckMessageRespons(Messages=[])

if __name__ == "__main__":
    run_server()