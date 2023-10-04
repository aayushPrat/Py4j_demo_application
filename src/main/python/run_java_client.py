import subprocess

# Path to the java file
java_file = "/Users/aayushsingh/PycharmProjects/testpy4j/src/main/java/CustomData.java"

# Specify the classpath including the path to the Py4J JAR file
classpath = "/Users/aayushsingh/PycharmProjects/testpy4j/src/main/java/lib/py4j-0.10.9.7.jar:."

# Command to run the Java class
java_command = f"java -cp {classpath} {java_file}"

try:
    # Run the Java class as a subprocess
    subprocess.check_call(java_command, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error running Java client: {e}")
