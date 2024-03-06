import subprocess

# Specify the path to your runnable JAR file
jar_path = r"C:\Users\GOD\Documents\Desktop_Sikuli_Scripts\PT-L3_sikuli.jar"

# Construct the command to run the JAR file
java_command = f"java -jar {jar_path}"

try:
    # Execute the command
    subprocess.run(java_command, shell=True, check=True)
    print("JAR file executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing JAR file: {e}")
