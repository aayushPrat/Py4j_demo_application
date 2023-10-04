import py4j.GatewayServer;

public class CustomData {
    private String pythonFunctionName="modify_with_space";
    private String data="Hi";

    public String getPythonFunctionName() {
        return pythonFunctionName;
    }

    public void setPythonFunctionName(String pythonFunctionName) {
        this.pythonFunctionName = pythonFunctionName;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public static void main(String[] args) {
        // Create an instance of CustomData
        CustomData customData = new CustomData();
        // Start the Py4J gateway server
        GatewayServer gatewayServer = new GatewayServer(customData);
        gatewayServer.start();
        System.out.println("Py4J gateway server started...");

    }
}
