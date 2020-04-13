import json
import grpc
from google.protobuf.timestamp_pb2 import Timestamp

import foobar_pb2
import foobar_pb2_grpc

channel = grpc.insecure_channel("localhost:4040")

stub = foobar_pb2_grpc.FoobarHandlerStub(channel)

timestamp = Timestamp()
# Store Foobar
fb = foobar_pb2.Foobar(
    FoobarContent="Python as Client here!!!",
    CreatedAt=timestamp.GetCurrentTime(),
    UpdatedAt=timestamp.GetCurrentTime(),
)
created_foobar = stub.Store(fb)
print("\nCreated Foobars\n")
print(created_foobar)

# Get All Foobars
get_list_foobar = foobar_pb2.FetchRequest(num=1)

list_foobar = stub.GetListFoobar(get_list_foobar)

print("Foobars\n")
for f_bar in list_foobar.Foobars:
    print(f_bar)

# Get Foobar By ID
get_foobar = foobar_pb2.SingleRequest(ID="edc2f74e-7e3f-4e0d-805f-e9ab3420ddd1")

foobar = stub.GetFoobar(get_foobar)

print("Detail Foobar\n")
print(foobar)