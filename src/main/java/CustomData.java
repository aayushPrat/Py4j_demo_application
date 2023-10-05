import py4j.GatewayServer;
import java.util.*;

public class CustomData<T> {
    private String pythonFunctionName="";
    private T data;

    public String getPythonFunctionName() {
        return pythonFunctionName;
    }

    public void setPythonFunctionName(String pythonFunctionName) {
        this.pythonFunctionName = pythonFunctionName;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public static void main(String[] args) {
        // Create an instance of CustomData
        CustomData<List<String>> customData = new CustomData<>();
        customData.setPythonFunctionName("modify_with_space");
        customData.setData(List.of("Hi","Hello","Hey"));
        // Start the Py4J gateway server
        GatewayServer gatewayServer = new GatewayServer(customData);
        gatewayServer.start();
        System.out.println("Py4J gateway server started...");
        while(true){
            try{
                Thread.sleep(1);
                System.out.println("checking");
                System.out.println(customData.getData());
            }
            catch(InterruptedException e){
                System.exit(0);
            }

        }



    }
}
