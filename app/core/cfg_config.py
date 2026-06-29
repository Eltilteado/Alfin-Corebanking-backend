from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base de datos PostgreSQL en la nube. En Render debe venir desde Environment Variables.
    DATABASE_URL: str

    # Clave JWT. En Render puedes sobrescribirla con una SECRET_KEY propia.
    SECRET_KEY: str = "alfin_core_change_me_in_render_2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # URL del backend del portal cliente/homebanking si alguna ruta del core lo consulta.
    PORTAL_BACKEND_URL: str = "http://localhost:8000"
    PORT: int = 8001

    # Dominios permitidos para CORS. Puedes sobrescribirlo en Render si cambias tu dominio.
    # Separar por comas: https://mi-front.vercel.app,http://localhost:5173
    CORS_ORIGINS: str = (
        "https://alfin-corebanking.vercel.app,"
        "https://alfin-core-banking.vercel.app,"
        "https://alfin-core.vercel.app,"
        "http://localhost:5173,"
        "http://localhost:5174,"
        "http://localhost:3000,"
        "http://127.0.0.1:5173,"
        "http://127.0.0.1:5174,"
        "http://127.0.0.1:3000"
    )

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip().rstrip("/") for origin in self.CORS_ORIGINS.split(",") if origin.strip()]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
