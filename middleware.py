from fastapi import Request, HTTPException
import jwt
from starlette.responses import JSONResponse

SECRET_KEY = "npfmlTGEKFz3fzOWojTipNAGXMSS4mmJPYzvroFVFaQ"
ALGORITHM = "HS256"

def create_token(dados: dict):
    token = jwt.encode(dados, SECRET_KEY,ALGORITHM)
    return token

async def auth_middleware(request:Request, call_next):

    if request.url == "http://127.0.0.1:8000/docs" :
        response = await call_next(request)
        return response

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return JSONResponse({"error": "Token nao enviado"}, status_code=401)
    
    if auth_header:
        
        token = auth_header
        try:
            if not token:
                return JSONResponse({"error": "Token nao enviado"}, status_code=401)
            # Decodifica o JWT usando SECRET_KEY e ALGORITHM corretos
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.state.user = payload  # Adiciona dados do usuário à requisição
        except jwt.DecodeError:
            return JSONResponse({"error": "Token inválido"}, status_code=401)
        except jwt.ExpiredSignatureError:
            return JSONResponse({"error": "Token expirado"}, status_code=401)

    response = await call_next(request)
    return response
