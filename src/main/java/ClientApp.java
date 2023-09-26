
import py4j.GatewayServer;

public class ClientApp {
    private String javaData = "Java data";

    public String getJavaData() {
        return javaData;
    }

    public void setJavaData(String data) {
        javaData = data;
    }
/* ClientApp class acts as a Java server, exposing the javaData field and its methods to be
    accessed remotely from Python and get modified */

    public static void main(String[] args) {
        ClientApp app = new ClientApp();
        // Setting up the gateway server that allows communication between python and java.
        /* by passing app as an argument to gateway server we are telling py4j to expose the methods and fields
        of the app object so that we may access it via the py4j gateway. */
        GatewayServer server = new GatewayServer(app);
        server.start(); // starts listening for py4j requests from python
        System.out.println("Java server started.");
    }
}
