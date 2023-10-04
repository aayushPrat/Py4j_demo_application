from py4j.java_gateway import JavaGateway, GatewayParameters


class PythonServer:
    def __init__(self, java_gateway):
        self.java_gateway = java_gateway
        self.java_server = java_gateway.entry_point  # Get the Java entry point

    def modify_with_space(self, data):
        new_str = "space" + data
        return new_str

    def changes(self):
        # Get the Python function name from the Java instance
        python_function_name = self.java_server.getPythonFunctionName()


        print("Original Data:", self.java_server.getData())
        # Call the custom Python function to modify the data
        modified_data = getattr(self, python_function_name)(self.java_server.getData())

        # Update the Java data with the modified data
        self.java_server.setData(modified_data)

        # Print the original and modified data
        print("Modified Data:", modified_data)

        #check the original java data
        #print(self.java_server.getData())

if __name__ == "__main__":
    # Start a Py4J gateway to connect to Java
    gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
    py_server = PythonServer(gateway)
    py_server.changes()
    # Shutdown the Py4J gateway
    gateway.shutdown()
    print("server closed")
