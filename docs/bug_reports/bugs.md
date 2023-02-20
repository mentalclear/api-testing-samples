# Bugs Discovered 

### Bug #1 

#### Description: Job identifier is not returned immediately after the POST resquest is sent to the /hash enpoint with correct payload. 

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. 

##### Replication Steps:  
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
7. Observe the response output.   

#### Actual result: 
When the POST resquest is sent to the /hash endpoint the job identifier will be returned after 5 seconds delay. 

#### Expected result:  
Per specification the job identifier should be returned immediately after the resquest is sent.

Notes. Discovered during Test Case 3.1.1 excution. See test_cases folder for respective test case.

### Bug #2 

#### Description: The application does not return hashed password after the POST resquest is sent to the /hash enpoint with correct payload.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. 

##### Replication Steps:  
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
7. Observe the response output.   

#### Actual result: 
The application returns the job identifier after the POST resquest is sent to the /hash enpoint with correct payload, but no hashed password being returned. There is a possibility of requirements gap here, since the requirement only specifies the hashing algoritm an not the output. 
Might need a clarification from a PM on what actaully we expect from the application. Currently there's no way to asses if the application is returning SHA512 hash upon the request. 

#### Expected result:  
Per specification the hashing algorithm should be SHA512. 

Notes. Discovered during Test Case #3.1.1 excution. See test_cases folder for respective test case.

### Bug #3 

#### Description: The POST resquest sent to the /hash enpoint with incorrect key name in the payload is not rejected.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. 

##### Replication Steps:  
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

#### Actual result: 
The application returns the job identifier after the POST resquest is sent to the /hash enpoint with correct payload, and there's no error  returned due to the incorrect key name in the payload.  
#### Expected result:  
When incorrect key name is used in the payload the application should reject the request and return an error.

Notes. Discovered during Test Case #3.1.2 excution. See test_cases folder for respective test case.


### Bug #4

#### Description: The time for a hasing requests is reported incorrectly in the stats.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. A stopwatch will be needed for the measurement.

##### Replication Steps:  
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
7. Start the stopwatch and send exactly one request.
8. The response status code should be 200.
9. Take the measurement from the stopwatch.
10. In Postman create a GET and the endpoint: "http://localhost:8088/stats"
11. Save the request.  
12. Send the request.  
13. Study the response.

#### Actual result: 
The application returns correct number of hash requests, but the time for 1 request is reported incorrectly. In my case each execution of the application returns the result in 100,000s ms. I've seen values from 100000 to 9000000ms. When the actual delay time and computation time toghether are no more than 6-7 seconds(6000 - 7000ms) in my environment.

#### Expected result:  
The application should return the total amount of hash requests since the server started, 1 in this scenario and the average time of a hash request in milliseconds which for 1 request should be equal to the computation time and include 5000ms for 5 sec dealy. 

Notes. Discovered during Test Case #3.3.1 excution. See test_cases folder for respective test case.

### Bug #5

#### Description: The POST resquest sent to the /stats enpoint is not rejected.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. 

##### Replication Steps:  
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

#### Actual result: 
The application returns status 200, and provides the stats output. This is in contrary to the specification which states that the endpoint 
/stats should NOT accept data.


##### Expected result:  
The response status code should be 400. The application should return an error, per the specification the endpoint: http://localhost:8088/stats shouldn't accept any data.

Notes. Discovered during Test Case #3.3.2 excution. See test_cases folder for respective test case.

### Bug #6

#### Description: The application doesn't shutdown gracefully under the requests load.

##### Preconditions: Windows/Linux/MacOS environment has been setup to run the application. An environment variable PORT is created and set to 8088. The application is installed and started per the installation manual. Postman standalone application is installed and ready to use. "Requests" python library is installed in the test environment.

##### Replication Steps:  
1. Download a python script spam_reqs.py from the tools folder of this repo to the test box. 
2. Open 3+ terminal windows and execute the following commands: 
    ```
    python spam_reqs.py
    ```
3. Study the output and monitor the application CPU and Memory consumption.
4. Open Postman.
5. Create a new POST request using the enpoint: "http://localhost:8088/hash" and the plain text body as: shutdown
6. Save the request.
7. While the application is still running and processing requests from the scripts send the POST request created in the Step 5.  

#### Actual result: 
After the sutdown request is sent the application doesn't shutdown gracefully. It continues to process requests even after reporting that shutdown signal is received. One of the instances of the scripts will fail, but others would be able to continue sending new requests and the app continiously processes them until another shutdown request is issued.

##### Expected result:  
The software should support a graceful shutdown request. Meaning, it should allow any in-flight password hashing to complete, reject any new requests, respond with a 200 and shutdown. No additional password requests should be allowed when shutdown is pending. 

Notes. Discovered during Test Case #6.1 excution. See test_cases folder for respective test case.
