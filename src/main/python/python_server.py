from py4j.java_gateway import JavaGateway, GatewayParameters


class MyPythonServer:
    def __init__(self, java_gateway):
        self.java_gateway = java_gateway
        self.java_server = java_gateway.entry_point  # Get the Java entry point
        print("Before the Change- " + self.java_server.getJavaData())

    # In this funtion we have changed the value of javaData variable from the java class.
    def modify_java_data(self):
        print("Modifying the data......")
        new_modified_data = self.java_server.getJavaData() + " modified in python"
        self.java_server.setJavaData(new_modified_data)
        print(self.java_server.getJavaData())  # check if the change has occurred.


if __name__ == "__main__":
    gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
    python_server = MyPythonServer(gateway)
    python_server.modify_java_data()
    gateway.shutdown()
    print("Server Closed")
