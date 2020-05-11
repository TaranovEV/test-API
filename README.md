# test-API
Methods:<br>
/generate - Generate your secret <br>
input: <br>
**secret**-(*type:string*), some text which will you need save <br>
**key**-(*type:string*), codeword<br>

Example:<br>
curl -X POST "http://127.0.0.1:8000/generate?secret={secret}&secret_key={key}" -H  "accept: application/json"

/secrets/{secret_key}<br>
Return your text <br>
input: <br>
**secret_key**-(*type:string*)<br>
