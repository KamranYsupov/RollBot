from aiogram import Router

from .start import router as start_router
from .registration import router as registration_router
from .roll import router as roll_router
from .html_echo import router as html_echo_router

def get_main_router():
    main_router = Router()

    main_router.include_router(start_router)
    main_router.include_router(registration_router)
    main_router.include_router(roll_router)
    main_router.include_router(html_echo_router)

    return main_router