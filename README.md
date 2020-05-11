# test-API
Инструкция:
1. Все необходимые библиотеки в файле requirements.txt
2. Открыть скрипт mongo_db_script.py
3. Заменить в строке cluster = MongoClient("mongodb+srv://user_avito:<***>@... значение "<***>" на пароль высланный в письме
4. Запустить сервер через терминал $uvicorn main:app --reload


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

Example:<br>
curl -X GET "http://127.0.0.1:8000/secrets/{secret_key}" -H  "accept: application/json"<br>
Request URL<br>
http://127.0.0.1:8000/secrets/{secret_key}
