from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model Data Mahasiswa sesuai instruksi tugas
class Item(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] 
    hobi: Optional[str] = None

# Simulasi database menggunakan dictionary
items_db = {}

# ROOT
@app.get("/")
def read_root():
    return {"message": "Selamat Datang di API Tugas 1 Integrasi Sistem"}


# CREATE (POST)
@app.post("/item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Data dengan NIM tersebut sudah ada")
    items_db[item_id] = item.dict()
    return {"message": "Data mahasiswa berhasil ditambahkan", "item": items_db[item_id]}

# READ BY ID (GET)
@app.get("/items/{item_id}") 
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    return {"item_id": item_id, "item": items_db[item_id]}

# UPDATE (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    items_db[item_id] = item.dict()
    return {"message": "Data mahasiswa berhasil diperbarui", "item": items_db[item_id]}

# DELETE (DELETE)
@app.delete ("/item/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    deleted_item = items_db.pop(item_id)
    return {"message": "Data mahasiswa berhasil dihapus", "deleted_item": deleted_item}