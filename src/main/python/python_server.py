from py4j.java_gateway import JavaGateway, GatewayParameters


class PythonServer:
    def __init__(self, java_gateway):
        self.java_gateway = java_gateway
        self.java_server = java_gateway.entry_point  # Get the Java entry point

    def convert_java_list_to_python(self, java_list):
        # Convert Java List to Python list
        python_list = list(java_list)
        return python_list

    def convert_python_to_java_list(self, python_list):
        # Convert Python list to Java ArrayList
        java_list = self.java_gateway.jvm.java.util.ArrayList()
        for item in python_list:
            java_list.add(item)
        print(type(java_list))
        return java_list

    def modify_with_space(self, data):
        python_list= self.convert_java_list_to_python(data)
        print(type(python_list))
        python_list.append("hellloooo")
        print(python_list)
        original_list=self.convert_python_to_java_list(python_list)
        return original_list

    def changes(self):
        # Get the Python function name from the Java instance
        python_function_name = self.java_server.getPythonFunctionName()

        print("Original Data:", self.java_server.getData())
        #print(type(self.java_server.getData()))
        # Call the custom Python function to modify the data
        modified_data = getattr(self, python_function_name)(self.java_server.getData())

        self.java_server.setData(modified_data)

        # Print the original and modified data
        print("Modified Data:", modified_data)


if __name__ == "__main__":
    # Start a Py4J gateway to connect to Java
    gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_field=True))
    py_server = PythonServer(gateway)

    py_server.changes()
    # Shutdown the Py4J gateway
    gateway.shutdown()
    print("server closed")
