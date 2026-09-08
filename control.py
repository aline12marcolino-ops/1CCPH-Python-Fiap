from pathlib import Path
import json

DATA_DIR=Path(__file__).resolve().parent/"data"
DATA_DIR.mkdir( exist_ok=True)
DB_PATH=DATA_DIR / "leads.json"

#CRUD
#READ
def read_leads():
    if not DB_PATH.exists():
        return[]
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:     #se corromper,vai voltar  vazio
        return []
#CREATE
def create_leads(leads_dict):
    leads = read_leads() #LISTA E LEADS
    leads.append(leads_dict)
    DB_PATH.write_text(json.dumps(leads, indent=4), encoding="utf-8")
#UPDATE
#DELETE
