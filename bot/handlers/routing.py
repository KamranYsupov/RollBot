from aiogram import Router

from .start import router as start_router
from .registration import router as registration_router

def get_main_router():
    main_router = Router()

    main_router.include_router(start_router)
    main_router.include_router(registration_router)

    return main_router