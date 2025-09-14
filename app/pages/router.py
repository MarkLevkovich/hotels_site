from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels, get_all

router = APIRouter(prefix='/pages', tags=['Frontend'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/hotels')
async def get_hotels_page(request: Request, hotels = Depends(get_hotels)):
    return templates.TemplateResponse(
        'hotels.html',
        {
            'request': request,
            'hotels': hotels
        }
    )


@router.get('/hotels/all')
async def get_hotels_page(request: Request, hotels = Depends(get_all)):
    return templates.TemplateResponse(
        'hotels.html',
        {
            'request': request,
            'hotels': hotels
        }
    )



@router.get('/')
async def get_hello_page(request: Request):
    return templates.TemplateResponse(
        'hello.html',
        {
            'request': request
        }
    )