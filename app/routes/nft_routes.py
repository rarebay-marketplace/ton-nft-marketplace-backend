from fastapi import APIRouter
from app.controllers.nft_controller import NFTController
from app.schemas.nft import NFTCollectionSchema, NFTItemsSchema

router = APIRouter()


@router.get(
    "/nfts/collections/{collection_address}", response_model=NFTCollectionSchema
)
async def get_nft_collection(collection_address: str):
    return await NFTController.get_collection_by_address(collection_address)


@router.get(
    "/nfts/collections/{collection_address}/items", response_model=NFTItemsSchema
)
async def get_collection_items(collection_address: str):
    return await NFTController.get_items_from_collection(collection_address)
