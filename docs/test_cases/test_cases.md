# Test Cases 

**Requirement 1** 
* When launched, the application should wait for http connections.  

### Test Case 1.1 Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual.  

##### Test Steps:  
1. Open a web browser and navigate to the URL: http://localhost:8088  
    Or alternatively:  
    1.1. Open cmd/bash/terminal and issue a command: `curl "http://localhost:8088"`  
    1.2. Start Postman and create a new GET request using the enpoint: "http://localhost:8088"  
2. Verify that the application is returning a response.  

##### Expected result:  
The application should return a response.  


**Requirement 2**
* Application should answer on the PORT specified in the PORT environment variable.    

### Test Case 2.1 Enahncement to Test Case 1.1, Negative Scenario.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual.  

##### Test Steps:  
1. Open a web browser and navigate to the URL: http://localhost:8088  
    Or alternatively:  
    1.1. Open cmd/bash/terminal and issue a command: `curl "http://localhost:8088"`  
    1.2. Start Postman and create a new GET request using the enpoint: "http://localhost:8088"  
2. Verify that the application is returning a response. 
3. Attempt to access the application on a different port. Use ranges of ports to verify that the application is NOT listening on other ports except the specified in the PORT environment variable.  
    3.1 Try range: 8000-8999 common local web server ports.  
    3.2 Try range: 3000-3999 common local web server ports.  

##### Expected result:  
The application should return a response when request is sent using port 8088. The application should not reply on other ports.

**Requirement 3**
* The application should support three endpoints.

**Requirement 3.1** 
* The application should support POST requests on endpoint /hash. It should return a job identifier immediately. It should then wait 5 seconds and compute the password hash. The hashing algorithm should be SHA512

### Test Case 3.1.1  Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps:  
1. Open Postman.  
2. Create a new POST request using the enpoint: "http://localhost:8088/hash"  
3. Open request body tab, select "raw" then format JSON.  
4. Enter the following JSON:  
   ```
    {  
        "password": "testpassword"  
    } 
    ```
5. Save the request.
6. Send the request.

##### Expected result:  
The response status code should be 200. The application should return a response. The response should contain a job identifier. The application should then wait 5 seconds and compute the password hash. The hashing algorithm should be SHA512.


### Test Case 3.1.2 Negative Scenario.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps:  
1. Open Postman.  
2. Create a new POST request using the enpoint: "http://localhost:8088/hash"  
3. Open request body tab, select "raw" then format JSON.  
4. Substitute key name "password" in the request nody JSON with any other key name, e.g:  
   ```
    {  
        "blahblahbalh": "testpassword"  
    } 
    ```
5. Save the request.
6. Send the request.

##### Expected result:  
The response status code should be 400. The application should return an error message when unexpected key name is used in the request body. 


### Test Case 3.1.3 Negative Scenario.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps:  
1. Open Postman.  
2. Create a new POST request using the enpoint: "http://localhost:8088/hash"  
3. Open request body tab, select "raw" then format JSON.  
4. Substitute value "testpassword"  in the request body JSON with any other data type, e.g, booleans, integers, floating point numbers, etc., attempt to input extra long strings, e.g:  
   ```
    {  
        "password": true  
    } 
    ```
    ```
    {  
        "password": 1234
    } 
    ```
    ```
    {  
        "password": 4.543  
    } 
    ```
5. Save the request.
6. Send the request.

##### Expected result:  
The response status code should be 400. The application should return an error message when unexpected value is provided for the key-vlaue pair in the request body. 


**Requirement 3.2** 
* The application should support GET requests on endpoint /hash/{job_id}. It should return the base64 encoded password hash for the corresponding POST request.

### Test Case 3.2.1  Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps:  
1. Open Postman.  
2. Create a new POST request using the enpoint: "http://localhost:8088/hash"  
3. Open request body tab, select "raw" then format JSON.  
4. Enter the following JSON:  
   ```
    {  
        "password": "testpassword"  
    } 
    ```
5. Save the request.
6. Send the request.
7. The response status code should be 200.
8. Take note on the job identifier received back.
9. In Postman create another request, use GET and the endpoint: "http://localhost:8088/hash/{job_id}" where {job_id} is the job identifier received in the previous request. 
10. Study the response. 

##### Expected result:  
The response status should be 200. The application should return a response in a form of a base64 encoded password hash. The expected length is 88 characters.

### Test Case 3.2.2  Negative Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps:  
1. Open Postman.  
2. In Postman create a GET and the endpoint: "http://localhost:8088/hash/{job_id}" where {job_id} is the random job identifier that has never been returned by the post requrest before. e.g. 31678537 
3. Study the response. 

##### Expected result:  
The response status code should be 400. The application should return a response with an error message stating that the job identifier is not found/incorrect.


**Requirement 3.3** 
* The application should support GET requests on endpoint /stats. It should accept no data. It should return a JSON data structure for the total hash requests since the server started and the average time of a hash request in milliseconds.

### Test Case 3.3.1  Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps: 
1. Restart the application.
2. Open Postman.  
3. Create a new POST request using the enpoint: "http://localhost:8088/hash"  
4. Open request body tab, select "raw" then format JSON.  
5. Enter the following JSON:  
   ```
    {  
        "password": "testpassword"  
    } 
    ```
6. Save the request.
7. Send exactly one request.
8. The response status code should be 200.
9. In Postman create a GET and the endpoint: "http://localhost:8088/stats"
10. Save the request.  
11. Send the request.  
12. Study the response.  

##### Expected result:  
The response status code should be 200. The application should return the total amount of hash requests since the server started, 1 in this scenario and the average time of a hash request in milliseconds which for 1 request should be equal to 5000.

### Test Case 3.3.2  Negative Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use.

##### Test Steps: 
1. Execute Test Case 3.3.1.
2. In Postman create a POST request, use the endpoint: "http://localhost:8088/stats"
3. Open request body tab, select "raw" then format JSON.  
4. Enter the following JSON:  
   ```
    {  
        "password": "testpassword"  
    } 
    ```
5. Save the request. 
6. Send the request.  
7. Study the response.  

##### Expected result:  
The response status code should be 400. The application should return an error, per the specification the endpoint: http://localhost:8088/stats shouldn't accept any data.  


**Requirement 4** 
* The software should be able to process multiple connections simultaneously.  

### Test Case 4.1 Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. "Requests" python library is installed in the test environment.

##### Test Steps: 
1. Download a python script spam_reqs.py from the tools folder of this repo to the test box. 
2. Open 3+ terminal windows and execute the following commands: 
    ```
    python spam_reqs.py
    ```
3. Study the output and monitor the application CPU and Memory consumption.

##### Expected result:  
Per the specification, the application should be able to process multiple connections simultaneously. 


**Requirement 5** 
* The software should support a graceful shutdown request. Meaning, it should allow any in-flight password hashing to complete, reject any new requests, respond with a 200 and shutdown.

### Test Case 5.1 Positive Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. "Requests" python library is installed in the test environment.

##### Test Steps: 
1. Download a python script spam_reqs.py from the tools folder of this repo to the test box. 
2. Start the script in a new terminal window. Make sure the script is running and reporting number of requests and status code.
3. Open Postman.
4. Create a new POST request using the enpoint: "http://localhost:8088/hash" and the plain text body as: shutdown
5. Save the request.
6. While the application is still running and processing requests from the script started in the Step 2, send the POST request created in the Step 4. 

##### Expected result:  
The software should support a graceful shutdown request. Meaning, it should allow any in-flight password hashing to complete, reject any new requests, respond with a 200 and shutdown.


**Requirement 6** 
* No additional password requests should be allowed when shutdown is pending. 

### Test Case 6.1 Negative Scenario

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. "Requests" python library is installed in the test environment.

##### Test Steps: 
1. Start test case 4.1 with 3+ terminal windows. Keep the scripts running.
2. Open Postman.
3. Create a new POST request using the enpoint: "http://localhost:8088/hash" and the plain text body as: shutdown
4. Save the request.
5. While the application is still running and processing requests from the scripts send the POST request created in the Step 3.  

##### Expected result:  
1. The software should support a graceful shutdown request. Meaning, it should allow any in-flight password hashing to complete, reject any new requests, respond with a 200 and shutdown.
2. No additional password requests should be allowed when shutdown is pending. 
