### Proper format for curl in Windows environments:

- In CMD: `curl -X POST -H "Content-Type: application/json" -d "{\"password\":\"test1\"}" http://127.0.0.1:8088/hash`  

- In PoswerShell `curl -X POST -H "Content-Type: application/json" -d '{\"password\":\"test1\"}' http://127.0.0.1:8088/hash`  

### Proper format for curl in Linux environments:

- Linux `curl -X POST -H "application/json" -d '{"password":"test1"}' http://127.0.0.1:8088/hash`
