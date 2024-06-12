#https://github.com/ONETAPL3G3ND
import grpc
import MainServer_pb2, MainServer_pb2_grpc

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:50000')
    stub = MainServer_pb2_grpc.MainServerStub(channel)

    id = int(input("Enter ID:"))
    Text = input("Enter Text:")
    request = MainServer_pb2.Message(Text=Text, ID=id)
    respons = stub.SendMessage(request)
    print("Code:", respons.Status)


